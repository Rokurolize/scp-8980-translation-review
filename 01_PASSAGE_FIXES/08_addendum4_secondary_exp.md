# SCP-8980 該当箇所 08 査読

**対象 EN:** `articles/fragment_scp-8980-1/segments/en/08_addendum4_secondary_exp.wikidot`
**対象 JP:** `source_jp.wikidot 行 1409-1484`

## このファイルの使い方

バーンズの雑な言い逃れと、不自然な比喩の直訳を見逃さないこと。
この箇所の指摘はいずれも修正が必要である。

## 総評

この箇所は、後半で本格化する「やわらかい言葉で包む支配」の前振りになっている。
ここで雑さと不快さをきれいな論文語に整えると、バーンズの嫌さがかなり薄まる。

## 直すべき箇所 [ERROR]

### E-08-01 `"or something of the sort"` の雑な逃げが消えている

**EN:** `"or something of the sort"`
**行:** `1441`
**JP:** `あるいはそれに類する`

**要旨:** ここは雑な言い逃れなので、整った論文語にしてはいけない。

**何がだめか:**

- バーンズの説明放棄が見えなくなる
- 倫理委員会コメントが問題にしている雑さが日本語で消える

### E-08-02 `"laser-targeted"` を文字通りのレーザーへ読んでいる

**EN:** `"laser-targeted"`
**行:** `1457`
**JP:** `レーザー銃のように狙いを定めている`

**要旨:** これは具体物ではなく、異様なまでに狙い撃ちであることの比喩である。

**何がだめか:**

- 日本語で急に漫画的になる
- 嫌さより先に比喩のぎこちなさが立つ
- バーンズの擬人化の調子が崩れる

## 補強したい箇所 [NOTE]

### N-08-01 `"I look forward to having it back with us"` の同僚性は残す

**EN:** `"I look forward to having it back with us"`
**行:** `1477`
**JP:** `SCP-8980が我々の元に帰還するのを私は楽しみにしています。`

**要旨:** 訳は大きく外れていないが、`with us` にある「こちら側の一員として戻ってくる」含みを残しておきたい。

**何がだめか:**

- `with us` は「我々と共に」「我々の側に」という帰属感を含む語であり、SCP-8980 が戻ってくる先を「我々のグループ・組織」として位置付けている。これはバーンズが SCP-8980 を同僚・内輪の成員として語る感触を与えており、管理と所属を同時に演出している。
- Congy 訳「我々の元に帰還する」の「帰還」は物体や人が戻ってくるという事実の語であり、`with us`（我々と共に）という帰属感・同僚性の語感が失われる。SCP-8980 が「我々の仲間として」戻るのか、「管理対象として」戻るのかの境界が、`with us` の有無で変わる。

**修正の方向:**

- `我々のもとに戻る` だけで終わらせず、`我々と一緒に` の距離感を保つ
- 戻ってくる事実だけでなく、バーンズの帰属意識も見せる

### N-08-02 `"Following several days..."` の移行期間を丸めない

**EN:** `"Following several days standardizing SCP-8980's containment arrangement, SCP-8980 began to resume active employment at the SCP Foundation on April 18th, 2005, with special considerations for its anomalous capabilities."`
**行:** `1481`
**JP:** `SCP-8980の収容体制標準化に数日を要した後、異常な能力に対して特別な配慮がなされたうえで、SCP-8980は2005年4月18日付でSCP財団での仕事を再開しました。`

**要旨:** `Following` の時系列と `began to resume` の立ち上がりを、単なる「後」と「再開した」で丸めない。

**何がだめか:**

- `Following several days standardizing SCP-8980's containment arrangement` は、収容体制の標準化という準備プロセスが先行していたことを示す前置副詞句である。`Following` は「〜を経て・〜が終わった後に」という時系列の継起を明示しており、移行期間（数日間の標準化プロセス）が再雇用開始の前段階として存在したことを記録している。
- `began to resume active employment` の `began to resume` は「再開し始めた」という段階的な立ち上がりを示している。`resumed`（即座に再開した）ではなく `began to resume`（再開へと向かう段階に入った）という表現は、雇用再開が一度に完全に戻ったのではなく、段階的に立ち上がっていったことを示す。Congy 訳「仕事を再開しました」は即座の完全再開として読まれ、この段階的な立ち上がりのニュアンスが消える。

**修正の方向:**

- `数日を経て` のように、調整期間を前景化する
- `再開した` だけでなく、段階的な再開を残す

### N-08-03 `"incorrect options being selected"` と `"requested to conclude the experiment"` は、起動失敗と申告の両方を残す

**EN:** `"high input latency, incorrect options being selected (such as language), and the device randomly restarting. While SCP-8980 was able to eventually set up the device, it was cited as being uncomfortable and requested to conclude the experiment."`
**行:** `1421`
**JP:** `入力遅延の増加、言語設定の際などの誤ったオプションの選択、デバイスのランダムな再起動などに見舞われ、オペレーティングシステムの設定に著しい困難をきたした。SCP-8980は最終的にデバイスの設定を完了できたが、不快感を訴えたため実験の終了を要求した。`

**要旨:** 起動に手間取った事実だけでなく、本人が不快感を訴えて終了を求めた流れまで残しておきたい。

**何がだめか:**

- `incorrect options being selected` は、SCP-8980 の意図とは異なるオプション（言語設定など）が選択されてしまうという操作上の誤りの具体的な記述である。これはただの不具合ではなく、SCP-8980 が意図した操作通りに機器を動かせなかった（入力の誤作動）という身体的・機能的な失制御を示している。
- `requested to conclude the experiment` は SCP-8980 が自ら実験の終了を申告したという能動的な行為であり、SCP-8980 の主体性（不快を自覚し申告する権利の行使）として読む必要がある。Congy 訳「不快感を訴えたため実験の終了を要求した」は意味は保たれているが、「要求した」という能動性の強度を確認し、SCP-8980 が受動的に終了させられたのではなく自ら申告して終了を求めたことが読める形を維持する。

**修正の方向:**

- `incorrect options` は、単なる不具合ではなく選択の誤りとして読む
- `requested to conclude` は、SCP-8980 の主体的な終了要求として残す

### N-08-04 `"electronic equipment"` は訳語を揃える

**EN:** `"with no prior interaction with other electronic equipment"` / `"due to its potential risk to nearby electronic equipment"`
**行:** `1419` / `1481`
**JP:** `他の電子機器との接触が一切ない` / `近隣の電子デバイスに潜在的なリスクが齎されるため`

**要旨:** `電子機器` と `電子デバイス` の揺れを止めて、同じ語を同じ語で返したい。

**何がだめか:**

- `electronic equipment` は文書全体で同一の概念を指す技術用語であり、同じ語を異なる訳語（「電子機器」と「電子デバイス」）で訳すと、制度文書としての一貫性が崩れ、別の概念として読まれる可能性がある。SCP-8980 の異常性（電子機器への影響）に言及する箇所では、この語の安定した訳語の使用が記録の精度に影響する。
- SCP記事の技術用語が記事内で揺れると、同じ現象・対象について述べていることが分かりにくくなる。`電子機器` または `電子デバイス` のどちらかに統一することで、この異常性の影響範囲について言及するたびに同じ語として認識できる。

**修正の方向:**

- 08 内で `electronic equipment` を `電子機器` に寄せる
- 似た文脈で `電子デバイス` に逃がさない

## 実務上の結論

- `with us` がある箇所は、単なる帰還ではなく所属感まで読む
- 収容体制の標準化は、再開の前段階として訳す
- `began to resume` の立ち上がりは落とさない
