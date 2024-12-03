# キャラクターによって表示する内容を変えたい

この機能を使うことで、特定の条件を満たしているキャラクターにのみ追加情報が分かるといったギミックを作ることが出来ます。

この機能は現状、以下の箇所で使用できます。

* 基本フェーズの「フェーズの内容」のテキスト/アクション/山札
* テキストタブのテキスト
* 手がかりの「手がかりの詳細」のテキスト

今回は例として手がかりの詳細のテキストを特定の条件によって変更してみましょう。

### ①テキストを作成する

「手がかりの詳細」で、条件分岐を行いたいテキストを作成します。今回は、赤文字の部分を条件によって出し分けたいと思います。

<figure><img src="../packages/ja/.gitbook/assets/スクリーンショット 2023-12-15 16.54.34 (1) (1).png" alt=""><figcaption></figcaption></figure>

### ②表示条件の制限を行う

まず、以下のような手順で条件の制限を行います。

<figure><img src="../packages/ja/.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>

そうすると、条件を設定するダイアログが表示されるので、任意の条件を設定します。

条件の詳しい設定方法は[こちら](../packages/ja/basic-features/condition.md)

<figure><img src="../packages/ja/.gitbook/assets/スクリーンショット 2023-12-15 17.03.47.png" alt=""><figcaption></figcaption></figure>

条件を設定し、「保存する」を押すとテキストの表示が変わり、表示条件が設定されました。

<figure><img src="../packages/ja/.gitbook/assets/スクリーンショット 2023-12-15 17.04.00.png" alt=""><figcaption></figcaption></figure>

動作確認を行ってみましょう。同じ手がかりでも、キャラクターによって違う文章が表示されています。

<figure><img src="../packages/ja/.gitbook/assets/スクリーンショット 2023-12-15 17.04.54.png" alt=""><figcaption></figcaption></figure>
