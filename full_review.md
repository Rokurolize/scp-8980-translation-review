# SCP-8980 該当箇所 01 査読

**対象 EN:** `articles/fragment_scp-8980-1/segments/en/01_css_and_theme.wikidot`
**対象 JP:** `bad_translation_jp_single.wikidot`

## このファイルの使い方

この箇所は本文訳の修正箇所を探す場ではなく、表示層を壊さないための保全メモである。
この帯では個別誤訳を量産するより、表示層を壊さないことのほうが重要である。したがって、ここでやるべきことは「訳す」より「壊さない」ことである。

## 総評

現行稿は、少なくとも次の点では致命傷を避けている。

- CSS 変数の装飾文字列を本文扱いしていない
- `@import`、`theme_url`、外部アセット参照を崩していない
- `[[module]]` と CSS ブロックの分割構造を保っている

この層を本文感覚で整形すると、該当箇所 02 と 03 の表示まで巻き込んで壊す。
したがって、該当箇所 01 は「修正対象が少ない」のではなく、「誤って触ると被害が大きい」範囲として扱う。

## 保全方針

### 1. CSS 変数の英語文字列は訳さない

対象例:

- `--header-title: "ETHICS COMMITTEE";`
- `--header-subtitle: "INTERNAL RECORDKEEPING INTERFACE";`

これらは本文の未訳ではなく、意匠の一部である。
可視見出しの日本語化は本文側で行うべきであり、ここまで日本語化すると、表示の二重化や役割分担の崩れが起きる。

### 2. URL、ファイル名、`theme_url` は一字もいじらない

対象例:

- `@import url('https://scp-wiki.wikidot.com/local--files/scp-8980/departuremono.css');`
- `theme_url=/local--files/scp-8980/modeL.css`

ここは「読みやすくする」ための調整対象ではない。
大文字小文字やファイル名の見た目が気になっても、訳文修正ではなく保全対象として扱う。

### 3. `[[module]]` の構造はまとめ直さない

見た目に重複していても、読み込み順や作用範囲は本文からは見えない。
特にタブ切替、ポップアップ、色覚対応表示と絡むため、文法破損がない限り再編しない。

## 実務上の結論

- 該当箇所 01 では、本文訳の修正は原則しない。
- 表示層に触る必要が生じた場合は、該当箇所 02 と 03 の可視文言修正と切り分けて扱う。
- ここを変更した場合は、少なくともポップアップ表示、タブ切替、テーマ切替の再確認を前提にする。

---

# SCP-8980 該当箇所 02 査読

**対象 EN:** `articles/fragment_scp-8980-1/segments/en/02_ec_popup_modal.wikidot`
**対象 JP:** `bad_translation_jp_single.wikidot`

## このファイルの使い方

- `[ERROR]` はそのまま修正対象
- `[OUT-OF-SCOPE]` は公開面から除去すべき混入物

この箇所は読者の最初の入口なので、声の強度を落とさないことと、公開面に作業メモを残さないことが最優先になる。

## 総評

現行稿はレイアウト自体は大崩れしていないが、次の 2 点は修正必須である。

- 倫理委員会の調査中というレジスターが、違反確定の断定に早まっている
- 原文にない作業用の折り畳みメモと sandbox URL がそのまま残っている

## 直すべき箇所 [ERROR]

### E-02-01 「調査中」を「違反確定」に早めている

**EN:** `"undergoing active Ethics Committee investigation for violation of the SCP Foundation's Code of Conduct"`
**行:** 702
**JP:** `SCP財団の行動規範に違反しているため、倫理委員会による調査対象となっています。`

**要旨:** この書き方は強すぎる。ここで必要なのは有罪宣告ではなく、調査中の警告である。

**何がだめか:**

- `"for violation of ..."` は調査理由であって、有罪認定ではない
- `違反しているため` と言い切ると、読者は委員会が最初から結論を出していると読む
- 以後の注釈付き本文が「検証」ではなく「処分済み文書」に見えてしまう

**修正の方向:**

- `違反の疑い`
- `継続調査の対象`
- `信頼できる情報源として扱うべきではない`

### E-02-02 公開面に原文にない作業メモが混入している

**混入箇所:** `[[collapsible show="+ 査読の前に必ずご一読ください" ...]]`、sandbox URL、アクセシビリティ未対応メモ

**要旨:** これは訳文の良し悪し以前の公開事故であり、本文から完全に外す。

**何がだめか:**

- 原文記事に存在しない
- Congy 氏の作業メモであって、作品本文でも訳注でもない
- sandbox URL と内部運用情報が公開面に露出する

**修正の方向:**

- 折り畳みブロック全体を公開用原稿から除去する
- 本文修正の主導線には残さない

## 実務上の結論

- ポップアップ本文は「調査中」で止める
- 作業メモは該当箇所 02 から一掃する
- この箇所では、訳の巧拙よりまず公開面の混入物除去を優先する

---

# SCP-8980 該当箇所 03 査読

**対象 EN:** `articles/fragment_scp-8980-1/segments/en/03_tabview_and_ec_memorandum.wikidot`
**対象 JP:** `bad_translation_jp_single.wikidot`

## このファイルの使い方

- `[ERROR]` は題名や制度文の基準線を壊しているため優先修正
- この箇所は入口文なので、弱い日本語や無難な注意文に落とさない

## 総評

ここは題名、内容警告、倫理委員会覚書という「読者の読み方を決める入口」が一度に並ぶ。
量は短いが、ここで言葉の温度を落とすと本文全体の牙が抜ける。

今回、強く採るべき論点は 1 つだけである。
それが題名後半 `"Without Regards"` の処理である。

## 直すべき箇所 [ERROR]

### E-03-01 `"Without Regards"` を「気遣いなど無く」で処理すると軽すぎる

**EN:** `SCP-8980 — Ergophobia: Without Regards`
**行:** 799
**JP:** `SCP-8980 - 仕事恐怖症: 気遣いなど無く`

**要旨:** この副題は、単なる親切不足ではなく、相手を顧みないこと、そのまま勘定に入れないことを含む。現状訳は軽く、題名として締まらない。

**何がだめか:**

- `気遣い` だと日常的な親切不足に縮む
- `など` が入ることで広告文句のように軽く見える
- 作品全体に通底する「顧みられなさ」「制度的な無視」の重さが出ない

**修正の方向:**

- `顧慮`
- `顧みられず`
- `何一つ顧みられず`

## 補強したい箇所 [NOTE]

### N-03-01 内容警告の強度は公文書調で立てたい

**EN:** `"extremely sensitive material. Viewer discretion is heavily advised."`
**行:** 802
**JP:** `非常にセンシティブな内容が含まれていますので、閲覧には十分ご注意ください。`

**要旨:** 現状訳でも警告であることは伝わるが、ここは日常的な注意喚起ではなく、強い閲覧警告としてもう一段冷たく立てたい。

**何がだめか:**

- `センシティブ` と `十分ご注意ください` の組み合わせだと、記事冒頭の告知として少し軽い
- `heavily advised` の強い勧告が、やわらかいお願い文に寄る
- 直後の倫理委員会覚書へ接続する公文書トーンが弱まる

## 実務上の結論

- まず題名後半を差し替える
- そのうえで内容警告と覚書導入文を同じ温度へ揃える
- 入口文は「自然」より「読者にどういう作品かを正しく学習させること」を優先する

---

# SCP-8980 該当箇所 04 査読

**対象 EN:** `articles/fragment_scp-8980-1/segments/en/04_page_header_scp_data.wikidot`
**対象 JP:** `bad_translation_jp_single.wikidot`

## このファイルの使い方

- `[ERROR]` はそのまま修正対象
- `[NOTE]` は意味は通るが、制度文体や係り先を整えたい論点
- `[OUT-OF-SCOPE]` はこの箇所単体では処理しない論点

この箇所は SCP ファイルの顔であり、ここでの誤りは本文全体の読み方を早い段階で誤らせる。

## 総評

この箇所の最重要点は 3 つである。

- `"I like you." -> "I lick you."` の仕掛けを壊さないこと
- Description 段落を、日本語として読み通せる制度文に戻すこと
- 形式文書のトーンを保ったまま、細部の用語や係り先を整えること

ここで制度文と注釈の顔を崩すと、本文へ入る前から「何がどの方向に SCP-8980 を傷つける現象なのか」がずれる。

## 直すべき箇所 [ERROR]

### E-04-01 `"I like you." -> "I lick you."` を「いいね」→「死ね」にしない

**EN:** `"I like you." -> "I lick you."`
**行:** 936
**JP:** `「いいね」 -> 「死ね」`

**要旨:** これは本記事の中心にある「一字違いで性的に不適切化する」仕掛けである。敵意方向へ変えると主題ごとずれる。

**何がだめか:**

- 好意から殺意へ飛んでしまう
- 性的嫌がらせの方向が消える
- 原文の一字差の見え方も再現できていない

**修正の方向:**

- 原文保持 + 注釈
- どうしても日本語化するなら、性的な不適切化の方向を守る

### E-04-02 Description の列挙が日本語として破綻している

**EN:** `"socially, financially, psychologically, etc."`
**行:** 933
**JP:** `社会的、経済的、心理的になど`

**要旨:** ここは制度文として一度で読める形に直す必要がある。

**何がだめか:**

- 助詞列が破綻している
- 悪影響の範囲が列挙として読めない

## 補強したい箇所 [NOTE]

### N-04-01 `"dietary needs"` 周辺は医療要件と時制を整理したい

**EN:** `"does not require any dietary needs"` / `"medical records do not indicate as such as of 2003"`
**行:** 914 / 914
**JP:** `如何なる食事上の配慮も要求していません` / `2003年時点のSCP-8980の医療記録にはそのような記載は存在しません`

**要旨:** このままでも大意は通るが、ここは「何を必要としていないか」と「2003年時点で何が記録にないか」を切り分けた方が、注釈の制度文として読みやすい。

**直すなら:**

- `dietary needs` を日常の食事ではなく医療上の食事要件として置く
- `as of 2003` を医療記録側へ素直に掛ける

### N-04-02 `"former duties"` と `"still anomalous"` の係り先を整えたい

**EN:** `"former duties"` / `"ensure it is still anomalous"`
**行:** 923 / 923
**JP:** `元の地位と職務に復帰するものとします` / `異常性が残存していることを確認するため`

**要旨:** 読めないわけではないが、`former` がどこに掛かるかと、年次検査の目的が少しもつれる。ここは本文と注釈のズレが一読で分かる形へ整理したい。

**直すなら:**

- 「元」は職務ではなく誤情報ラベル側で受ける
- 年次検査は「まだ異常か」の確認であると素直に書く

### N-04-03 `"obsolete"` を「廃止」と断言しすぎない

**EN:** `"Caucasian" is an obsolete classification`
**行:** 931
**JP:** `「コーカソイド」という単語の使用は廃止されました`

**要旨:** 禁じたい方向自体は伝わるが、`obsolete` は「正式に廃止された」と言い切るより、「もう古く、現行では不適切」と言う方が注釈の温度に合う。

### N-04-04 `"first became anomalous"` を「最初に異常性を獲得した」に寄せすぎない

**EN:** `first became anomalous`
**行:** 946
**JP:** `最初に異常性を獲得した`

**要旨:** ここは「異常性が発覚した」のであって、「本人が異常を獲得した」と言い切る箇所ではない。日本語で強く言い直すと、発見時点の曖昧さが消える。

**何がだめか:**

- 原文は異常化の断定を避けている
- `became` を「獲得した」と置くと、本人が能動的に得たように響く
- `Discovery` 段落の慎重さが薄れる

**修正の方向:**

- `最初に異常性が確認された`
- `最初に異常性が発覚した`

### N-04-05 `"a prominent member of Junior Staff"` は `a` と所属感を残したい

**EN:** `a prominent member of Junior Staff`
**行:** 929
**JP:** `ジュニアスタッフの代表的なメンバー`

**要旨:** このままでも意味は通るが、`a` が示す「同じ集団の中の一員」という感触がやや薄い。`代表的な` だけだと、集団の中の一人というより代表者のように見えやすい。

### N-04-06 `"is subject to ongoing research"` は状態として置きたい

**EN:** `is subject to ongoing research`
**行:** 942
**JP:** `現在調査が進められています`

**要旨:** 言いたいことは合っているが、`subject to` は「研究の対象になっている」という状態述語である。日本語でも、単に「調査中」ではなく、対象として置かれている感じを残したい。

## このファイルでは採らない論点 [OUT-OF-SCOPE]

### O-04-01 代名詞方針はこの箇所だけで決めない

**要旨:** `it / its / itself` の訳し分けは、少なくとも該当箇所 15 以降を含む記事全体の呼称設計として扱うべきである。
このファイル単体の修正指示には残さない。

## 実務上の結論

- まず `"like" / "lick"` の仕掛けを壊さない形へ戻す
- Description 段落の日本語破綻を直す
- NOTE 論点は本文全体を大きく動かさず、制度文体の精度を上げる方向で使う

---

# SCP-8980 該当箇所 05 査読

**対象 EN:** `articles/fragment_scp-8980-1/segments/en/05_addendum1_initial_interview.wikidot`
**対象 JP:** `bad_translation_jp_single.wikidot`

## このファイルの使い方

この箇所は、SCP-8980 とバーンズの声の基準線を決める。
したがって、単語対応だけでなく、誰がどんな距離で話しているかを必ず残す。

- `[ERROR]` はそのまま修正対象
- `[NOTE]` は補強候補として弱めて残す

## 総評

現行訳は大意は追えているが、初期バーンズの「丁寧な外面」と、SCP-8980 の「知的な怒り」がかなり平らになっている。
加えて、日付ミスが 1 行目から入っており、これは単純だが重い。

ここでバーンズを最初から露骨に雑な人間へ寄せると、後半で仮面が剥がれる落差を先に食ってしまう。

## 直すべき箇所 [ERROR]

### E-05-01 日付 `March 10th, 2005` を取り違えない

**EN:** `DATE: March 10th, 2005`
**行:** 959
**JP:** `日付: 2005年5月10日`

**修正:** `2005年3月10日` に戻す。

**要旨:** これは単純な誤訳だが、後続の時系列と一周年対応を壊す。

### E-05-02 `"my heuristic"` の所有格を落とさない

**EN:** `"my heuristic for {calculating Ackermann function values for m over 50}"`
**行:** 1009
**JP:** `発見的手法に関するプレゼンテーションの最中でした。`

**要旨:** ここは SCP-8980 自身の研究成果であり、所有格を落とすと後続の研究盗用の伏線が弱まる。

### E-05-03 `"inane procedures"` と `"for someone such as you"` の裏表を潰さない

**EN:** `"being forced to undergo these inane procedures must be quite troublesome for someone such as you."`
**行:** 981
**JP:** `このような何の足しにもならないような手順を踏まねばならないということは、あなたのような人にはさぞ迷惑のかかることでしょうから。`

**要旨:** ここは表向きの敬意と、その下にある軽蔑が同時に出ていなければならない。

### E-05-04 `"Wonderful."` を権威的にしない

**EN:** `"Wonderful."`
**行:** 1058
**JP:** `宜しい。`

**要旨:** ここは軽い事務的承認であって、「うむ、許す」の語感ではない。

### E-05-05 `"That"` の指示対象をずらさない

**EN:** `"That would at least be appreciated."`
**行:** 1052
**JP:** `あなたのことは恩に着られますね`

**要旨:** 感謝しているのはバーンズ個人ではなく、読み物を持ち込む提案そのものである。

**修正の方向:**

- 提案自体を指す文に戻す
- バーンズ個人への恩義へずらさない

### E-05-06 `"Yes, that should be sufficient."` を「はいはい」にしない

**EN:** `"Yes, that should be sufficient."`
**行:** 1023
**JP:** `はいはい`

**要旨:** 初期バーンズはまだ丁寧な仮面を維持している。ここで露骨な雑さを先取りしない。

## 補強したい箇所 [NOTE]

### N-05-01 `Lillian—` のダッシュは中断として残したい

**EN:** `Lillian—`
**行:** 975
**JP:** `リリアン?`

**要旨:** このままでも内容は追えるが、疑問符だと呼びかけの語尾に聞こえる。ここは遮られた中断の方が、バーンズの馴れ馴れしさと直後の訂正要求を自然につなげる。

### N-05-02 `"tilts its head upwards"` の動きはもう少し具体化できる

**EN:** `"tilts its head upwards"`
**行:** 1042
**JP:** `頭を上に向ける`

**要旨:** 今の訳でも概意は取れるが、ただ上を見るより、後ろにもたれた姿勢のまま天井を仰ぐ動きとして出した方が、閉じ込められた窮屈さと倦みが見えやすい。

### N-05-03 `"circumstances in which"` は「時の状況」より「経緯」に寄せたい

**EN:** `Next, please describe the circumstances in which you discovered your anomalous properties.`
**行:** 997
**JP:** `では次に、自身の異常性に気付いた時の状況について説明してください。`

**要旨:** ここは単なる発見の瞬間ではなく、どういう場面で、どういう経緯で異常性が見つかったかを聞いている。`時の状況` だけだと、条件や背景が細くなる。

### N-05-04 `sympathetically` と `audible yawn` はバーンズの作り物の親切を残したい

**EN:** `Dr. Byrnes smiles sympathetically, then stretches, letting out an audible yawn.`
**行:** 1046
**JP:** `悼ましそうに笑みを浮かべ、それから伸びをして、音を出してあくびをする。`

**要旨:** ここは本当に親切な笑顔ではなく、親切に見せる笑顔である。さらに `audible yawn` は、聞こえるあくびとして残さないと、バーンズの気の抜けた支配が弱まる。

### N-05-05 `both blood samples and physical examination` は両方を明示したい

**EN:** `SCP-8980 anomalous property testing will proceed using both blood samples and physical examination.`
**行:** 1068
**JP:** `SCP-8980の異常性の検査は血液サンプルの使用と身体検査を併せて実施する予定です。`

**要旨:** `併せて` でも意味は通るが、`both` は「血液サンプルと身体検査の両方」をわざわざ立てる語である。片方を主、片方を従にしない方がよい。

## 実務上の結論

- この箇所ではまず時系列と声の基準線を直す
- バーンズは最初から露骨に粗暴にしない
- SCP-8980 の研究者としての主体性を、所有格や言い回しで落とさない

---

# SCP-8980 該当箇所 06 査読

**対象 EN:** `articles/fragment_scp-8980-1/segments/en/06_addendum2_test_results.wikidot`
**対象 JP:** `bad_translation_jp_single.wikidot`

## このファイルの使い方

この箇所では、バーンズの丁寧さが配慮ではなく圧力として働いているかを確認する。
元の 2 件を核にしつつ、周辺の圧力表現もいくつか補強している。

## 総評

この箇所の芯は、SCP-8980 の疲弊と、バーンズのもっともらしい慰撫が正面衝突することにある。
現行訳は大意こそ追えているが、検査で絞られる身体感覚と、翌日も検査に入れられる嫌さが弱い。

## 直すべき箇所 [ERROR]

### E-06-01 `"being put through the wringer"` が「散々苦労」に平坦化している

**EN:** `"being put through the wringer"`
**行:** 1121
**JP:** `散々苦労してきた`

**要旨:** ここは単に大変だったではなく、検査で絞られ消耗しきっていることを出す必要がある。

**何がだめか:**

- 慣用句の身体性が落ちる
- `blood drawn` と並ぶことで出る消耗感が弱まる
- SCP-8980 の怒りが「愚痴」寄りに見えてしまう

**修正の方向:**

- `絞り尽くされた`
- `しごかれた`
- `くたくたになった`

### E-06-06 `"get your testing set up by tomorrow"` が受け手側の不利益をぼかしている

**EN:** `"I'll be sure to get your testing set up by tomorrow."`
**行:** 1211
**JP:** `明日までには検査の手はずを整えておきますね。`

**要旨:** ここは段取りの説明ではなく、「明日にはまた検査に入れる」という通知である。

**何がだめか:**

- `手はずを整える` では準備側の事務作業に寄る
- SCP-8980 が翌日からまた検査にかけられることが軽くなる
- バーンズの丁寧な支配の滑りがよくなりすぎる

**修正の方向:**

- `明日には検査に入れるよう手配する`
- `次の検査を始められるようにしておく`

### E-06-07 `"Just consider this a... an extended vacation, alright?"` を段取り説明にしない

**EN:** `"Just consider this a... an extended vacation, alright?"`
**行:** 1195
**JP:** `長期休暇の類であると思ってください。いいですね？`

**要旨:** これは中立な予定説明ではなく、次の検査を「休暇」と呼んで丸めた支配の言い方である。`alright?` も確認ではなく、やわらかい圧として残したい。

**何がだめか:**

- `extended vacation` の皮肉が弱まる
- 検査を受ける不利益がぼける
- `alright?` の押しつけが消える

**修正の方向:**

- `しばらくの長期休暇`
- `とでも思っておいてください`

## 補強したい箇所 [NOTE]

### N-06-01 `visibly agitated` は観察記録として残したい

**EN:** `SCP-8980 is seated, though visibly agitated; it repeatedly taps its leg and huffs for an extended period.`
**行:** 1103
**JP:** `SCP-8980は着席していたが明らかに動揺しており、長時間にわたって足を繰り返し叩き、息を荒くしている。`

**要旨:** ここは「動揺している」だけでは足りず、外から見て分かる動揺であることが大事である。`repeatedly` と `for an extended period` も、観察記録の粘りとして残したい。

### N-06-02 `it seems like` は診断のクッションとして機能している

**EN:** `Well... it seems like the anomaly is trying to humiliate you.`
**行:** 1155
**JP:** `ええ、どうやら件の異常現象はあなたの自尊心を傷つけようと試みているみたいなんです。`

**要旨:** `it seems like` は断定を避けるクッションであり、`humiliate` は単なる「傷つける」ではない。ここは、バーンズが丁寧に見せかけて決めつけている嫌さを残したい。

### N-06-03 `no disciplinary action will be taken at this time` は決定の温度を落とさない

**EN:** `While the incident in question was found to be a violation of the Foundation Citation Policy, no disciplinary action will be taken at this time.`
**行:** 1203
**JP:** `この件は財団の引用規定に違反していると判断されましたが、現時点では懲戒処分は行われません。`

**要旨:** ここは「現時点では」が核であり、単なる説明ではなく委員会の決定である。`will be taken` の決定性を、ぼかしすぎないようにしたい。

### N-06-04 `Great! I always appreciate it when a meeting goes smoothly.` は満足の押しつけになっている

**EN:** `Great! I always appreciate it when a meeting goes smoothly.`
**行:** 1211
**JP:** `良いね！話がスムーズに進むといつも嬉しくなるね。`

**要旨:** `Great!` は単なる相づちではなく、手続きがうまく進んだことへの満足である。`いつも嬉しくなる` だけだと、圧のある達成感が少し弱い。

### N-06-05 `on time, next time!` は軽い冗談ではなく釘刺し

**EN:** `Alright, I'll see you bright and early tomorrow — on time, next time!`
**行:** 1215
**JP:** `わかりました。じゃあ、明日の朝早くに会いましょう。今度は時間通りに行きますよ！`

**要旨:** ここは親しげな締めではなく、遅刻を釘刺しする台詞である。`on time, next time!` の嫌味を落とすと、最後の一刺しがなくなる。

## 実務上の結論

- 消耗の慣用句は身体感覚を戻す
- バーンズの診断、拘束告知、締めの釘刺しは、どれも丁寧な顔をした圧として訳す
- 現時点では 2 件に加えて、観察描写と終端の圧力表現を補強済み

---

# SCP-8980 該当箇所 07 査読

**対象 EN:** `articles/fragment_scp-8980-1/segments/en/07_addendum3_experimentation.wikidot`
**対象 JP:** `bad_translation_jp_single.wikidot`

## このファイルの使い方

この箇所のバーンズは、「悪い知らせを丁寧に伝える人」の顔で、実際には財団側の利害を押しつけてくる。
ここでの誤りはすべてそのまま採る。

## 総評

重要なのは、SCP-8980 がどう分類され、誰のために収容が続き、バーンズがどんな内輪理屈でそれを正当化しているかである。
現行訳は意味を拾っている箇所もあるが、暫定診断、反語、財団側の利害、身内論理の 4 点が弱い。

## 直すべき箇所 [ERROR]

### E-07-01 `"Like hell it isn't!"` の強い肯定を外してはいけない

**EN:** `"Like hell it isn't!"`
**行:** 1351
**JP:** `そんなわけがないじゃないですか！`

**要旨:** ここは否定の否定ではなく、直前の発言を真っ向からひっくり返す強い肯定である。

**何がだめか:**

- `like hell` の強い反発が消える
- `it isn't` をそのまま否定として処理すると、バーンズの発言を受けた切迫感が落ちる
- 何に対する反論かが、日本語だけでは見えにくい

### E-07-02 仮の見立てが説明文に崩れている

**EN:** `"it seems like you're a unique Pattern-Based anomaly"`
**行:** 1331
**JP:** `パターンに基づいた特異なアノマリーということなのでしょう`

**要旨:** ここは確定診断ではなく、もっともらしく押しつけられる暫定分類である。

**何がだめか:**

- `"it seems like"` の仮置きが薄い
- 分類ラベルとしての押しつけが弱い
- バーンズの専門家ぶった見立てに見えにくい

### E-07-03 反語の詰問が普通の質問に寄っている

**EN:** `"How in the world am I supposed to be calm about this?"`
**行:** 1345
**JP:** `一体どうすれば冷静でいられるというんですか？`

**要旨:** 現状訳でも大筋は近いが、方法質問ではなく、命令そのものを突き返す詰問として立てたい。

**修正の方向:**

- `これでどうやって冷静でいろっていうんですか`
- `冷静でいられるわけがない`

### E-07-04 `"for us"` が落ちている

**EN:** `"the best thing you can do for us"`
**行:** 1365
**JP:** `今のあなたにとっての最善策`

**要旨:** ここは本人利益ではなく、財団側の利益を正面から言っている。

**何がだめか:**

- バーンズと財団の利害が隠れる
- 収容継続が医療的助言のように見える
- 本記事の制度的な冷たさが薄まる

### E-07-05 `"one of our own"` の身内論理が崩れている

**EN:** `"what shouldn't we do for one of our own?"`
**行:** 1403
**JP:** `仲間を助けるためには何をしないことがあるのでしょうか？`

**要旨:** ここは身内だから何をしてもよい、という内輪の加害理屈である。現行訳は日本語としても立っていない。

**修正の方向:**

- `身内の一人のためなら、何だってする`
- `うちの仲間なんだから、やらない理由はない`

### E-07-06 `"This isn't the end of the world or anything."` の雑な逃げを消さない

**EN:** `"This isn't the end of the world or anything."`
**行:** 1349
**JP:** `こんなのは世界の終わりとかそういうことじゃないん?`

**要旨:** `or anything` は「大したことじゃない」の崩しであり、ただの否定ではない。

**何がだめか:**

- 相手の不安を軽くいなす雑さが弱まる
- `world` と `anything` の落差が消える
- 直前の強い反発を受け止めるバーンズの小馬鹿にした口ぶりが立たない

## 実務上の結論

- バーンズの利害は必ず「私たち」の側で訳す
- SCP-8980 の反発は反語の強さを残す
- afterword の内輪理屈は、きれいな善意へ言い換えない

---

# SCP-8980 該当箇所 08 査読

**対象 EN:** `articles/fragment_scp-8980-1/segments/en/08_addendum4_secondary_exp.wikidot`
**対象 JP:** `bad_translation_jp_single.wikidot`

## このファイルの使い方

この箇所では、バーンズの雑な言い逃れと、不自然な比喩の直訳を見逃さない。
今回は 2 件ともそのまま修正対象である。

## 総評

地味なセグメントだが、後半で本格化する「やわらかい言葉で包む支配」の前振りになっている。
ここで雑さと不快さをきれいな論文語に整えると、バーンズの嫌さがかなり薄まる。

## 直すべき箇所 [ERROR]

### E-08-01 `"or something of the sort"` の雑な逃げが消えている

**EN:** `"or something of the sort"`
**行:** 1441
**JP:** `あるいはそれに類する`

**要旨:** ここは雑な言い逃れなので、整った論文語にしてはいけない。

**何がだめか:**

- バーンズの説明放棄が見えなくなる
- 倫理委員会コメントが問題にしている雑さが日本語で消える

### E-08-02 `"laser-targeted"` を文字通りのレーザーへ読んでいる

**EN:** `"laser-targeted"`
**行:** 1457
**JP:** `レーザー銃のように狙いを定めている`

**要旨:** これは具体物ではなく、異様なまでに狙い撃ちであることの比喩である。

**何がだめか:**

- 日本語で急に漫画的になる
- 嫌さより先に比喩のぎこちなさが立つ
- バーンズの擬人化の調子が崩れる

## 補強したい箇所 [NOTE]

### N-08-01 `"I look forward to having it back with us"` の同僚性は残す

**EN:** `"I look forward to having it back with us"`
**行:** 1477
**JP:** `SCP-8980が我々の元に帰還するのを私は楽しみにしています。`

**要旨:** 訳は大きく外れていないが、`with us` にある「こちら側の一員として戻ってくる」含みを残しておきたい。

**修正の方向:**

- `我々のもとに戻る` だけで終わらせず、`我々と一緒に` の距離感を保つ
- 戻ってくる事実だけでなく、バーンズの帰属意識も見せる

### N-08-02 `"Following several days..."` の移行期間を丸めない

**EN:** `"Following several days standardizing SCP-8980's containment arrangement, SCP-8980 began to resume active employment at the SCP Foundation on April 18th, 2005, with special considerations for its anomalous capabilities."`
**行:** 1481
**JP:** `SCP-8980の収容体制標準化に数日を要した後、異常な能力に対して特別な配慮がなされたうえで、SCP-8980は2005年4月18日付でSCP財団での仕事を再開しました。`

**要旨:** `Following` の時系列と `began to resume` の立ち上がりを、単なる「後」と「再開した」で丸めない。

**修正の方向:**

- `数日を経て` のように、調整期間を前景化する
- `再開した` だけでなく、段階的な再開を残す

### N-08-03 `"incorrect options being selected"` と `"requested to conclude the experiment"` は、起動失敗と申告の両方を残す

**EN:** `"high input latency, incorrect options being selected (such as language), and the device randomly restarting. While SCP-8980 was able to eventually set up the device, it was cited as being uncomfortable and requested to conclude the experiment."`
**行:** 1421
**JP:** `入力遅延の増加、言語設定の際などの誤ったオプションの選択、デバイスのランダムな再起動などに見舞われ、オペレーティングシステムの設定に著しい困難をきたした。SCP-8980は最終的にデバイスの設定を完了できたが、不快感を訴えたため実験の終了を要求した。`

**要旨:** 起動に手間取った事実だけでなく、本人が不快感を訴えて終了を求めた流れまで残しておきたい。

**修正の方向:**

- `incorrect options` は、単なる不具合ではなく選択の誤りとして読む
- `requested to conclude` は、SCP-8980 の主体的な終了要求として残す

### N-08-04 `"electronic equipment"` は訳語を揃える

**EN:** `"with no prior interaction with other electronic equipment"` / `"due to its potential risk to nearby electronic equipment"`
**行:** 1419 / 1481
**JP:** `他の電子機器との事前の接触がない` / `近隣の電子機器に潜在的なリスクがあるため`

**要旨:** `電子機器` と `電子デバイス` の揺れを止めて、同じ語を同じ語で返したい。

**修正の方向:**

- 08 内で `electronic equipment` を `電子機器` に寄せる
- 似た文脈で `電子デバイス` に逃がさない

## 実務上の結論

- `with us` がある箇所は、単なる帰還ではなく所属感まで読む
- 収容体制の標準化は、再開の前段階として訳す
- `began to resume` の立ち上がりは落とさない

---

# SCP-8980 該当箇所 09 査読

**対象 EN:** `articles/fragment_scp-8980-1/segments/en/09_addendum5_post_reemployment.wikidot`
**対象 JP:** `bad_translation_jp_single.wikidot`

## このファイルの使い方

この箇所では、SCP-8980 がバーンズの管轄を抜けようとする方向が見えているかを最優先で確認する。
今回は 3 件ともそのまま採る。

## 総評

ここは単なる口論ではない。
SCP-8980 が初めて制度の抜け道を探し、バーンズを飛ばして別経路へ進もうとする場面である。
したがって、制度名、迂回、案件移管の 3 つが崩れると、この箇所全体の方向が変わる。

## 直すべき箇所 [ERROR]

### E-09-01 引用符つき制度名が制度語として立っていない

**EN:** `"continued employment despite anomalous interference"`
**行:** 1527
**JP:** `異常影響の保有に関わらない雇用継続`

**要旨:** これはSCP-8980が皮肉を込めて言い直す制度名であり、構文も意味も崩してはいけない。

**何がだめか:**

- `interference` が `保有` に化けている
- 制度名として読めない
- SCP-8980 が自分を縛る仕組みを苦々しく呼ぶ感じが消える

### E-09-02 `"go around you"` が先回りの意味にずれている

**EN:** `"I'll just go around you."`
**行:** 1593
**JP:** `私は一足先に行くつもりです。`

**要旨:** ここはバーンズを飛ばして別の窓口へ行く宣言である。

**何がだめか:**

- 競争で先回りする意味に読める
- 直後の申立てや RFR と接続しない

### E-09-03 `"get my case off your hands"` が退去要求に化けている

**EN:** `"get my case off your hands"`
**行:** 1593
**JP:** `この件についてお引き取りいただければ`

**要旨:** ここは案件移管の要求であって、相手に帰れと言っているのではない。

**何がだめか:**

- `case` の制度語が落ちる
- 担当替えを求める文として読めない

## 補強したい箇所 [NOTE]

### N-09-01 `"quickly achieved similar efficiency"` の回復感を残す

**EN:** `"For the first few days following SCP-8980's accommodations being standardized, SCP-8980 showed signs of struggling, however quickly achieved similar efficiency within a week of acclimation, despite the limitations."`
**行:** 1487
**JP:** `SCP-8980の収容環境が標準化された後、最初の数日間はSCP-8980は苦労している様子を見せていましたが、制約の存在に関わらず順応後1週間以内に__当初の__効率性を速やかに達成しました。`

**要旨:** 内容は通るが、`quickly achieved` の「急速に元の水準へ戻った」感じを残したい。

**修正の方向:**

- `順応から1週間も経たないうちに` として、回復の速度を見せる
- `similar efficiency` は `同程度の効率` で止めず、元の水準への復帰を匂わせる

### N-09-02 `"The Foundation often does things to people that they don't agree with."` の制度性を落とさない

**EN:** `"The Foundation often does things to people that they don't agree with."`
**行:** 1559
**JP:** `財団というのはしばしば人々にとって同意できないような真似をする。`

**要旨:** `often` と `don't agree with` が、財団の慣常的な加害を指していることを明示しておきたい。

**修正の方向:**

- `しばしば` を軽く流さず、制度として繰り返される冷たさとして読む
- `同意できない` だけでなく、押しつけの常態を出す

### N-09-03 `"You barely talked to us outside of work."` の薄さを残す

**EN:** `"You barely talked to us outside of work."`
**行:** 1535
**JP:** `仕事以外ではほとんど我々と話をしませんでしたよね。`

**要旨:** `barely` は単なる「ほとんど」より、関係の薄さを突きつける語である。

**修正の方向:**

- `ろくに` を使って、接触の少なさを刺す
- 仕事外の距離感を、ただの事実ではなく不満として出す

### N-09-04 `"motions around wildly"` の制御喪失を落とさない

**EN:** `"SCP-8980 motions around wildly."`
**行:** 1545
**JP:** `SCP-8980は激しく動き回る。`

**要旨:** `wildly` は単なる強さではなく、制御を失った取り乱し方を示している。

**修正の方向:**

- `激しく` で止めず、`取り乱して` `無我夢中で` のように様子を出す
- 動きの大きさより、感情の崩れを前景化する

## 実務上の結論

- 再雇用後の回復は、速度と限定性の両方を残す
- 財団の常態的な加害は、軽い一般論に落とさない
- `barely` は人間関係の薄さまで含めて訳す

---

# SCP-8980 該当箇所 10 査読

**対象 EN:** `articles/fragment_scp-8980-1/segments/en/10_form2093a_first_filing.wikidot`
**対象 JP:** `bad_translation_jp_single.wikidot`

## このファイルの使い方

このフォームは、SCP-8980 側の訴えとバーンズ側の自己弁明が一つの制度書式の中でぶつかる場である。
したがって、文章を読みやすく整えるより、バーンズの自己正当化の気味悪さを消さないことを優先する。

今回は 2 件ともそのまま採る。

## 総評

危険なのは次の 2 点である。

- バーンズの自己中心的な言い直しが、良心的な補足へ整えられている
- 接触制限と暫定収容延長を正当化する一文が丸ごと欠けている

この二つが残ると、フォーム全体が「少しまずい人の釈明」ではなく、「そこそこ良心的な説明文」に見えてしまう。

## 直すべき箇所 [ERROR]

### E-10-01 `"for all of us — it especially —"` の鈍さを消してはいけない

**EN:** `"painful for all of us — it especially —"`
**行:** 1764
**JP:** `私たち全員、特にSCP-8980自身にとって辛い`

**要旨:** ここはバーンズがまず自分たちを先に置き、あとから本人を足している。その鈍さが重要である。

**何がだめか:**

- 現状訳だと最初から被害者を適切に勘定しているように見える
- 原文の「思い出したように本人を足す」嫌さが消える

### E-10-02 接触制限と暫定収容延長の一文が欠けている

**EN:** `"For this reason, we've had to take extra precaution regarding who SCP-8980 interacts with, both for its safety and for ours. This is also why its provisional containment has been extended."`
**行:** 1766
**JP:** 当該一文が欠落

**要旨:** これは言い回しの問題ではなく、自己弁明の核心が一文ごと落ちている。

**何がだめか:**

- 接触制限を本人のためでもあると言い張る偽善が見えない
- 暫定収容延長の説明責任が消える
- バーンズの文が「危ないかもしれない」で止まり、行動の正当化まで届かない

## 補強したい箇所 [NOTE]

### N-10-01 `"As a former non-anomalous member of Foundation staff..."` は申立人の資格根拠である

**EN:** `"As a former non-anomalous member of Foundation staff who has worked closely with containment specialists in the past, I am of the opinion I am being deprived of certain rights and subject to improper containment, including (but not limited to):"`
**行:** 1698
**JP:** `私は、現在担当中の収容スタッフによる私の収容対応に対して非常に不満を抱いています。過去に収容スペシャリストと密接に協力してきた財団の元非異常職員として、私は特定の権利を?奪され、不適切な収容を受けていると考えられます。`

**要旨:** `former non-anomalous member` を単なる肩書きで終わらせず、申立ての資格を支える立場表明として読ませたい。

**修正の方向:**

- `元非異常職員` の部分を、現在の立場との対比として立てる
- `過去に〜してきた` の累積を、申立ての根拠として見せる

## 実務上の結論

- 申立書では、発言者の立場そのものを資格根拠として残す
- `former` は単なる経歴ではなく、現在の主張の足場として訳す
- 本人の不満は、制度上の権利侵害として読める形にする

---

# SCP-8980 該当箇所 11 査読

**対象 EN:** `articles/fragment_scp-8980-1/segments/en/11_form2093a_rewritten_response.wikidot`
**対象 JP:** `bad_translation_jp_single.wikidot`

## このファイルの使い方

該当箇所 10 と同じく、ここは制度文体の冷たさを守る場である。
単に硬い日本語ではなく、「何を認め、何を拒み、どこで責任を限定しているか」が読める文にする。

今回は 3 件ともそのまま採る。

## 総評

危険なのは次の 3 点である。

- 該当箇所 10 と同じ欠落が再掲版でも放置されている
- 長い法務文の論理が日本語でほどけていない
- 最後の警告文が、制度警告ではなく日常的な注意書きに落ちている

## 直すべき箇所 [ERROR]

### E-11-01 接触制限と暫定収容延長の一文をここでも落としてはいけない

**EN:** `"both for its safety and for ours"` / `"This is also why its provisional containment has been extended."`
**行:** 1936 / 
**JP:** `これは、アノマリーの安全と我々の安全の両方を守るためであり、また、暫定的な収容期間が延長された理由でもあります。`

**要旨:** 該当箇所 10 と同じ欠落を、改稿版でも繰り返してはならない。

**修正の方向:**

- 該当箇所 10 と同じ文を戻す
- 両版の論理を揃える

### E-11-02 `"either normalcy or monetary/personnel resources"` の切り分けをほどく

**EN:** `"either normalcy or monetary/personnel resources of the SCP Foundation"`
**行:** 1975
**JP:** `正常性または金銭的・人的資源に重大な、または極めて高い確率で損害を与える`

**要旨:** 現状訳は、何にどの種の損害が及ぶのかが読みづらい。

**何がだめか:**

- `either A or B` の切り分けが曖昧
- `重大` と `極めて高い確率` の係り先が見えにくい
- 法務文書としての冷たさではなく、ただの読みにくさになっている

### E-11-04 最後の警告は「自己責任」では弱すぎる

**EN:** `"Reviewer discretion is heavily advised. Proceed at your own risk."`
**行:** 2016
**JP:** `審査は各自の判断で行ってください。自己責任で進んでください。`

**要旨:** ここはネット上の断り書きではなく、倫理委員会文書としての強い閲覧警告である。

**何がだめか:**

- `自己責任` が日常語に見える
- 制度文書としての重さが足りない

## 補強したい箇所 [NOTE]

### N-11-01 `"I suppose you could say that I'm a changed man now."` の婉曲を残す

**EN:** `"Yes, well, I suppose you could say that I'm a changed man now."`
**行:** 2058
**JP:** `ああ、そうですね。私は今や生まれ変わったと言えるでしょう。`

**要旨:** `I suppose you could say` の婉曲さを消さず、自己弁明の照れ隠しを残したい。

**修正の方向:**

- `まあ、そう言えるかもしれません` のように、断定しすぎない
- 自己改革の宣言ではなく、言い逃れに近い調子を保つ

### N-11-02 `"As a former non-anomalous member of Foundation staff..."` をここでも落とさない

**EN:** `"As a former non-anomalous member of Foundation staff who has worked closely with containment specialists in the past, I am of the opinion I am being deprived of certain rights and subject to improper containment, including (but not limited to):"`
**行:** 1868
**JP:** `私は、現在担当中の収容スタッフによる私の収容対応に対して非常に不満を抱いています。過去に収容スペシャリストと密接に協力してきた財団の元非異常職員として、私は特定の権利を?奪され、不適切な収容を受けていると考えられます。`

**要旨:** 10 と同じく、`former` は申立ての資格を支える立場表明である。

**修正の方向:**

- 申立書の資格根拠として、かつての職歴を明示する
- `元非異常職員` を単なる説明で終わらせず、主張の足場として見せる

## 実務上の結論

- 改稿版でも、申立人の立場表明を落とさない
- 婉曲な自己弁明は、断定に潰さず残す
- 収容に対する不満は、制度文の硬さの中で立てる

---

# SCP-8980 該当箇所 12 査読

**対象 EN:** `articles/fragment_scp-8980-1/segments/en/12_addendum6_containment_plan.wikidot`
**対象 JP:** `bad_translation_jp_single.wikidot`

## このファイルの使い方

この箇所では、バーンズが規範に従うふりをしながら、同じ方向へ SCP-8980 を押し戻しているかを見抜く。
今回の 5 件はすべてそのまま採る。

## 総評

要点は、やわらかい語ほど疑って読むことにある。
`amenable` `save you trouble` `Okay?` `two cents` `comfortable` は、どれも親切そうに見えて支配の滑りをよくしている。

## 直すべき箇所 [ERROR]

### E-12-01 `"amenable"` を「働きやすい」にすると善意化しすぎる

**EN:** `"some more amenable conditions"`
**行:** 2092
**JP:** `より働きやすい環境`

**要旨:** ここは職場改善ではなく、もう少し従わせやすい条件を探る話である。

### E-12-02 `"save you trouble"` は親切ではなく会話の遮断

**EN:** `"Let me save you trouble Chris."`
**行:** 2120
**JP:** `あなたの手間を省いてあげましょう。`

**要旨:** ここは「どうせそう言うつもりでしょうから、先に言います」という遮断である。

### E-12-03 最後の `"Okay?"` は確認強制である

**EN:** `"I am fine. I am fine. Okay?"`
**行:** 2120
**JP:** `大丈夫でしょうか？`

**要旨:** これは自分の状態を尋ねる文ではない。会話を閉じるための圧である。

### E-12-04 `"if you want my two cents"` は軽口混じりの差し出口

**EN:** `"if you want my two cents"`
**行:** 2132
**JP:** `個人的な意見としては`

**要旨:** 丁寧な私見ではなく、頼まれてもいない口出しとして訳すべきである。

### E-12-05 `"comfortable with its new role"` を美化しない

**EN:** `"as comfortable as possible with its new role"`
**行:** 2144
**JP:** `新たな役割にできるだけ快く順応`

**要旨:** ここは役割受容をやわらかく包む嫌な言い方であって、前向きな適応ではない。

## 補強したい箇所 [NOTE]

### N-12-01 `"Never thought I'd see you act so professional — you didn't even stutter!"` の嘲りを分ける

**EN:** `"Wow, they must've given you quite the beating, Byrnes! Never thought I'd see you act so professional — you didn't even stutter!"`
**行:** 2054
**JP:** `おお、バーンズ、相当ひどい目に遭ったんですね！あなたがこんなにもプロらしく振舞ってくれるとは思いもよりませんでしたよ。どもりもしなかったではありませんか！`

**要旨:** 驚きと嘲笑の二段があるので、`Never thought` の軽さと `you didn't even stutter` の皮肉を別々に立てたい。

**修正の方向:**

- `思いもよりませんでした` を、やや軽い驚きとして残す
- `どもりもしなかった` は、バーンズをからかう刺さり方を保つ

### N-12-02 `"I highly recommend"` の強さを落とさない

**EN:** `"I highly recommend that you don't file it, though, if you want my two cents."`
**行:** 2132
**JP:** `ただ、個人的な意見としては、提出しないことを//強く//推奨します。`

**要旨:** `highly` は強い押しつけで、`if you want my two cents` の軽口と組み合わさることで、丁寧さより介入の強さが立つ。

**修正の方向:**

- `余計なお世話を承知で` のように、口出しの感じを出す
- `強く` を落とさず、推奨の強圧感を残す

## 実務上の結論

- 嘲りと親切ぶりは、同じ日本語に潰さない
- `highly` は単なる強調ではなく、介入の圧として訳す
- `Never thought` の軽い驚きを、礼儀正しさに変えすぎない

---

# SCP-8980 該当箇所 13 査読

**対象 EN:** `articles/fragment_scp-8980-1/segments/en/13_addendum7_tertiary_exp.wikidot`
**対象 JP:** `bad_translation_jp_single.wikidot`

## このファイルの使い方

この箇所では、崩壊と制度的正当化が切れ目なく続く流れを保てているかを確認する。
今回の指摘はすべてそのまま修正対象として扱う。

## 総評

重要なのは、実験コメントの硬さ、崩壊の身体描写、バーンズの押し切り、乱闘、そして制度語までを一続きで保つことである。
現行訳は大意は通るが、場面ごとの圧力がところどころ切れている。

## 直すべき箇所 [ERROR]

### E-13-01 `"If we are to find some alternative system, we have to be creative."` は意志と硬さを落とさない

**EN:** `"If we are to find some alternative system, we have to be creative."`
**行:** 2182
**JP:** `代替策を見つけるには創意工夫が必要です`

**要旨:** 意味は通るが、ここは「見つけるつもりなら」という研究者の踏み込みと、後続へ向けた硬さが要る。

### E-13-02 泣き崩れが実験打ち切りの直接原因だと読めるようにする

**EN:** `"began sobbing uncontrollably, terminating the test"`
**行:** 2196
**JP:** `激しく泣き始めた。研究者らが介入し、実験は早期に終了した。`

**要旨:** ここは「泣いた。その後終了」ではなく、「泣き崩れたため打ち切り」でつなげたい。

### E-13-03 `"only SCP-8980's general proximity"` は近くにいるだけで足りることを保つ

**EN:** `"only SCP-8980's general proximity"`
**行:** 2200
**JP:** `SCP-8980 の一般的な近接性だけで十分`

**要旨:** `only` は条件の限定であって、単なる付随情報ではない。近くにいるだけで反応するという異常性を、十分条件として立てる必要がある。

### E-13-04 `"I suppose I'm not allowed to push you..."` は押し切りの含みを落とさない

**EN:** `"I suppose I'm not allowed to push you to answer medical questions against your will, according to the Foundation Code of Conduct, so I'll just drop the issue for now. We can circle back to it some other time. Anyways... for the second item on the agenda, let's see—"`
**行:** 2262
**JP:** `財団の行動規範によれば、あなたの意志に反して医学的な質問に答えるよう強要することは許されないですから、今はその件はいったん置いておいて、また別の機会にでも話し合いましょうか。さて…二つ目の議題ですが、ええ?`

**要旨:** ここは制度を盾にしながら話題を押し進める場面で、言い切りの雑さと次の議題へ滑る圧が重要である。

### E-13-05 `"What day is it?"` は「今日は何の日ですか？」ではない

**EN:** `"What day is it?"`
**行:** 2270
**JP:** `今日は何の日ですか？`

**要旨:** ここは日付の確認であり、祝日や記念日の確認ではない。

### E-13-06 `"Please, calm down."` は慰めではなく制止として置く

**EN:** `"Please, calm down."`
**行:** 2294
**JP:** `お願いですから、落ち着きなさい。`

**要旨:** ここは優しい声ではなく、相手の崩壊を押し止めようとする管理的な制止である。

### E-13-07 `"backs itself against the wall"` と `"hysterical sobs"` を身体の位置で訳す

**EN:** `"backs itself against the wall. It begins muttering to itself, hysterical sobs occasionally ringing out."`
**行:** 2296
**JP:** `壁に背中を押し付ける。独り言を呟き始め、時折ヒステリックに大声ですすり泣く。`

**要旨:** ここは単なる心理描写ではなく、追い詰められて壁際へ退く身体移動と、切れ切れに漏れる泣き声が同時に進む場面である。

### E-13-08 `"screams, then sobs loudly, and lowers itself onto the floor"` の重さを落とさない

**EN:** `"SCP-8980 screams, then sobs loudly, and lowers itself onto the floor."`
**行:** 2302
**JP:** `叫び声をあげ、その後激しく泣いて、床に崩れ落ちる。`

**要旨:** `lowers itself` は単なる転倒ではなく、力尽きて床へ沈む動作として読むべきである。

### E-13-09 `"we're guaranteed to make a breakthrough"` の保証を装う押し切りを弱めない

**EN:** `"we're guaranteed to make a breakthrough within a year or two"`
**行:** 2308
**JP:** `1、2年以内には必ず突破口が見つかるに違いない`

**要旨:** ここは確信ではなく、結果を保証するような押し切りが嫌さの芯である。

### E-13-10 `"And I am here to help you, even if you don't understand that yet."` の押し付けを残す

**EN:** `"And I am here to help you, even if you don't understand that yet."`
**行:** 2316
**JP:** `私はあなたのことを救うためにここにいるのだから。`

**要旨:** ここは善意の告白ではなく、相手が拒んでいても自分は正しいと押し通す台詞である。

### E-13-11 `"misogynistic"` の欠落で怒りの焦点をずらさない

**EN:** `"egotistical, narcissistic, misogynistic piece of shit smug FUCKING face!"`
**行:** 2320
**JP:** `自己中でナルシスト、女性蔑視の//**糞野郎**//の、お前の自惚れた顔に監視されて、こんな何の役にも立つはずのない実験に付き合うぐらいなら、いっそのこと死んだ方がマシじゃないですか！`

**要旨:** `女性蔑視の` が抜けると、SCP-8980 がバーンズをどう見ているかという怒りの焦点が薄まる。

### E-13-12 `"without warning, lunges at Dr. Byrnes..."` と名乗りの爆発をひと続きにする

**EN:** `"SCP-8980, without warning, lunges at Dr. Byrnes over the table, knocking them both to the floor. Dr. Byrnes yells in terror."` / `"MY FUCKING NAME IS LILLIAN MARLEY, YOU GODDAMN PIECE OF SHIT!"`
**行:** 2324 / 2326
**JP:** `前もっての注意もなしにテーブル越しにバーンズ博士に飛び掛かり、両名とも床に倒れる。バーンズ博士は慄き、叫び声をあげる。` / `私の名前はリリアン・マーリーなの、__この糞野郎！__`

**要旨:** ここは乱闘の勢いと、名乗りを奪い返す爆発が一体である。動作と台詞を切り離すと、反撃の圧が弱まる。

### E-13-13 `"Dr. Byrnes struggles wildly as SCP-8980 frantically begins searching."` は乱闘の暴力を消さない

**EN:** `"Dr. Byrnes struggles wildly as SCP-8980 frantically begins searching."`
**行:** 2328
**JP:** `バーンズ博士は激しくもがき苦しむ。`

**要旨:** `struggles wildly` と `frantically begins searching` が同時に起きているので、単なる抵抗や落ち着いた格闘にしない。

### E-13-14 `"pulls himself up using the knocked-over table"` は床から身を引き起こす重さを落とさない

**EN:** `"Dr. Byrnes pulls himself up using the knocked-over table, holding his stomach."`
**行:** 2334
**JP:** `ひっくり返されたテーブルにつかまりながら腹を押さえて立ち上がる`

**要旨:** ただ立ち上がるのではなく、倒れた体を支えながら引き起こす動作として読ませたい。

### E-13-15 `"sobs and moans softly"` は声の質をずらさない

**EN:** `"Instead, it sobs and moans softly on the floor, slowly curling itself into a fetal position."`
**行:** 2336
**JP:** `床の上で静かにすすり泣き、うめき声を上げながらゆっくりと胎児のように体を丸める。`

**要旨:** ここは単なる「泣く」ではなく、弱ったうめきと縮こまりが残る場面である。`groans` の音の質を落としすぎない。

### E-13-16 `"for the safety of both the anomaly and its containment personnel"` の対称性を立てる

**EN:** `"for the safety of both the anomaly and its containment personnel"`
**行:** 2346
**JP:** `アノマリーと収容担当職員両方の安全を確保するため`

**要旨:** 意味は通るが、被害者と職員を同じ「安全」の枠へ並べる制度語の冷たさを、もう一段残したい。

### E-13-17 `"thoughtful, compassionate, and patient"` から `"ultimately resulted in it committing suicide"` までを一続きで読む

**EN:** `"Dr. Crawford has generally been described as thoughtful, compassionate, and patient by most of the anomalies put under her care in the past. However, several incidents demonstrating grossly inappropriate behavior throughout her career resulted in the Foundation terminating her employment in 2013. This includes a particularly grievous incident in 2012, involving a romantic relationship with a male anomaly under her care that ultimately resulted in it committing suicide in containment."`
**行:** 2360
**JP:** `クロフォード博士は、過去に彼女のケアを受けたアノマリーのほとんどから、思慮深く、思いやりがあり、忍耐強いと評されていました。しかし、彼女のキャリアを通じて著しく不適切な行動を示すいくつかの事件が相次いだため、財団は2013年に彼女の雇用を終了しました。これには2012年に発生した特に深刻な事件が含まれており、それは、彼女がケアしていた男性アノマリーとの恋愛関係が原因で、最終的にアノマリーが収容室内で自殺したというものです。`

**要旨:** ここはクロフォードの善人評と加害歴を同じ段落で往復させる箇所であり、`particularly grievous` と `involving` と `ultimately resulted` の因果を切らさないことが重要である。

## 実務上の結論

- 崩壊から制度語までを一続きで読ませる
- バーンズの断言は無責任な保証として訳す
- 動作は身体の重さを落とさない

---

# SCP-8980 該当箇所 14 査読

**対象 EN:** `articles/fragment_scp-8980-1/segments/en/14_addendum8_health_crawford.wikidot`
**対象 JP:** `bad_translation_jp_single.wikidot`

## このファイルの使い方

既存査読で大きな論点はかなり拾えている。
この改稿では、未収録の論点を原文の登場順で、実際に直すための作業項目として並べ直す。

## 総評

この箇所では、クロフォードの刷り込みが後半のバーンズ面談でそのまま再生される。
したがって、前半の身体描写と後半のメタデータ、復唱、退室要求のどれも小粒ではない。

## 直すべき箇所 [ERROR]

### E-14-01 `"What makes you say that, Lillian?"` から `"fidgets in place absentmindedly"` までを、穏やかな誘導として残す

**EN:** `"What makes you say that, Lillian?"` / `"fidgets in place absentmindedly"` / `"Dr. Crawford is occupied writing notes at her desk"`
**行:** 2408 / 2440 / 2440
**JP:** `どうしてそう思うんですか、リリアン？` / `ぼんやりとその場で足踏みをしている` / `クロフォード博士は机でメモを取っており`

**要旨:** ここは雑談の入口ではなく、相手をほどきながら話を引き出す誘導である。`occupied writing notes` を弱めると、クロフォードが話を聞くより記録を優先している嫌さが抜ける。

### E-14-02 `"His loss, right?"` は慰めの軽口であって、確認ではない

**EN:** `"His loss, right?"`
**行:** 2484
**JP:** `彼の損です。いいですね？`

**要旨:** ここは相手を軽く慰める語り口であり、採点のような確認にするとクロフォードの押しつけが弱まる。

### E-14-03 `Something new seems to be bothering you today.` と `It's important...` を、やさしい語で丸めない

**EN:** `"Something new seems to be bothering you today."` / `"It's important for you to be able to communicate your feelings with me if you want me to be able to help you."`
**行:** 2542 / 2548
**JP:** `なんだか今日はいつもと違うことがあるみたいですね。` / `私があなたを助けられるようになりたければ、気持ちを私に伝えられることが大事ですよ。`

**要旨:** ここは相談の顔をした上書きであり、話しやすさを演出しながら相手の拒否権を奪っている。

### E-14-04 `It's simply awful, isn't it?` から `There's no shame...` までを、慰めの顔をした上書きとして読む

**EN:** `"It's simply awful, isn't it?"` / `"Oh, dearie, it's my job to know these things."` / `"There's no shame in feeling upset or angry at the circumstances you've been put in."`
**行:** 2554 / 2566 / 2588
**JP:** `それは、ひどいことですよね？` / `あら、そういうことを知っておくのは私の仕事なんですから。` / `置かれた状況に腹を立てたり落ち込んだりしても、恥じることはありません。`

**要旨:** ここは同意を取りながら、相手の受け取り方を全部クロフォード側の枠へ戻している。`It's simply awful, isn't it?` を外すと、同情の口調だけが残って、同意の押しつけが見えなくなる。

### E-14-05 `"What's the fucking point, then?"` と `"What the hell do I do then?"` を、追い詰められた行き場のなさとして返す

**EN:** `"What's the fucking point, then?"` / `"(Mumbling) What the hell do I do then?"`
**行:** 2576 / 2594
**JP:** `じゃあ、何の意味があるんだよ？` / `じゃあ、私は何をすればいいんだよ。`

**要旨:** ここは説明を求めているのではなく、行き先を失った反発が噴き出している。無難な質問にすると、追い詰められた感じが抜ける。

**何がだめか:**

- 追い詰められた反発が、ただの疑問に見える
- 受け身の苦さが弱まり、クロフォードの誘導が軽く見える

### E-14-06 `"a challenge"` は前段で植え付けられた言い換えである

**EN:** `"consider their problems like... a challenge"` / `"A challenge..."` / `"Yeah... a... a challenge, right? It's a challenge. I can... yeah... yeah..."`
**行:** 2598 / 2610 / 2614
**JP:** `課題のように考える` だけで済ませた訳 / 復唱

**要旨:** ここはクロフォードが「乗り越えるもの」という枠へ言い換え、SCP-8980 がそれを呑み込んで自分に言い聞かせる場面である。復唱だけ切り出すと、植え付けの気味悪さが薄れる。

### E-14-07 `"SUBJECT: Newfound Motivation"` は「動機」ではなく、持ち上がった意欲の件名である

**EN:** `"SUBJECT: Newfound Motivation"`
**行:** 2646
**JP:** `新たに見つかった動機`

**要旨:** 件名を説明文にすると、報告書の冷たさではなく質問票みたいに見える。ここは生産性の急上昇を示すラベルとして置く。

### E-14-08 ログ ID `8980-S12` を崩さない

**EN:** `ID 8980-S12`
**行:** 2656
**JP:** `IDは8980-W12`

**修正:** `8980-S12` に戻す。

**要旨:** これは単純だが重大な誤記で、文書追跡性を壊す。

### E-14-09 `"change of heart"` と `"gives a single shit about me"` で、心境の変化を疑問視するだけに留めない

**EN:** `"we've had such a sudden change of heart"` / `"I'm sure Steele gives a single shit about me"`
**行:** 2668 / 2670
**JP:** `あなたがなぜそんなに急に考えを変えたのか` / `ああ、スティールなんかがどうして私のことを気にするんでしょうね`

**要旨:** ここは、バーンズが生産性の急上昇を「心境の変化」として疑い、SCP-8980 がその見立てを下品に突き返す場面である。`single shit` の汚さを抜くと、苛立ちが丸くなる。

**何がだめか:**

- `we've had such a sudden change of heart` を単なる心境の変化にすると、バーンズの疑念が薄くなる
- `single shit` の汚さが抜ける
- SCP-8980 の突っぱね方が丸くなる

### E-14-10 `"I'm just feeling better, alright?"` から `"Can I go?"` までを、押しつけられた同意として拾う

**EN:** `"I'm just feeling better, alright?"` / `"My therapist has been really useful."` / `"I admit it. Therapy was helpful. Can I go?"`
**行:** 2674 / 2674 / 2678
**JP:** `いいですか？私はただ気分がよくなっただけ。セラピストのおかげです。` / `あなたの言う通りでしたよ、いいですか？セラピストが本当に役に立ったんですよ？`

**要旨:** ここは `alright?` と `okay?` を重ねながら、相手の語彙をなぞって退室を求めている。`I'm just feeling better` を落とすと、前段の刷り込みが終わった後の自動再生が見えなくなる。

**何がだめか:**

- `I'm just feeling better, alright?` が落ちる
- `I admit it.` が落ちる
- `Can I go?` が落ちる
- 退室要求が消えて支配関係の嫌さが弱まる

### E-14-11 `"get their act together"` を、道徳的更生ではなく持ち直しとして読む

**EN:** `"It's not so common for someone to get their act together without fixing the root cause."`
**行:** 2680
**JP:** `根本的な原因を解決せずに行動が改まるのはあまり宜しいことではないようで。`

**要旨:** ここは素行の更生を言っているのではなく、異常な持ち直し方の不自然さを見ている。`行動が改まる` にすると、医療的な観察が道徳説教に寄る。

### E-14-12 `"I plead the fifth"` を法廷文言に寄せすぎない

**EN:** `"I plead the fifth."`
**行:** 2684
**JP:** `黙秘権を行使します。`

**要旨:** これは本気の法廷答弁ではなく、皮肉を帯びた決まり文句である。硬すぎると、SCP-8980 が Byrnes をかわした冗談の感じが消える。

### E-14-13 `"Can't a lady do her fucking job in peace?"` と `"Why do you have to worm..."` を落とさない

**EN:** `"Can't a lady do her fucking job in peace? Why do you have to worm your way into every goddamn thing I do?"`
**行:** 2690
**JP:** なし

**要旨:** ここは、SCP-8980 がようやく抑え込んでいた怒りを噴き出す場面である。ここを抜くと、後の切り上げ要求が単なる切り替えに見える。

### E-14-14 `"Thanks for wasting my time. Asshole."` を落とさない

**EN:** `"Thanks for wasting my time. Asshole."`
**行:** 現行source_en.wikidotに該当行なし
**JP:** なし

**要旨:** この一言で、面談は「終わった会話」ではなく、見せかけの対話を使った消耗戦だったと分かる。

## 実務上の結論

- 前半の誘導は、単なる雑談に整えない
- 中盤の同情は、相手の受け取り方を上書きしていると明示する
- 後半の拒絶は、最後まで拒絶として残す
- 退室要求と罵倒は、抜くと場面の重さが落ちる

---

# SCP-8980 該当箇所 15 査読

**対象 EN:** `articles/fragment_scp-8980-1/segments/en/15_incident2_ace_exploit.wikidot`
**対象 JP:** `bad_translation_jp_single.wikidot`

## このファイルの使い方

この箇所は、担当医の宥め、SCP-8980 の絶望、バーンズ再登場の衝撃、制度語の冷たさが一気に噴き出す場面である。
したがって、慣用句、呼称、薬理語、動作、感情の噴出をすべて雑に扱えない。

- `[ERROR]` はそのまま修正対象
- `[NOTE]` は補強候補として残す
- `[OUT-OF-SCOPE]` はこの箇所単体の修正指示から外す

## 総評

この箇所で落としてはならないのは次の 4 点である。

- 担当医の宥め文句は、安心させる声ではなく責任回避の定型句として聞こえること
- バーンズを見た瞬間の SCP-8980 の絶望が平板化しないこと
- 室内動作と薬理語を正しく読むこと
- 末尾の調査コメントが、ただの要約ではなく冷たい制度語として残ること

ここを普通の医療場面の日本語で均すと、「助けを求めても制度ごと見殺しにされる場面」が、単に怖い処置の記録へ痩せる。

## 直すべき箇所 [ERROR]

### E-15-00 監査許可の出所と身体検査をぼかさない

**EN:** `"Dr. Byrnes requested and received permission from the Site-17 Containment Oversight Committee to conduct a full audit of SCP-8980 and its containment area."`
**行:** 2720 / 2722
**JP:** `サイト-17収容監視委員会に対してSCP-8980およびその収容区域の全面監査の実施を要請し、許可を受理されました`

**要旨:** ここは「誰が申請し、誰が通し、誰が承認したのか」を分けて読めるようにしないと、監査そのものが中立の手続きに見えてしまう。さらに、その直後の身体検査までが「通ったからやった」処理に見えやすくなる。

**何がだめか:**

- `requested and received` が一続きに流れて、バーンズが申請した事実が弱まる
- `from the Site-17 Containment Oversight Committee` の責任主体が見えにくい
- 監査と一緒に行われた解体・捜索が、過剰な制度暴力ではなく事務処理の延長に見える

### E-15-01 `"No harm, no foul"` を字義分解しない

**EN:** `"No harm, no foul."`
**行:** 2802
**JP:** 構成語へ分解した説明調の訳

**要旨:** ここは「問題ないから大丈夫」という、責任回避の定型句として訳すべきである。

**何がだめか:**

- 規則違反容認の説明に見える
- 後段の逡巡と裏切りの構図が崩れる

### E-15-02 発話中断と侮辱未遂を整えない

**EN:** `the list of "targeted engrams" for the //nu//—ice doctor, here`
**行:** 2782
**JP:** `この、//しんま//……いや、信頼のおける担当医`

**要旨:** ここは言い間違えを取り繕いながら相手を下げる一瞬であり、整った自己修正にするとバーンズの軽蔑が消える。

**修正の方向:**

- 中断記号を残す
- 言い直し後も持ち上げではなく、ごまかしとして聞こえる語にする

### E-15-03 `"ma'am"` を「奥様」にしない

**EN:** `"ma'am"`
**行:** 2824
**JP:** `奥様`

**要旨:** ここで必要なのは職業的距離を保つ一般呼称であって、婚姻や主従を含む呼び方ではない。

### E-15-04 `"sedative"` を「鎮痛剤」にしない

**EN:** `"a quick-acting light sedative agent"`
**行:** 2834
**JP:** `鎮痛剤`

**要旨:** ここは痛みを取る薬ではなく、抵抗を抑えるための鎮静である。

### E-15-05 `"station"` を部屋単位で読まない

**EN:** `"station"`
**行:** 2796
**JP:** `記憶処理室に連れ戻す`

**要旨:** ここは室内の注射台や処置台であって、部屋全体への移動ではない。

### E-15-06 `"Oh god."` の原初的な絶望を平らにしない

**EN:** `"Oh god."`
**行:** 2766
**JP:** `なんでなの。`

**要旨:** これは問いではなく、バーンズを見た瞬間の絶望の噴出である。

### E-15-07 `"apparent"` を曖昧化しない

**EN:** `"stops thrashing in apparent defeat"`
**行:** 2812
**JP:** `敗北したかのようにのたうち回るのを止め`

**要旨:** ここは見るからにそう見える状態であり、「本当は違うかもしれない」含みを足さない。

### E-15-08 事後総括の職権悪用を縮めない

**EN:** `it is clear that Dr. Byrnes abused the protections assigned to the Head Researcher position to purposefully amnesticize SCP-8980 of non-essential concepts and memories. The effects of this can be seen in the following log in the SCP-8980 file.`
**行:** 2942
**JP:** `バーンズ博士が研究主任の地位に与えられた保護権限を濫用し、SCP-8980から本質的でない概念および記憶を意図的に消去したことは明白である。その影響は、SCP-8980ファイルの以下の記録に見て取ることができる。`

**要旨:** ここは「権限を持っていた」ではなく「権限を悪用した」ことが中心である。総括文をやわらげると、記憶消去が職権による制度暴力だったことが消える。

**何がだめか:**

- `abused the protections` の悪用性が弱まる
- `purposefully` の故意が薄れる
- `The effects of this can be seen...` の導入が、単なる説明文に見えてしまう

## 補強したい箇所 [NOTE]

### N-15-03 「復元不能」より冷たい調査語に寄せる余地がある

**EN:** `"could not be rederived"`
**行:** 2958
**JP:** `復元が不可能でした`

**要旨:** このままでも結論自体は伝わるが、ここは感傷ではなく調査上の失敗を書く冷たい文である。`復元` より `再導出` の方が、手が届かなかった感じを制度語として残しやすい。

## このファイルでは採らない論点 [OUT-OF-SCOPE]

### O-15-01 `it` の訳し分け方針

**要旨:** これは記事全体の呼称設計であって、該当箇所 15 単体で決めるべき論点ではない。

### O-15-02 該当箇所 16 のバーンズ発話をここで扱わない

**要旨:** この例は実際には該当箇所 16 側の対象であり、該当箇所 15 の修正指示からは外す。

## 実務上の結論

- 担当医の定型句は「宥め」ではなく「責任回避」として訳す
- バーンズ再登場の衝撃は問いではなく絶望の噴出で受ける
- 該当箇所外の設計論は本文の修正指示に混ぜない

---

# SCP-8980 該当箇所 16 査読

**対象 EN:** `articles/fragment_scp-8980-1/segments/en/16_addendum9_depression.wikidot`
**対象 JP:** `bad_translation_jp_single.wikidot`

## このファイルの使い方

この箇所は記事の感情的頂点であり、クロフォードのガスライティングと、バーンズ面会での壊れた懇願が連続する。
したがって、ここでは「意味が通る」では足りない。誰の言葉が誰の頭に住み着いているか、どのくらい壊れているかを、そのまま読める日本語にする必要がある。

- `[ERROR]` はそのまま修正対象
- `[NOTE]` は有効だが、断定を弱めて使う
- `[OUT-OF-SCOPE]` はこの箇所の修正指示から外す

## 総評

この箇所で最優先なのは次の 4 点である。

- クロフォードの声を「優しい人」で終わらせないこと
- 宗教的慣用句や定型句が借りてくる道徳権威を落とさないこと
- SCP-8980 の懇願を儀礼的な申し出にしないこと
- バーンズの最後の祝辞を、露骨な脅迫へ変質させないこと

ここを丸めると、クロフォードは「寄り添う年長者」に、バーンズは「ただ脅すだけの男」に見えてしまい、作品の芯であるガスライティングと永続支配が薄まる。

## 直すべき箇所 [ERROR]

### E-16-01 `"Ah, here we go."` は開始宣言ではなく探索完了の独り言

**EN:** `"Ah, here we go."`
**行:** 2982
**JP:** `では、始めましょう。`

**要旨:** 直前ト書きがファイル探索で、直後も報告書読解に続くため、ここは会話開始ではない。

### E-16-01a `"The amnestics got you down, huh?"` を真面目な診断にしない

**EN:** `"The amnestics got you down, huh?"`
**行:** 2990
**JP:** `記憶処理のせいで気分が落ち込んでいるんですか？`

**要旨:** ここは診断でも共感でもなく、相手を軽くからかいながら話題を握るための切り出しである。真面目な病状確認にすると、クロフォードの軽薄さと支配の入り口が弱まる。

### E-16-02 `"turn the other cheek"` の道徳権威を落とさない

**EN:** `"turn the other cheek"` / `Only then will you finally be able to get ahead.`
**行:** 3048 / 3048
**JP:** `甘んじる`

**要旨:** ここは聖書由来の定型句を借りて、抵抗せず受け入れろと強要する場面である。続く `Only then...` も、前後を切らずに「そうして初めて」の説教調として拾わないと、服従を道徳化する圧が落ちる。

### E-16-03 `"Here's to many more."` を露骨な脅迫にしない

**EN:** `"Here's to many more."`
**行:** 3176
**JP:** `ここからが本番だよ。`

**要旨:** ここは祝辞の形式で永続支配を告げるのが嫌さの核心であり、脅迫に寄せすぎるとバーンズの質が変わる。

### E-16-04 「差し上げましょう」の連打をやめる

**EN:** `"I'll give you everything I own. All of it. You can have everything in my bank account and in my room. I'll draw out loans for you that I can't pay back. I'll give you my paycheck. Everything."` / `"I'll— I'll work whatever assignment you g-give me. I'll let you take credit for all of my papers. I'll be your s— (//SCP-8980 gulps.//) your secretary. I'll bring you your morning coffee and make you your sandwiches. //I'll lick your shoes.//"` / `"I'll... I'll even sleep with you. Please."`
**行:** 3136 / 3140 / 3146
**JP:** `差し上げましょう` の連打

**要旨:** ここは床に崩れた人間の絶望であって、儀礼的な贈与宣言ではない。

### E-16-08 `"There... there's always work to be done."` の壊れた復唱を落とさない

**EN:** `"I suppose our emotional little brains are just like the Foundation itself, no? No matter how hard of a job we do, there's always work to be done."` / `"There... there's always work to be done."`
**行:** 3060 / 3064
**JP:** `私たちの感情を司る小さな脳は、財団そのものとよく似ているとは思いませんか？どんなに大変な仕事をしても、常にやるべきことが常にあるんですから。` / `そう… やるべきことは常にあるのね。`

**要旨:** ここはクロフォードの説教が SCP-8980 の口の中に入り込んで戻ってくる場面である。単なる同意や要約にすると、ガスライティングの侵入が消える。

**何がだめか:**

- `There's always work to be done` を、単なる諭しや感想に薄めてはいけない
- 直後の `There... there's always work to be done.` は、壊れた復唱として別格に扱う必要がある
- この復唱を落とすと、終盤で SCP-8980 の内面が侵食された事実が弱まる

### E-16-09 末尾の一文欠落を戻す

**EN:** `"SCP-8980 slowly lifts itself off the floor, and gets ready for work."`
**行:** 3180
**JP:** `午前8:00:03 | 1時間半にわたって何の活動もなかった後、SCP-8980の室内のリモートワーク装置がその日の作業スケジュールを印刷した。SCP-8980はゆっくりと床から身を起こし、仕事の準備を始めた。`

**要旨:** ここは章の締めそのもので、床から身を起こして仕事に戻る流れまで書かれて初めて終わり方が成立する。時計だけで終わると、絶望の完成が切れる。

**何がだめか:**

- 床から身を起こす動きが消える
- そのまま仕事に戻る流れが消える
- 1時間半の沈黙のあとに来る、完全服従の終止符が消える

### E-16-06 `"any other old lady"` の generic singular を落とさない

**EN:** `"any other old lady"`
**行:** 3006
**JP:** `他のおばあさんたち`

**要旨:** ここは特定複数の老女ではなく、無害な「そのへんの年寄り」ロールを押しつける言い方である。

### E-16-07 斜体の焦点をずらさない

**EN:** 自発性の真偽に掛かる強調
**行:** 3002
**JP:** `自発的にやった`

**要旨:** 強調は行為そのものではなく、「本当に自分で選んだのか」に掛かっている。

## 補強したい箇所 [NOTE]

### N-16-01 「あらま」は許容だが、声としてはもう一段詰められる

**EN:** `"Oh dear."`
**行:** 3052
**JP:** `あらま`

**要旨:** このままでも機能はするが、幼い軽さが少し前に出る。直後に被害の話へ入ることを考えると、もう半歩だけ抑えた声の方がクロフォードのいやらしさが続きやすい。

### N-16-02 `"victim mentality"` 周辺は軽蔑の調子まで拾いたい

**EN:** `"victim mentality"`
**行:** 3020
**JP:** `被害者意識`

**要旨:** `被害者意識` 自体で意味は通るが、この場面は診断名ではなく、相手を見下しながら責任転嫁する言い方である。少し棘を足せるなら、その方がクロフォードの加害が見えやすい。

### N-16-03 「犯す」は強すぎる可能性がある

**EN:** `"If I wanted to fuck you, I would've done it by now."`
**行:** 3166
**JP:** `あんたのことを犯したいなら、とっくにそうしてるさ。`

**要旨:** このままでも加害性は強く出るが、`犯す` は原文より一段踏み込みすぎる。硬い誤りではないものの、もし距離を戻すなら性交表現の範囲で止める方が原文に近い。

### N-16-04 バーンズの一人称切替は設計としては有効

**要旨:** 原文の必須条件ではないが、日本語で仮面が剥がれる瞬間を出す案としては使える。このままでも成立するが、採るなら該当箇所 16 だけの思いつきではなく、バーンズ全体の声として揃えたい。

### N-16-05 吃音だけでなく言い直し構造も拾いたい

**要旨:** 現状訳でも崩れはあるが、吃音だけでなく言い直しまで残すと、頭の中で言葉が絡まる感じがもう少し出る。直さなくても致命傷ではないが、効く調整ではある。

### N-16-06 深いため息の身体感覚をもう少し出したい

**要旨:** 意味は通るが、聞こえるほど深いため息の質感を補える。細い点ではあるが、SCP-8980 がそれだけで怯む場面なので、音と深さは拾う価値がある。

## このファイルでは採らない論点 [OUT-OF-SCOPE]

### O-16-01 担当医台詞との時系列接続メモ

**要旨:** これは該当箇所 15 側の論点であり、該当箇所 16 既存訳の当否判定としては対象外である。

## 実務上の結論

- クロフォードの善意語をそのまま善意として訳さない
- 壊れた懇願は身体状態に合う崩れ方へ戻す
- NOTE 論点は「直さないと成立しない誤り」ではなく「もう一段詰めたい調整」として扱う

---

# SCP-8980 該当箇所 17 査読

**対象 EN:** `articles/fragment_scp-8980-1/segments/en/17_addendum10_neutralization.wikidot`
**対象 JP:** `bad_translation_jp_single.wikidot`

## このファイルの使い方

この箇所は短いが、虐待後の症状を制度文書がどう記録するかを決める。
したがって、小さい用語差でも読み筋を変えるものは落とさない。

## 総評

ここで大事なのは、マクファレルが Lillian を道徳的に批評しているのではなく、虐待後の対人機能の崩れを臨床的に観察していることを守ることである。

## 直すべき箇所 [ERROR]

### E-17-01 `"social awareness"` は「社会意識」ではない

**EN:** `"a lack of social awareness"`
**行:** 3200
**JP:** `社会意識の欠如`

**要旨:** ここは公共心や社会問題への関心ではなく、対人文脈の把握や社会性の崩れである。

**何がだめか:**

- 道徳的・政治的な意味に滑る
- 虐待後の症候としての読みが弱くなる

## 補強したい箇所 [NOTE]

### N-17-01 `"none of its stated anomalous properties"` は「いずれも」を落とさない

**EN:** `"possessed none of its stated anomalous properties"`
**行:** 3198
**JP:** `記載されている異常性を一切保持していない`

**要旨:** 意味は通るが、列挙された異常性質を一つずつ確認していった感じが弱い。ここは「いずれも」で、項目ごとの全否定を見せた方がよい。

### N-17-02 `noted that the entity possessed several alarming features` は「察知した」ではない

**EN:** `"noted that the entity possessed several alarming features"`
**行:** 3200
**JP:** `いくつかの憂慮すべき特徴を保持していることを察知しました`

**要旨:** `noted` は勘で見抜く語ではない。観察した、記録した、所見として認めた、という事務的な向きに寄せる。

### N-17-03 `As of January 19th, 2015` は状態更新の時点を先に固定する

**EN:** `"As of January 19th, 2015, SCP-8980 began rehabilitation and reintegration into the wider Foundation workplace under direct supervision from Dr. Morgan McPharrell. SCP-8980 is pending reclassification to Neutralized."`
**行:** 3202
**JP:** `2015年1月19日現在、モーガン・マクファレル博士の直接の監督の下、SCP-8980はリハビリテーションと財団の職場への再統合を開始しています。SCP-8980は現在、Neutralizedへの再分類待ちです。`

**要旨:** 過去の発効点と、文書が今述べている現在の状態が混ざっている。ここは「付で」「保留中」で、過去の開始と現在の保留を分けて置く。

## 実務上の結論

- symptom を moral な語へずらさない
- この箇所では、短さより用語の向きを優先する

---

# SCP-8980 該当箇所 18 査読

**対象 EN:** `articles/fragment_scp-8980-1/segments/en/18_investigation_summary.wikidot`
**対象 JP:** `bad_translation_jp_single.wikidot`

## このファイルの使い方

この箇所は、法務語の精度がそのまま作品の倫理的結論になる。
したがって、読みやすさより先に「どの違反を、どの語で名指ししているか」を守る。

## 総評

見た目は単なる違反一覧だが、実際には「バーンズが何をしたかを、財団が裁ける言葉へ落とし込む」場面である。
今回の 6 件はすべてそのまま採る。

## 直すべき箇所 [ERROR]

### E-18-01 `"abuse of an anomaly"` は「濫用」ではなく「虐待」

**EN:** `"Abuse of an anomaly"`
**行:** 3264
**JP:** `アノマリーの濫用`

**要旨:** ここで裁かれているのは物品悪用ではなく、知性ある被害者への虐待である。

### E-18-02 `"extort, manipulate"` を「脅迫・教唆」にしない

**EN:** `"extort, manipulate"`
**行:** 3260
**JP:** `脅迫・教唆`

**要旨:** これは権力を使った圧力と操作であって、犯罪のそそのかしではない。

### E-18-03 `"intimidation"` を前項と同じ「恐喝」に潰さない

**EN:** `"Deliberate intimidation of an anomaly"`
**行:** 3268
**JP:** `意図的な恐喝行為`

**要旨:** ここは金品目的の脅しではなく、恒常的な威圧である。

### E-18-04 条番号 `2.4.1` を落とさない

**EN:** `"Gross negligence of an anomaly. (Title 2, Chapter 2 § 2.4.1)"`
**行:** 3266
**JP:** `第2章第2節第2.4.1条: アノマリーに対する重大な過失`

**修正:** 怠慢側を `第2章第2節第2.4.1条` に戻す。

**要旨:** 違反類型ごとの切り分けそのものがこの文書の核心なので、条番号の誤記は小さくない。

### E-18-05 `"experience with Dr. Crawford"` は未来の再接触ではない

**EN:** `"SCP-8980's experience with Dr. Crawford"`
**行:** 3325
**JP:** `クロフォード博士と接することで`

**要旨:** ここは過去に受けた体験の後遺であり、「また会わせるのは危険だ」に狭めない。

### E-18-06 `"keep this case open indefinitely"` は案件保留の無力感が芯

**EN:** `"keep this case open indefinitely"`
**行:** 3351
**JP:** `当面の間継続して調査を行う予定`

**要旨:** ここは調査継続ではなく、打つ手がないまま案件だけが開きっぱなしで残ることが重要である。

## 補強したい箇所 [NOTE]

### N-18-01 勧告リストは 3 本立ての命令形として保つ

**EN:** `1. Provide monetary compensation to SCP-8980 for the abuse it suffered under Dr. Christopher Byrnes. / 2. Provide free parapsychological counseling to SCP-8980 for the remainder of its tenure at the Foundation. / 3. Request the Fire Suppression Department to soft-monitor SCP-8980 in order to properly reintegrate it back into the Foundation's workplace environment.`
**行:** 3287 / 3288 / 3289
**JP:** `1. クリストファー・バーンズ博士の下で受けた虐待に対し、SCP-8980に金銭的補償を提供すること。 / 2. SCP-8980の財団在籍期間を通じ、無償の超心理カウンセリングを提供すること。 / 3. SCP-8980を財団の業務環境に適切に再統合するため、火災鎮圧部門にソフトモニタリングを依頼すること。`

**要旨:** ここは説明文ではなく勧告の列挙である。各項目を命令形のまま並べ、3 本の勧告だと分かる形を崩さない。

### N-18-02 `as well as requiring three months of remedial therapy` は標準処分の付け足しではない

**EN:** `"the standard escalation of docking one week of pay, as well as requiring three months of remedial therapy"`
**行:** 3277
**JP:** `1週間の給与減額と3か月間の強制療法`

**要旨:** `as well as` をただの `and` に落とすと、標準処分の内訳であることが弱まる。給与減額と矯正療法を、同じパッケージの中身として見せる。

### N-18-03 委員会投票の報告文は結果だけでなく、投票される手続きまで残す

**EN:** `"All three Ethics Committee Proposals presented by the Review Team have passed."` / `"Foundation Motions will be put up for vote at the next annual Inter-Committee Council Session, should they be approved by the Ethics Committee as a whole."`
**行:** 3320 / 3309
**JP:** `倫理委員会に提出された全ての提案は可決されました。財団の動議については、倫理委員会全体で承認された場合、次回の年次各委員会合同会議において投票が行われる予定です。`

**要旨:** ここは単なる可決報告ではなく、提案が審査を通って、さらに本会議で投票されるという手続きの段階を示している。`should` と投票の二段構えを残す。

### N-18-04 `Thank you for your invaluable efforts in this case, Roberts.` は委員長の評語として置く

**EN:** `"Thank you for your invaluable efforts in this case, Roberts."`
**行:** 3307
**JP:** `この件でのあなたの貴重な尽力に感謝します、ロバーツ。`

**要旨:** ここは単なる礼ではなく、委員会側が査読結果を認めて閉じる評語である。`invaluable efforts` を軽くしすぎない。

## 実務上の結論

- 法務語の向きを絶対に取り違えない
- 条番号や違反区分を軽視しない
- 終盤コメントは制度的な無力感を残して閉じる

---

# SCP-8980 該当箇所 19 査読

**対象 EN:** `articles/fragment_scp-8980-1/segments/en/19_mcpharrell_email_logout.wikidot`
**対象 JP:** `bad_translation_jp_single.wikidot`

## このファイルの使い方

この箇所は記事の結語であり、マクファレルの私信とログアウト表示が読後感を決める。
したがって、報告書の硬さではなく、「親しい同僚への業務メール」の声を正しく出すことが重要になる。

- `[ERROR]` はそのまま修正対象
- `[NOTE]` は本文の断定を弱めたうえで残す

## 総評

現行訳は、慣用句の字義分解と、メールの言葉遣いのずれが集中している。
ここで私信らしい疲弊、罪悪感、苛立ちが消えると、記事全体が「報告書で終わった」ように見えてしまう。

ここは制度文の余韻ではなく、制度に擦り切れた同僚の私信で終わるべき箇所である。

## 直すべき箇所 [ERROR]

### E-19-01 `"sir"` を「旦那様」にしない

**EN:** `"sir"`
**行:** 3433
**JP:** `旦那様`

**要旨:** ここは男性権威一般への反射的服従であり、婚姻・主従・接客の含意を持つ語へずらさない。
この文脈では、自然さと症状の読みやすさの両方を考えると `先生` が使いやすい。

**修正の方向:**

- `先生`
- `マクファレル様`
- 必要なら原語保持 + 注記

### E-19-02 メール冒頭を会話文にしない

**EN:** `"Good afternoon Flora,"`
**行:** 3425
**JP:** `こんにちは、フローラさん。`

**要旨:** ここは親しい同僚宛ての業務メールであり、挨拶は会話文ではなくメール体裁で置くべきである。

### E-19-03 `basically infeasible` の「事実上不可能」を落とさない

**EN:** `"Long-distance is basically infeasible until we can stabilize her technophobia enough to get her on a computer for more than an hour at time."`
**行:** 3429
**JP:** `テクノフォビアをある程度安定させて一度に一時間以上パソコンに向かえるようにならない限り、遠隔カウンセリングは事実上不可能です。`

**要旨:** `basically infeasible` は「たぶん無理」ではなく、実務上もう回らないという強い判断である。ここは事実上不可能の温度で置く。

### E-19-04 `get Director Thompson off my case` を「お叱り」にしない

**EN:** `"But I can't get Director Thompson off my case unless her work gets done, so I've bit the bullet and just started doing her work for her."`
**行:** 3431
**JP:** `でも、彼女の仕事が終わらない限りトンプソン管理官のお叱りは止まらないので、仕方なく彼女の代わりに仕事を引き受けることにしました。`

**要旨:** ここは小言を受ける話ではなく、Thompson を自分の件から引き剥がせないという方向の慣用句である。`off my case` の主語関係を戻す。

### E-19-05 `"bite the bullet"` の覚悟を決める感じを落とさない

**EN:** `"bit the bullet"`
**行:** 3431
**JP:** `仕方なく`

**要旨:** 受動的な諦めではなく、嫌なことに腹をくくって踏み切る感じが必要である。

### E-19-06 `"Between A and B"` の並列を保つ

**EN:** `"Between A and B"`
**行:** 3435
**JP:** `それに加えて`

**要旨:** ここは二種類の負担が並列してマクファレルを摩耗させているのであって、片方を副次化しない。

### E-19-07 `"pain in my ass"` の私信らしい毒気を落とさない

**EN:** `"pain in my ass"`
**行:** 3435
**JP:** `厄介な存在`

**要旨:** ここは業務文ではなく愚痴の私信であり、もっと砕けた苛立ちが要る。

## 補強したい箇所 [NOTE]

### N-19-01 `"At least I get overtime pay."` は疑問にしすぎない

**EN:** `"At least I get overtime pay."`
**行:** 3431
**JP:** `せめてもの救いは、残業代をもらえることでしょうか。`

**要旨:** `せめてもの救い` まではよいが、`でしょうか` で締めると自嘲より不確かな疑問に寄る。断定寄りの自嘲に寄せた方がよい。

### N-19-02 `For one` と `random bouts of screaming` は進捗報告の口調を崩さない

**EN:** `"For one, she's finally stopped compulsively calling me "sir". It was a bit funny at first, but it got weird really quick, so I'm glad we can finally move past that. The random bouts of screaming haven't stopped though, and neither has her tendency to stare at me while I sleep, but they've become less frequent."`
**行:** 3433
**JP:** `一つに、私のことを反射的に「先生」と呼ぶのがようやく止まりました。最初は少し可笑しかったんですが、すぐに不気味になったので、ようやくこれが終わってくれてほっとしています。突然叫び出すのはまだ続いていますし、私が寝ている間にじっと見つめるのも相変わらずですが、頻度は減っています。`

**要旨:** `For one` は列挙の入口であり、`bouts` は発作的な反復である。単発の動作に畳み込まず、症状の持続を残す。

### N-19-03 `we've still got a ways to go` は先の長さを残す

**EN:** `"we've still got a ways to go."`
**行:** 3433
**JP:** `まだまだ道のりは長い`

**要旨:** 意味は合うが、`we've still got` の主観的な疲れが薄い。`まだ先は長い` だけでなく、話者が自分の手で抱えている感じを残す。

### N-19-04 `I really needed to get this off my chest.` と `the Committee's hands were tied` を打ち明けとして処理する

**EN:** `"I really needed to get this off my chest. I know you said the Committee's hands were tied, but if there's anything you can do, please help me out here."`
**行:** 3437
**JP:** `このメールを送ることは恐らく、私のキャリアの中で最も馬鹿な行為かもしれませんが、どうしてもこの気持ちのはけ口を見つけたかったのです。委員会にはどうすることもできないと言われましたが、もし何かできることがあれば、どうか私のことをお助けください。`

**要旨:** ここは単なる不満ではなく、打ち明けの独白である。`get this off my chest` は胸の内を明かすことで、`hands were tied` は手が縛られている比喩を保つ。

### N-19-05 `psychotic woman` は臨床語ではなく罵倒として置く

**EN:** `"I'm not sure how much longer I can handle this psychotic woman."`
**行:** 3437
**JP:** `この精神異常な女性に私はこれ以上耐えられないのかもしれません。`

**要旨:** ここは診断ではなく、私信の愚痴としての粗い言葉である。上品な語へ逃がさず、話者の苛立ちを残す。

### N-19-06 `de facto co-opted into being her full-time caretaker` と `she's completely worn me down` を一つの被害として読む

**EN:** `"I've been de facto co-opted into being her full-time caretaker, and frankly she's being a real pain in my ass. Between doing her work and chores for her and dealing with her severe neuroses all day every day, she's completely worn me down to the point that I can't even respect her as a person anymore, much less a coworker."`
**行:** 3435
**JP:** `誰にもこんなことを言えないでしょうが… フローラさん、私は本当に彼女に腹が立ってきました。私は事実上彼女の専属介護人になってしまいました。正直に言って、彼女は本当に厄介な存在です。毎日毎日、彼女の仕事や家事を代わりにやって、//それに加えて//彼女の重い神経症に付き合わされて、彼女のことを人間として尊重できないぐらいに疲れ果ててしまいました。ましてや一同僚として彼女に敬意を払うだなんて無理でしょう。`

**要旨:** ここは「面倒を見るようになった」では弱い。本人の意思に反して介護役へ組み込まれ、摩耗させられた、という被害の向きを残す。

### N-19-07 `Something's gonna give.` は限界ではなく破綻予告として置く

**EN:** `"Something's gonna give."`
**行:** 3435
**JP:** `もう限界は近いのかもしれません。`

**要旨:** `Something` の漠然さが大事で、何が折れるかはまだ決まっていない。`限界` に収束させず、何かが壊れる予告として訳す。

### N-19-08 `calling it quits and letting her rot` は放置の残酷さを落とさない

**EN:** `"calling it quits and letting her rot"`
**行:** 3435
**JP:** `諦めて放っておこうか`

**要旨:** `calling it quits` と `letting her rot` は別動作で、後者には朽ち果てるまで放置する残酷さがある。`放っておく` だけでは弱い。

### N-19-09 結語で `Lillian` を出すかどうかは細い調整点

**要旨:** 人物の残余の見え方に関わるので注記として残すが、硬い誤りではない。このままでも話は通るが、最後まで `her` で押すか、どこかで `Lillian` を戻すかで、マクファレルの情の残り方は少し変わる。

### N-19-10 `Director` の肩書き訳は記事全体で揃えたい

**要旨:** このファイル単独で壊れているわけではないが、制度語の統一として見直す価値がある。いまのままでも大意は崩れないので、本文の必須修正とは分けて扱いたい。

### N-19-11 署名の肩書き表記は書式上の判断幅がある

**要旨:** 修正候補ではあるが、即座の必須修正ではない。署名欄だけ英語肩書きを残すか、日本語本文に合わせるかは書式判断として最後に揃えればよい。

## 実務上の結論

- マクファレルの声は「親しい同僚への疲れたメール」として訳す
- 慣用句は辞書第一義へ崩さない
- NOTE 論点は、メール文体の仕上げとして二段目に回す
