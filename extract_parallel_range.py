#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


EMPTY_MARKER = "(空行)"
RANGE_RE = re.compile(r"^(?P<start>\d+)(?:(?P<sep>[,-])(?P<end>\d+))?$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="source_en.wikidot と source_jp.wikidot から指定行範囲の対訳を抽出します。"
    )
    parser.add_argument("line_range", help="単独行 '1335'、または範囲 '1335,1516' / '1335-1516'")
    parser.add_argument("--source", default="source_en.wikidot", help="原文ファイル")
    parser.add_argument("--jp", default="source_jp.wikidot", help="日本語ファイル")
    return parser.parse_args()


def fail(message: str) -> int:
    print(message, file=sys.stderr)
    return 1


def read_lines(path_str: str) -> list[str]:
    path = Path(path_str)
    return path.read_text(encoding="utf-8").splitlines()


def parse_line_range(raw: str) -> tuple[int, int]:
    match = RANGE_RE.fullmatch(raw)
    if not match:
        raise ValueError(f"不正な範囲指定です: {raw}")

    start = int(match.group("start"))
    end = int(match.group("end") or start)

    if start < 1 or end < 1:
        raise ValueError("行番号は 1 以上で指定してください。")
    if start > end:
        raise ValueError("開始行は終了行以下で指定してください。")

    return start, end


def fence_for(text: str) -> str:
    longest = 0
    current = 0
    for char in text:
        if char == "`":
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return "`" * (longest + 1 if longest >= 3 else 3)


def format_inline_code(text: str) -> str:
    if text == "":
        return EMPTY_MARKER
    fence = fence_for(text)
    return f"{fence}{text}{fence}"


def format_block(line_no: int, en_line: str, jp_line: str) -> str:
    return "\n".join(
        [
            f"### {line_no}",
            f"**EN:** {format_inline_code(en_line)}",
            f"**JP:** {format_inline_code(jp_line)}",
        ]
    )


def main() -> int:
    args = parse_args()

    try:
        start, end = parse_line_range(args.line_range)
    except ValueError as exc:
        return fail(str(exc))

    try:
        source_lines = read_lines(args.source)
        jp_lines = read_lines(args.jp)
    except FileNotFoundError as exc:
        return fail(f"ファイルが見つかりません: {exc.filename}")

    if len(source_lines) != len(jp_lines):
        return fail(
            f"入力ファイルの行数が一致しません: source={len(source_lines)} jp={len(jp_lines)}"
        )

    if end > len(source_lines):
        return fail(f"指定範囲が総行数を超えています: max={len(source_lines)}")

    blocks = [
        format_block(line_no, source_lines[line_no - 1], jp_lines[line_no - 1])
        for line_no in range(start, end + 1)
    ]
    print("\n\n".join(blocks))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
