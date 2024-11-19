---
description: カラーテーマ
---

# カラーテーマ

カラーテーマページからカラーテーマの設定ができます。

<figure><img src="../../.gitbook/assets/image (110).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>

テーマは2024/01/12 現在で以下の種類が使用できます。

<table data-view="cards"><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td><strong>ライト</strong></td><td><img src="../../.gitbook/assets/light (1) (1).png" alt="" data-size="original"></td><td></td></tr><tr><td><strong>ダーク</strong></td><td><img src="../../.gitbook/assets/dark.png" alt="" data-size="original"></td><td></td></tr><tr><td><strong>マリン</strong></td><td><img src="../../.gitbook/assets/marine (1) (1).png" alt="" data-size="original"></td><td></td></tr><tr><td><strong>アンティーク</strong></td><td><img src="../../.gitbook/assets/antique.png" alt="" data-size="original"></td><td></td></tr><tr><td><strong>ドリーム</strong></td><td><img src="../../.gitbook/assets/dream.png" alt="" data-size="original"></td><td></td></tr><tr><td><strong>モダン</strong></td><td><img src="../../.gitbook/assets/modern.png" alt="" data-size="original"></td><td></td></tr><tr><td><strong>メカニカル</strong></td><td><img src="../../.gitbook/assets/mechanical.png" alt="" data-size="original"></td><td></td></tr><tr><td><strong>ノスタルジア</strong></td><td><img src="../../.gitbook/assets/nostalgia.png" alt="" data-size="original"></td><td></td></tr><tr><td><strong>サイバーパンク</strong></td><td><img src="../../.gitbook/assets/cyberpunk.png" alt="" data-size="original"></td><td></td></tr></tbody></table>

文字色は自動で最適化されるので、モードに合わせて変える必要はありません。

![](../../images/mode2.png)



### 設定したタイミングでカラーテーマが変わらない？ <a href="#why-not-change" id="why-not-change"></a>

カラーテーマ設定画面の上から順に、「ライト：フェーズ１が開始した」、「ダーク：フェーズ２が開始した」というテーマを設定しているとします。

フェーズ２開始時点でライトからダークに変わってほしいですが、この設定では変わりません。

フェーズ１→フェーズ２と進んだ場合、「フェーズ１が開始した」という条件はフェーズ２が開始しても満たしていることになるからです。条件は、より上にある画像が優先なので、ライトの条件が満たされている限りずっと、ダークには変わりません。



改善方法

* ライトの条件を「フェーズ１が進行中」に変える
* ライトの条件を「フェーズ１が開始した　かつ　フェーズ２が踏まれなかった」に変える
