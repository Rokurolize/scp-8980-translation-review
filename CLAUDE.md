# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## このリポジトリの概要

SCP-8980（SCP Foundation 架空文書）の英語原文 → 日本語訳を査読するプロジェクト。
`source_en.wikidot`（英語原文）と `bad_translation_jp_single.wikidot`（問題訳文）は **両ファイルとも 3505 行で行番号が 1 対 1 に対応している**。

リポジトリはパブリック公開済み。査読結果は GitHub Pages でも閲覧できる：
<https://rokurolize.github.io/scp-8980-translation-review/>

## 正本と生成物の関係

- **正本**: `review_db/segments/*.json`（直接編集する対象）
- **生成物**: `01_PASSAGE_FIXES/*.md`（JSON から再生成されるため手編集しない）
- スキーマ定義: `review_db/schema.json`

## 日常コマンド

```bash
# バリデーション（JSON スキーマ + 行番号照合）
python3 review_registry.py validate

# JSON から Markdown を再生成
python3 review_registry.py render --all
python3 review_registry.py render <segment_id>          # 単体
python3 review_registry.py render --all --single-file   # full_review.md に出力

# 区間・指摘の確認
python3 review_registry.py show <segment_id>
python3 review_registry.py show <segment_id> <issue_id>

# 指摘追加・更新
python3 review_registry.py issue-add <segment_id> <id> <severity> "<heading>"
python3 review_registry.py issue-set <segment_id> <id> --summary "要旨" --en '"quote"' --line 1121 --jp '訳文'

# 原文・訳文の対訳確認
python3 extract_parallel_range.py 1335,1516
python3 extract_parallel_range.py 1335               # 単一行
```

`jsonschema` パッケージが必要（未インストールの場合、validate 時にスキーマ検証がスキップされる）。

## GitHub Pages（MkDocs）

`main` へのプッシュで `.github/workflows/pages.yml` が自動実行される：

1. `python3 review_registry.py render --all` で Markdown を再生成
2. MkDocs（Material テーマ）でビルド
3. `gh-pages` ブランチにデプロイ → Pages に反映

設定ファイルは `mkdocs.yml`（ルート）。`docs/` ディレクトリはビルド中間生成物であり gitignore 済み。

## アーキテクチャ

### `review_registry.py`

メインの CLI ツール。サブコマンド構成：

| コマンド | 役割 |
|---|---|
| `import-current` | `01_PASSAGE_FIXES/*.md` を解析して `review_db/segments/*.json` を初回生成する |
| `validate` | JSON の整合性・行番号照合チェック |
| `render` | JSON → Markdown 再生成 |
| `show` | 区間／指摘を整形表示 |
| `issue-add` | 指摘ひな型を JSON に追加 |
| `issue-set` | 既存指摘の要旨・根拠・修正方針等を更新 |

内部主要関数：`parse_markdown_file()`, `validate_segment()`, `render_markdown()`, `normalize_text()`（引用照合用の正規化）

### JSON データモデル（`review_db/segments/*.json`）

区間単位で 1 ファイル。各 issue の主要フィールド：

```
id          : "E-XX-YY"（error）/ "N-XX-YY"（note）
severity    : "error" | "note" | "out_of_scope"
evidence    : [{en_quote, jp_quote, source_ref: {kind, line}}]
summary     : 要旨
why_bad     : 問題点の箇条書き
fix_directions : 修正方針の箇条書き
extra_blocks : 追加ブロック（"混入箇所:" "修正:" 等）
```

特殊ケース：
- 指摘を持たない区間（CSS/テーマ等）は `extra_sections` に保持
- 原文に対応行がない注記は `source_ref.kind == "note"`

#### テキストフィールドの想定読者

`usage_notes`・`overview`・`conclusions` の文章は、査読を受ける側（翻訳者・修正実施者）に向けて書く。
査読者内部の優先順位・採択決定・作業自己報告（「今回は〜採る」「〜確認する」「補強済み」等）は記載しない。
判断基準の詳細は `review_db/rewrite_criteria.md` を参照。

### `jq` による直接操作例

```bash
# error 指摘の ID 一覧
jq '.issues[] | select(.severity == "error") | .id' review_db/segments/06_addendum2_test_results.json

# note 件数
jq '[.issues[] | select(.severity == "note")] | length' review_db/segments/14_addendum8_health_crawford.json
```

## ライセンス

- **コード・査読データ**（`review_registry.py`、`review_db/`、`01_PASSAGE_FIXES/` 等）: MIT License（権利者: Rokurolize）
- **`source_en.wikidot`**: CC BY-SA 3.0（出典: <https://scp-wiki.wikidot.com/scp-8980>）
- **`bad_translation_jp_single.wikidot`**: CC BY-SA 3.0（出典: <http://scp-jp-sandbox3.wikidot.com/draft:9832594-90-d929>）
