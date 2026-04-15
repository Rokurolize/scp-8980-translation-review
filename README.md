# SCP-8980 日本語訳査読レビュー

SCP-8980（SCP Foundation 架空文書）の英語原文から日本語訳への翻訳精度を査読するプロジェクトです。

## 概要

- 英語原文（`source_en.wikidot`）と日本語訳（`bad_translation_jp_single.wikidot`）を 1 行単位で対応付け
- 誤訳・訳抜け・ニュアンスの歪みを `review_db/segments/*.json` に記録
- `review_registry.py render --all` で `01_PASSAGE_FIXES/` 配下の Markdown を自動生成
- GitHub Pages でレビュー結果を公開：<https://Rokurolize.github.io/scp-8980-translation-review/>

## 主なコマンド

```bash
# バリデーション
python3 review_registry.py validate

# Markdown 再生成
python3 review_registry.py render --all

# 指摘追加・更新
python3 review_registry.py issue-add <segment_id> <id> <severity> "<heading>"
python3 review_registry.py issue-set <segment_id> <id> --summary "要旨" --en '"quote"' --line 1121 --jp '訳文'

# 対訳確認
python3 extract_parallel_range.py 1335,1516
```

## ライセンス

### コード・査読コンテンツ

本リポジトリのスクリプト（`review_registry.py` 等）および査読データ（`review_db/`、`01_PASSAGE_FIXES/`）は **MIT License** のもとで公開しています。
詳細は [LICENSE](LICENSE) を参照してください。

### 収録原文ファイル

以下のファイルは **CC BY-SA 3.0** ライセンスのもとで配布されます。

| ファイル | 出典 | ライセンス |
|---|---|---|
| `source_en.wikidot` | <https://scp-wiki.wikidot.com/scp-8980> | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) |
| `bad_translation_jp_single.wikidot` | <http://scp-jp-sandbox3.wikidot.com/draft:9832594-90-d929> | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) |
