# v1 のシナリオを v2 に移行する

ウズスタジオには、オレンジを基調としたv1（旧版エディタ）とブルーを基調としたv2があります。

v1で作成したシナリオは、本ページで説明する手順を踏むと、v2版として公開することができます。v1ではできなかったことがv2では多く実装できるようになっているので、リメイクやアップデートも歓迎です。

## v2移行の手順

### ①v1での操作

※2024年8月6日時点で運営が全シナリオに対して①の処理を終えています。②から実行してください。

* ウズスタジオv1で移行したいシナリオを開きます。
* 左タブの「作品を提出」をクリックします。
* チェックボックスにチェックを入れて「アプリに反映」を押します。

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

### ②v2での操作

* ウズスタジオv2にログインします。
  * ウズアプリで使用しているログイン方法（電話番号・メールアドレスなど）でログインします。
  * ウズスタジオv1に登録しているメールアドレスではありませんので、ご注意ください。
* ウズスタジオv2のシナリオ一覧画面から、先程v1でアプリに反映を押したシナリオを開きます。
* 画面上部に並ぶタブから「リリース管理」をクリックします。
* バージョン欄の「・・・」をクリックし、「このバージョンを復元」をクリックします。
* 成功するとデータ移行が完了しているので、右上の「シナリオを編集」というボタンを押します。データが正常に表示されていれば完了です。\
  ※シナリオが見つかりませんでしたと表示される場合は[こちら](https://docs.studio.uzu-app.com/qanda/qanda#v2shinariono)をお試しください。

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption></figcaption></figure>

### ③移行申請フォームを送信するまでの流れ

1. 上記の説明を参考に、まず**v2エディターでのシナリオ復元**を行います。ざっくり言うと「v1側でアプリに反映を押す」→「v2側で復元する」という手順です。
2. 改行等のレイアウトが一部崩れますので、**v2エディターで調整**ししてください。v2化に伴い、読み合わせフェーズの改善や複数回投票への改善などを行う場合はそのあたりも修正してください。
3. 調整・修正が終わったら、v2エディター右上のボタンより**動作確認**をしてください。
4. 動作確認が問題さそうであれば、v2エディター右上のボタンより「**最新バージョンを作成**」を押してください。
5. 作成に成功したら「リリース管理画面」に自動で遷移します。
6. そこにある「v2移行申請」ボタンから申請を行ってください。

{% hint style="info" %}
その後、運営でシナリオを確認し、v2版を一般ユーザーにも公開できるよう処理をいたします。公開を告知する公式からのSNS投稿は20:00を基本としています。
{% endhint %}

移行申請フォームを送信し、運営による承認・アプリ上の一般ユーザーへの公開が終わったら、v2移行は完了です。

### v2版のテストプレイをしたい場合

バージョンを作成（アプリへの反映）をした後、作者アカウントでウズアプリ内のシナリオページを見に行くと「**最新版でイベントを作成**」というボタンが現れています。そちらからイベントを作成すると、v2版のテストプレイが実施できます。

{% hint style="info" %}
ちなみに、このボタンは作者アカウントでログインした場合にしか見えません。一般ユーザーにはv1版を公開したまま、裏でv2版のテストプレイができる状態です。
{% endhint %}

## v1とv2で異なっている部分

* v2では、ボタンひとつで太字や斜体、見出し文字や色付き文字に変えられるようになっています。
* それに伴い、マークダウン記法を覚える必要がなくなりました。

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## v2移行することで改善できること

### ◆読み合わせフェーズ

* v2では、**読み合わせフェーズをどこにでも何回でも差し込める**ようになりました。
* v1で2回以上の読み合わせを設ける際、キャラ名「セリフ」のようにテキストで代用していた部分を大幅に改善できます。

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

### ◆投票フェーズ

* v2では、**投票フェーズを何回でも設定できる**ようになりました。
* v1シナリオで頻発していた「投票前に投票先を一つに絞るための長い説明」を設ける必要がなくなり、より自然な形で投票できます。

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

* 「キャラクター１が○○に投票しているとき」のような詳細な条件による分岐も設定できるようになっています。

<figure><img src="../.gitbook/assets/スクリーンショット 2024-02-20 20.40.59 (1) (1).png" alt=""><figcaption></figcaption></figure>

### ◆シナリオ途中での分岐

* v2では、**シナリオの途中でも条件に合わせた分岐ができる**ようになりました。
* v1でよく行われていた「改行で中身が見えないように工夫したタブを複数配布して該当するものだけ見てもらう」ような状態を大きく改善できます。

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

### ◆調査・手がかり

* v2では、**投票で調べる場所を選ぶ→該当する手がかりを配布する**といった**調査**が実装できるようになりました。
* 手がかりは「**全体公開**」も「**譲渡**」も「**誰かだけに公開**」もできます。
* v1でよく行われていた「リンクをタップ→画像を表示」で、プレイヤーの良心に任せた擬似調査を大きく改善できます。

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

### ◆その他

* **キャラクターテキストを「あるフェーズにいるときだけ表示する」ことができる**ため、読み返し禁止のようなギミックがより自然に実装できます。
* 読み合わせ中の特定の地の文やセリフをきっかけとして、**フェーズの途中でBGMを変えられる**ようになりました。

<figure><img src="../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>

* **先のフェーズを隠すかどうか選べる**ようになりました。
  * 追加議論があることを最初は見せたくない場合などに有効です。
* **web上の動作確認でBGMやSEも再生される**ようになりました。
* v2シナリオでは、**観戦**が可能です。
  * 作者が観戦者として入れるので、テストプレイがやりやすくなりました。
  * ※v1のままのシナリオは観戦できません。
* v1では感想戦画面で全てのエンディングが強制的に公開されていましたが、v2では**配布するエンディングと配布しないエンディングを作者側で制御できる**ようになりました。
* 感想戦画面における**真相テキストを複数のタブに分ける**ことができるようになりました。
  * 「真相解説はこちら」「宣伝はこちら」のような使い方が可能となります。
* 「**シナリオ傾向**」「**注意事項**」を設定できるようになりました。
  * 「あらすじ」や「作者コメント」に無理やり入れていた注意事項や文章を内容ごとにきちんと分類して表示できるようになっています。

<figure><img src="../.gitbook/assets/image (8) (1).png" alt="" width="375"><figcaption></figcaption></figure>

ウズスタジオv2には、本ページで紹介しきれないくらいたくさんの機能があります。v1では少し不自然な形で実装していたものも、v2ではより自然な状態に改善できますので、ぜひあなたのシナリオもv2版へ移行してみてください。

## よくあるご質問

**Q. v2移行のための処理をすると、すぐにv2版がアプリに反映されてしまいますか？**

A. そんなことはありません。移行と調整が終わったら申請フォームに回答していただきます。申請フォームの回答を運営が確認して処理をおこなうまで、v2版がアプリ上で遊べる状態にはなりませんので、ご安心ください。

**Q. v2版のテストプレイはどうやったらいいですか？**

A. v1版をアプリ上で公開したまま、作者のみが立てられるイベントとして裏でv2版のテストプレイをおこなうことが可能です。作者は観戦者として参加する形になります。

その他のQ＆Aは[こちら](../QandA-v1-v2.md)をご参照ください。
