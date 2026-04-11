from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
PASSAGES_DIR = ROOT / "01_PASSAGE_FIXES"
REVIEW_DB_DIR = ROOT / "review_db"
SEGMENTS_DIR = REVIEW_DB_DIR / "segments"
SOURCE_EN_PATH = ROOT / "source_en.wikidot"
SOURCE_JP_PATH = ROOT / "bad_translation_jp_single.wikidot"

SECTION_SEVERITY = {
    "直すべき箇所 [ERROR]": "error",
    "補強したい箇所 [NOTE]": "note",
    "このファイルでは採らない論点 [OUT-OF-SCOPE]": "out_of_scope",
}

SEVERITY_SECTION_TITLE = {
    "error": "直すべき箇所 [ERROR]",
    "note": "補強したい箇所 [NOTE]",
    "out_of_scope": "このファイルでは採らない論点 [OUT-OF-SCOPE]",
}

ISSUE_ID_RE = re.compile(r"^([A-Z]-[0-9]{2}-[0-9A-Za-z]+)\s+(.*)$")
HEADING_RE = re.compile(r"^##\s+(.+)$")
SUBHEADING_RE = re.compile(r"^###\s+(.+)$")
LABEL_RE = re.compile(r"^\*\*(.+?):\*\*\s*(.*)$")
TARGET_RE = re.compile(r"^\*\*対象\s+(EN|JP):\*\*\s*(.*)$")
JP_RANGE_RE = re.compile(r"行\s+([0-9]+)-([0-9]+)\s+付近")


@dataclass
class ValidationMessage:
    level: str
    segment_id: str
    message: str


def load_text_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def strip_code_fence(text: str) -> str:
    text = text.strip()
    if len(text) >= 2 and text[0] == "`" and text[-1] == "`":
        return text[1:-1]
    return text


def normalize_text(text: str) -> str:
    value = text.strip()
    value = strip_code_fence(value)
    value = value.strip('"“”')
    value = re.sub(r"\*\*|//|\{|\}", "", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip().lower()


def split_display_parts(raw_values: list[str]) -> list[str]:
    parts: list[str] = []
    for value in raw_values:
        for part in value.split(" / "):
            part = part.strip()
            if part:
                parts.append(part)
    return parts


def parse_source_refs(raw_values: list[str]) -> list[dict[str, Any]]:
    refs: list[dict[str, Any]] = []
    for part in split_display_parts(raw_values):
        stripped = strip_code_fence(part)
        if stripped.isdigit():
            refs.append({"kind": "line", "line": int(stripped)})
        elif stripped:
            refs.append({"kind": "note", "note": stripped})
    return refs


def split_blocks(lines: list[str]) -> list[str]:
    blocks: list[list[str]] = []
    current: list[str] = []
    for line in lines:
        if line.strip():
            current.append(line.rstrip())
            continue
        if current:
            blocks.append(current)
            current = []
    if current:
        blocks.append(current)
    return ["\n".join(block) for block in blocks]


def issue_sort_key(issue: dict[str, Any]) -> tuple[int, str]:
    return (int(issue["order"]), issue["id"])


def parse_markdown_file(path: Path) -> dict[str, Any]:
    lines = load_text_lines(path)
    if not lines or not lines[0].startswith("# "):
        raise ValueError(f"{path.name}: 題名行が見つかりません")

    title = lines[0][2:].strip()
    source_en_path = ""
    source_jp_path = "bad_translation_jp_single.wikidot"
    source_range = {"start": None, "end": None}
    usage_notes: list[str] = []
    overview: list[str] = []
    conclusions: list[str] = []
    issues: list[dict[str, Any]] = []
    extra_sections: list[dict[str, Any]] = []

    current_section: str | None = None
    section_lines: list[str] = []
    issue_severity: str | None = None
    i = 1

    while i < len(lines):
        line = lines[i].rstrip()
        target_match = TARGET_RE.match(line)
        if target_match:
            target_kind, target_value = target_match.groups()
            target_value = target_value.strip()
            if target_kind == "EN":
                source_en_path = strip_code_fence(target_value)
            else:
                source_jp_path = strip_code_fence(target_value)
                range_match = JP_RANGE_RE.search(target_value)
                if range_match:
                    start, end = range_match.groups()
                    source_range = {
                        "start": int(start),
                        "end": int(end),
                        "note": strip_code_fence(target_value),
                    }
            i += 1
            continue

        heading_match = HEADING_RE.match(line)
        if heading_match:
            if current_section is not None and section_lines:
                store_section(
                    current_section,
                    section_lines,
                    issue_severity,
                    usage_notes,
                    overview,
                    conclusions,
                    issues,
                    extra_sections,
                )
                section_lines = []
            current_section = heading_match.group(1).strip()
            issue_severity = SECTION_SEVERITY.get(current_section, None)
            i += 1
            continue

        section_lines.append(lines[i])
        i += 1

    if current_section is not None and section_lines:
        store_section(
            current_section,
            section_lines,
            issue_severity,
            usage_notes,
            overview,
            conclusions,
            issues,
            extra_sections,
        )

    segment_id = path.stem
    issues.sort(key=issue_sort_key)
    return {
        "segment_id": segment_id,
        "title": title,
        "source_en_path": source_en_path,
        "source_jp_path": source_jp_path,
        "source_range": source_range,
        "usage_notes": usage_notes,
        "overview": overview,
        "issues": issues,
        "extra_sections": extra_sections,
        "conclusions": conclusions,
    }


def store_section(
    section_title: str,
    section_lines: list[str],
    issue_severity: str | None,
    usage_notes: list[str],
    overview: list[str],
    conclusions: list[str],
    issues: list[dict[str, Any]],
    extra_sections: list[dict[str, Any]],
) -> None:
    if section_title == "このファイルの使い方":
        usage_notes.extend(split_blocks(section_lines))
        return
    if section_title == "総評":
        overview.extend(split_blocks(section_lines))
        return
    if section_title == "実務上の結論":
        conclusions.extend(split_blocks(section_lines))
        return
    if issue_severity is not None:
        issues.extend(parse_issue_section(section_lines, issue_severity))
        return
    extra_sections.append(
        {
            "title": section_title,
            "blocks": split_blocks(section_lines),
        }
    )


def parse_issue_section(lines: list[str], severity: str) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []
    current_heading: str | None = None
    current_lines: list[str] = []
    order = 0
    for raw_line in lines:
        match = SUBHEADING_RE.match(raw_line.rstrip())
        if match:
            if current_heading is not None:
                order += 1
                issues.append(parse_issue_block(current_heading, current_lines, severity, order))
            current_heading = match.group(1).strip()
            current_lines = []
            continue
        if current_heading is not None:
            current_lines.append(raw_line)
    if current_heading is not None:
        order += 1
        issues.append(parse_issue_block(current_heading, current_lines, severity, order))
    return issues


def parse_issue_block(heading_text: str, lines: list[str], severity: str, order: int) -> dict[str, Any]:
    match = ISSUE_ID_RE.match(heading_text)
    if match:
      issue_id, heading = match.groups()
    else:
      issue_id = f"UNASSIGNED-{order:02d}"
      heading = heading_text

    issue: dict[str, Any] = {
        "id": issue_id,
        "severity": severity,
        "order": order,
        "heading": heading,
        "evidence": [],
        "summary": None,
        "why_bad": [],
        "fix_directions": [],
        "extra_blocks": [],
    }

    en_lines = []
    line_lines = []
    jp_lines = []

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue

        label_match = LABEL_RE.match(line)
        if not label_match:
            if issue["summary"] is None:
                issue["summary"] = line
            else:
                issue["summary"] = f"{issue['summary']}\n{line}"
            i += 1
            continue

        label, raw_value = label_match.groups()
        label = label.strip()
        raw_value = raw_value.rstrip()

        if label == "EN":
            en_lines.append(raw_value)
            i += 1
            continue
        if label == "行":
            line_lines.append(raw_value)
            i += 1
            continue
        if label == "JP":
            jp_lines.append(raw_value)
            i += 1
            continue

        if label == "要旨":
            text_lines = [raw_value] if raw_value else []
            i += 1
            while i < len(lines):
                next_line = lines[i].rstrip()
                if not next_line.strip():
                    i += 1
                    if text_lines:
                        break
                    continue
                if LABEL_RE.match(next_line):
                    break
                if next_line.startswith("- "):
                    break
                text_lines.append(next_line)
                i += 1
            issue["summary"] = "\n".join(text_lines).strip() if text_lines else None
            continue

        if label in {"何がだめか", "修正の方向", "直すなら"}:
            items: list[str] = []
            i += 1
            while i < len(lines):
                next_line = lines[i].rstrip()
                if not next_line.strip():
                    i += 1
                    if items:
                        break
                    continue
                if LABEL_RE.match(next_line):
                    break
                if next_line.startswith("- "):
                    items.append(next_line[2:].strip())
                    i += 1
                    continue
                if items:
                    items[-1] = f"{items[-1]}\n{next_line}"
                else:
                    items.append(next_line)
                i += 1
            if label == "何がだめか":
                issue["why_bad"].extend(items)
            elif label == "修正の方向":
                issue["fix_directions"].extend(items)
            else:
                issue["extra_blocks"].append(
                    {
                        "label": label,
                        "kind": "list",
                        "items": items,
                    }
                )
            continue

        text_lines = [raw_value] if raw_value else []
        i += 1
        while i < len(lines):
            next_line = lines[i].rstrip()
            if not next_line.strip():
                i += 1
                if text_lines:
                    break
                continue
            if LABEL_RE.match(next_line) or next_line.startswith("- "):
                break
            text_lines.append(next_line)
            i += 1
        issue["extra_blocks"].append(
            {
                "label": label,
                "kind": "text",
                "value": "\n".join(text_lines).strip(),
            }
        )

    issue["source_refs"] = parse_source_refs(issue["line_display_lines"])
    return issue


def render_markdown(segment: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append(f"# {segment['title']}")
    lines.append("")
    lines.append(f"**対象 EN:** `{segment['source_en_path']}`")
    lines.append(f"**対象 JP:** `{segment['source_jp_path']}`")
    lines.append("")

    if segment["usage_notes"]:
        lines.append("## このファイルの使い方")
        lines.append("")
        render_blocks(lines, segment["usage_notes"])

    if segment["overview"]:
        lines.append("## 総評")
        lines.append("")
        render_blocks(lines, segment["overview"])

    grouped: dict[str, list[dict[str, Any]]] = {"error": [], "note": [], "out_of_scope": []}
    for issue in sorted(segment["issues"], key=issue_sort_key):
        grouped[issue["severity"]].append(issue)

    for severity in ("error", "note", "out_of_scope"):
        if not grouped[severity]:
            continue
        lines.append(SEVERITY_SECTION_TITLE[severity].join(["## ", ""]))
        lines[-1] = f"## {SEVERITY_SECTION_TITLE[severity]}"
        lines.append("")
        for issue in grouped[severity]:
            render_issue(lines, issue)

    for section in segment["extra_sections"]:
        lines.append(f"## {section['title']}")
        lines.append("")
        render_blocks(lines, section["blocks"])

    if segment["conclusions"]:
        lines.append("## 実務上の結論")
        lines.append("")
        render_blocks(lines, segment["conclusions"])

    return "\n".join(lines).rstrip() + "\n"


def render_blocks(lines: list[str], blocks: list[str]) -> None:
    for block in blocks:
        for raw_line in block.split("\n"):
            lines.append(raw_line)
        lines.append("")


def render_issue(lines: list[str], issue: dict[str, Any]) -> None:
    lines.append(f"### {issue['id']} {issue['heading']}")
    lines.append("")
    
    # Render evidence - group / for display when multiple
    if issue["evidence"]:
        en_values = []
        line_values = []
        jp_values = []
        for ev in issue["evidence"]:
            if ev["en_quote"]:
                en_values.append(ev["en_quote"])
            if ev["source_ref"]["kind"] == "line":
                line_values.append(str(ev["source_ref"]["line"]))
            elif ev["source_ref"]["kind"] == "note":
                line_values.append(ev["source_ref"]["note"])
            if ev["jp_quote"]:
                jp_values.append(ev["jp_quote"])
        
        if en_values:
            lines.append(f"**EN:** {' / '.join(en_values)}")
        if line_values:
            lines.append(f"**行:** {' / '.join(line_values)}")
        if jp_values:
            lines.append(f"**JP:** {' / '.join(jp_values)}")
        lines.append("")

    for block in issue["extra_blocks"]:
        if block["label"] in {"混入箇所", "修正"} and block["kind"] == "text":
            lines.append(f"**{block['label']}:** {block['value']}")
            lines.append("")

    if issue["summary"]:
        summary_lines = issue["summary"].split("\n")
        lines.append(f"**要旨:** {summary_lines[0]}")
        for extra_line in summary_lines[1:]:
            lines.append(extra_line)
        lines.append("")

    if issue["why_bad"]:
        lines.append("**何がだめか:**")
        lines.append("")
        for item in issue["why_bad"]:
            lines.append(f"- {item}")
        lines.append("")

    if issue["fix_directions"]:
        lines.append("**修正の方向:**")
        lines.append("")
        for item in issue["fix_directions"]:
            lines.append(f"- {item}")
        lines.append("")

    for block in issue["extra_blocks"]:
        if block["label"] in {"混入箇所", "修正"}:
            continue
        if block["kind"] == "text":
            lines.append(f"**{block['label']}:** {block['value']}")
            lines.append("")
        else:
            lines.append(f"**{block['label']}:**")
            lines.append("")
            for item in block["items"]:
                lines.append(f"- {item}")
            lines.append("")


def validate_segment(
    segment: dict[str, Any],
    source_en_lines: list[str],
    source_jp_lines: list[str],
) -> list[ValidationMessage]:
    messages: list[ValidationMessage] = []
    segment_id = segment["segment_id"]
    required_keys = {
        "segment_id",
        "title",
        "source_en_path",
        "source_jp_path",
        "source_range",
        "usage_notes",
        "overview",
        "issues",
        "extra_sections",
        "conclusions",
    }
    missing = sorted(required_keys - set(segment))
    if missing:
        messages.append(ValidationMessage("error", segment_id, f"必須項目欠落: {', '.join(missing)}"))
        return messages

    seen_ids: set[str] = set()
    seen_orders: set[int] = set()
    for issue in segment["issues"]:
        issue_id = issue["id"]
        order = int(issue["order"])
        if issue_id in seen_ids:
            messages.append(ValidationMessage("error", segment_id, f"重複した指摘番号: {issue_id}"))
        seen_ids.add(issue_id)
        if order in seen_orders:
            messages.append(ValidationMessage("warning", segment_id, f"重複した表示順: {order}"))
        seen_orders.add(order)
        messages.extend(validate_issue(segment_id, issue, source_en_lines, source_jp_lines))
    return messages


def validate_issue(
    segment_id: str,
    issue: dict[str, Any],
    source_en_lines: list[str],
    source_jp_lines: list[str],
) -> list[ValidationMessage]:
    messages: list[ValidationMessage] = []
    issue_prefix = f"{segment_id}:{issue['id']}"
    
    for ev_idx, evidence in enumerate(issue["evidence"]):
        en_part = evidence["en_quote"]
        jp_part = evidence["jp_quote"]
        ref = evidence["source_ref"]
        
        if ref["kind"] == "line":
            line_no = int(ref["line"])
            if line_no < 1 or line_no > len(source_en_lines):
                messages.append(ValidationMessage("error", segment_id, f"{issue_prefix} 行番号範囲外: {line_no}"))

        if ref["kind"] == "line" and en_part:
            source_line = source_en_lines[ref["line"] - 1]
            if normalize_text(en_part) != normalize_text(source_line):
                messages.append(
                    ValidationMessage(
                        "warning",
                        segment_id,
                        f"{issue_prefix} 原文説明文のため照合保留: {en_part}",
                    )
                )

        if ref["kind"] == "line" and jp_part:
            normalized_jp = normalize_text(jp_part)
            if normalized_jp in {"なし", "当該一文が欠落"}:
                continue
            source_line = source_jp_lines[ref["line"] - 1]
            if normalized_jp != normalize_text(source_line):
                messages.append(
                    ValidationMessage(
                        "warning",
                        segment_id,
                        f"{issue_prefix} 訳文照合差異: {jp_part}",
                    )
                )

    return messages


def command_import_current(args: argparse.Namespace) -> int:
    ensure_dir(SEGMENTS_DIR)
    count = 0
    for path in sorted(PASSAGES_DIR.glob("*.md")):
        segment = parse_markdown_file(path)
        output_path = SEGMENTS_DIR / f"{path.stem}.json"
        output_path.write_text(json.dumps(segment, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        count += 1
    print(f"取り込み完了: {count} 件")
    return 0


def command_validate(args: argparse.Namespace) -> int:
    if not SEGMENTS_DIR.exists():
        print("review_db/segments が存在しません。先に import-current を実行してください。", file=sys.stderr)
        return 1

    source_en_lines = load_text_lines(SOURCE_EN_PATH)
    source_jp_lines = load_text_lines(SOURCE_JP_PATH)
    if len(source_en_lines) != len(source_jp_lines):
        print("source_en.wikidot と bad_translation_jp_single.wikidot の行数が一致しません。", file=sys.stderr)
        return 1

    # Load schema
    jsonschema = None
    schema = None
    try:
        import jsonschema
        schema = json.loads((REVIEW_DB_DIR / "schema.json").read_text(encoding="utf-8"))
    except ImportError:
        print("jsonschema がインストールされていないためスキーマ検証をスキップします", file=sys.stderr)
    except FileNotFoundError:
        print("schema.json が存在しないためスキーマ検証をスキップします", file=sys.stderr)

    messages: list[ValidationMessage] = []
    seen_segment_ids = set()
    for path in sorted(SEGMENTS_DIR.glob("*.json")):
        segment = json.loads(path.read_text(encoding="utf-8"))
        
        # Schema validation
        if jsonschema and schema:
            try:
                jsonschema.validate(segment, schema)
            except jsonschema.ValidationError as e:
                messages.append(ValidationMessage(
                    "error", 
                    segment.get("segment_id", path.stem), 
                    f"スキーマ不適合: {e.message}"
                ))
        
        # Segment ID uniqueness
        if segment["segment_id"] in seen_segment_ids:
            messages.append(ValidationMessage(
                "error", 
                segment["segment_id"], 
                f"重複した segment_id"
            ))
        seen_segment_ids.add(segment["segment_id"])
        
        # Severity vs ID prefix check
        for issue in segment["issues"]:
            expected_prefix = "E-" if issue["severity"] == "error" else "N-"
            if issue["severity"] in ["error", "note"] and not issue["id"].startswith(expected_prefix):
                messages.append(ValidationMessage(
                    "warning",
                    segment["segment_id"],
                    f"{issue['id']}: 接頭辞不一致 severity={issue['severity']}"
                ))
        
        messages.extend(validate_segment(segment, source_en_lines, source_jp_lines))

    errors = [msg for msg in messages if msg.level == "error"]
    warnings = [msg for msg in messages if msg.level == "warning"]
    for msg in errors + warnings:
        prefix = "ERROR" if msg.level == "error" else "WARN"
        print(f"{prefix} {msg.segment_id}: {msg.message}")
    print(f"検証結果: error={len(errors)} warning={len(warnings)}")
    return 1 if errors else 0


def load_segment(segment_id: str) -> tuple[Path, dict[str, Any]]:
    path = SEGMENTS_DIR / f"{segment_id}.json"
    if not path.exists():
        raise FileNotFoundError(f"{segment_id} が見つかりません")
    return path, json.loads(path.read_text(encoding="utf-8"))


def save_segment(path: Path, segment: dict[str, Any]) -> None:
    path.write_text(json.dumps(segment, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def command_render(args: argparse.Namespace) -> int:
    if args.all:
        targets = sorted(SEGMENTS_DIR.glob("*.json"))
    else:
        if not args.segment_id:
            print("segment_id か --all が必要です。", file=sys.stderr)
            return 1
        targets = [SEGMENTS_DIR / f"{args.segment_id}.json"]

    for path in targets:
        segment = json.loads(path.read_text(encoding="utf-8"))
        output_path = PASSAGES_DIR / f"{segment['segment_id']}.md"
        output_path.write_text(render_markdown(segment), encoding="utf-8")
        print(f"再生成: {output_path.relative_to(ROOT)}")
    return 0


def command_show(args: argparse.Namespace) -> int:
    _, segment = load_segment(args.segment_id)
    if args.issue_id:
        issue = next((item for item in segment["issues"] if item["id"] == args.issue_id), None)
        if issue is None:
            print(f"{args.issue_id} が見つかりません。", file=sys.stderr)
            return 1
        print(render_markdown({**segment, "issues": [issue], "extra_sections": [], "conclusions": []}).rstrip())
        return 0
    print(json.dumps(segment, ensure_ascii=False, indent=2))
    return 0


def command_issue_add(args: argparse.Namespace) -> int:
    path, segment = load_segment(args.segment_id)
    if any(issue["id"] == args.issue_id for issue in segment["issues"]):
        print(f"{args.issue_id} は既に存在します。", file=sys.stderr)
        return 1
    next_order = max((int(issue["order"]) for issue in segment["issues"]), default=0) + 1
    segment["issues"].append(
        {
            "id": args.issue_id,
            "severity": args.severity,
            "order": next_order,
            "heading": args.heading,
            "evidence": [],
            "summary": None,
            "why_bad": [],
            "fix_directions": [],
            "extra_blocks": [],
        }
    )
    segment["issues"].sort(key=issue_sort_key)
    save_segment(path, segment)
    print(f"追加: {args.segment_id} {args.issue_id}")
    return 0


def command_issue_set(args: argparse.Namespace) -> int:
    path, segment = load_segment(args.segment_id)
    issue = next((item for item in segment["issues"] if item["id"] == args.issue_id), None)
    if issue is None:
        print(f"{args.issue_id} が見つかりません。", file=sys.stderr)
        return 1

    if args.heading is not None:
        issue["heading"] = args.heading
    if args.summary is not None:
        issue["summary"] = args.summary
    if args.why_bad:
        issue["why_bad"] = args.why_bad
    if args.fix_direction:
        issue["fix_directions"] = args.fix_direction
    
    # Add/append evidence
    if args.en is not None or args.line is not None or args.jp is not None:
        ref = {"kind": "note", "note": ""}
        if args.line is not None:
            ref = parse_source_refs([args.line])[0]
        issue["evidence"].append({
            "en_quote": args.en or "",
            "jp_quote": args.jp or "",
            "source_ref": ref
        })

    save_segment(path, segment)
    print(f"更新: {args.segment_id} {args.issue_id}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="査読台帳を JSON 正本として管理するための道具")
    subparsers = parser.add_subparsers(dest="command", required=True)

    import_parser = subparsers.add_parser("import-current", help="既存の査読文書を JSON 化する")
    import_parser.set_defaults(func=command_import_current)

    validate_parser = subparsers.add_parser("validate", help="JSON と根拠行を検証する")
    validate_parser.set_defaults(func=command_validate)

    render_parser = subparsers.add_parser("render", help="JSON から Markdown を再生成する")
    render_parser.add_argument("segment_id", nargs="?")
    render_parser.add_argument("--all", action="store_true")
    render_parser.set_defaults(func=command_render)

    show_parser = subparsers.add_parser("show", help="区間または個別指摘を表示する")
    show_parser.add_argument("segment_id")
    show_parser.add_argument("issue_id", nargs="?")
    show_parser.set_defaults(func=command_show)

    add_parser = subparsers.add_parser("issue-add", help="指摘を追加する")
    add_parser.add_argument("segment_id")
    add_parser.add_argument("issue_id")
    add_parser.add_argument("severity", choices=["error", "note", "out_of_scope"])
    add_parser.add_argument("heading")
    add_parser.set_defaults(func=command_issue_add)

    set_parser = subparsers.add_parser("issue-set", help="指摘を更新する")
    set_parser.add_argument("segment_id")
    set_parser.add_argument("issue_id")
    set_parser.add_argument("--heading")
    set_parser.add_argument("--summary")
    set_parser.add_argument("--en")
    set_parser.add_argument("--line")
    set_parser.add_argument("--jp")
    set_parser.add_argument("--why-bad", action="append", default=[])
    set_parser.add_argument("--fix-direction", action="append", default=[])
    set_parser.set_defaults(func=command_issue_set)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
