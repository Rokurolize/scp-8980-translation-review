import json
from pathlib import Path
import re


def strip_code_fence(text: str) -> str:
    text = text.strip()
    if len(text) >= 2 and text[0] == "`" and text[-1] == "`":
        return text[1:-1]
    return text


def split_display_parts(raw_values: list[str]) -> list[str]:
    parts: list[str] = []
    for value in raw_values:
        for part in value.split(" / "):
            part = part.strip()
            if part:
                parts.append(part)
    return parts


def migrate_segment(file_path: Path) -> None:
    data = json.load(open(file_path))
    for issue in data["issues"]:
        evidence = []

        # Get all parts
        en_parts = split_display_parts(issue.get("en_display_lines", []))
        jp_parts = split_display_parts(issue.get("jp_display_lines", []))
        source_refs = issue.get("source_refs", [])

        # Zip them together
        max_len = max(len(en_parts), len(jp_parts), len(source_refs))
        for i in range(max_len):
            en = en_parts[i] if i < len(en_parts) else ""
            jp = jp_parts[i] if i < len(jp_parts) else ""
            ref = source_refs[i] if i < len(source_refs) else {"kind": "note", "note": ""}
            evidence.append(
                {
                    "en_quote": en,
                    "jp_quote": jp,
                    "source_ref": ref,
                }
            )

        issue["evidence"] = evidence

        # Remove old parallel arrays
        if "en_display_lines" in issue:
            del issue["en_display_lines"]
        if "line_display_lines" in issue:
            del issue["line_display_lines"]
        if "jp_display_lines" in issue:
            del issue["jp_display_lines"]
        if "source_refs" in issue:
            del issue["source_refs"]

    json.dump(data, open(file_path, "w"), ensure_ascii=False, indent=2)
    print(f"Migrated {file_path.name}")


if __name__ == "__main__":
    segments_dir = Path("review_db/segments")
    for seg_file in sorted(segments_dir.glob("*.json")):
        migrate_segment(seg_file)

    print("Migration complete: all segments migrated to evidence array structure")