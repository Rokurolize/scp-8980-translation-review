# 査読台帳 `JSON` 化計画

## 目的

- 査読指摘の正本を `JSON` で管理する。
- `01_PASSAGE_FIXES/*.md` は生成物として扱い、手編集をやめる。
- 根拠引用、行番号、要旨、修正方針を機械的に検証できるようにする。
- `jq` で一覧・集計・抽出をしやすくする。

## 正本と生成物

- 正本
  - `review_db/segments/*.json`
  - `review_db/schema.json`
- 生成物
  - `01_PASSAGE_FIXES/*.md`

## 初版で実装するもの

- `review_registry.py`
  - `import-current`
    - 既存の `01_PASSAGE_FIXES/*.md` を取り込み、`review_db/segments/*.json` を生成する。
  - `validate`
    - `JSON` の形と、原文・訳文の根拠行を検査する。
  - `render`
    - `JSON` から `01_PASSAGE_FIXES/*.md` を再生成する。
  - `show`
    - 区間または個別指摘を整形表示する。
  - `issue-add`
    - 指摘のひな型を追加する。
  - `issue-set`
    - 既存指摘の要旨、根拠、箇条書きを更新する。

## `JSON` の基本構造

- 区間単位で 1 ファイルを持つ。
- 上位項目は次を基本とする。
  - `segment_id`
  - `title`
  - `source_en_path`
  - `source_jp_path`
  - `source_range`
  - `usage_notes`
  - `overview`
  - `issues`
  - `extra_sections`
  - `conclusions`
- 各 `issue` は次を持つ。
  - `id`
  - `severity`
  - `order`
  - `heading`
  - `en_display_lines`
  - `line_display_lines`
  - `jp_display_lines`
  - `source_refs`
  - `summary`
  - `why_bad`
  - `fix_directions`
  - `extra_blocks`

## 例外形の扱い

- `01_css_and_theme.md` のように指摘一覧を持たない文書は、`extra_sections` に保持する。
- `OUT-OF-SCOPE` は `severity: "out_of_scope"` として `issues` に入れる。
- 原文に相当行がない注記は `source_refs.kind == "note"` で保持する。
- `**混入箇所:**` や `**修正:**` のような追加項目は `extra_blocks` に保持する。

## 検証方針

- `JSON` の必須項目を検査する。
- `source_en.wikidot` と `bad_translation_jp_single.wikidot` の行数一致を検査する。
- `**行:**` の番号が存在する場合、対応する原文・訳文行との照合を行う。
- 照合は正規化比較を許可する。
  - 前後引用符を外す
  - `**`、`//`、`{}` を除く
  - 連続空白を圧縮する
- 既存文書にある説明的な引用や欠落指摘は、即失敗ではなく警告として出す。

## 運用

### 初回取り込み

```bash
rtk python review_registry.py import-current
rtk python review_registry.py validate
```

### 一覧と確認

```bash
rtk jq '.issues[] | select(.severity == "error") | .id' review_db/segments/06_addendum2_test_results.json
rtk jq '[.issues[] | select(.severity == "note")] | length' review_db/segments/14_addendum8_health_crawford.json
rtk python review_registry.py show 16_addendum9_depression E-16-04
```

### 文書再生成

```bash
rtk python review_registry.py render --all
```

### 指摘追加

```bash
rtk python review_registry.py issue-add 06_addendum2_test_results E-06-99 error "新規見出し"
rtk python review_registry.py issue-set 06_addendum2_test_results E-06-99 --summary "要旨" --en '"quote"' --line 1121 --jp '訳文'
```

## 受け入れ条件

- `import-current` が既存の `01_PASSAGE_FIXES/*.md` をすべて `JSON` 化できること。
- `validate` が致命的な不整合を出さず完走すること。
- `render --all` で区間別文書を再生成できること。
- 日常的な追加・更新を `review_registry.py` と `jq` の組み合わせで行えること。
