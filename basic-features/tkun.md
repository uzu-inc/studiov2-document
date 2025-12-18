# トークン

トークンは、調査トークンとしての用途のほかに、状態のON/OFFの判定、数値比較など様々な活用が可能です。



## 調査トークン <a href="#investigation" id="investigation"></a>

手がかりを得る際に消費するトークンとする、最も一般的な使い方です。

### トークンの作成 <a href="#add" id="add"></a>

1. トークン編集画面で「トークンを作成」を押します（2つ目以降は右上の「トークンを追加」から）
2. 調査トークンなど名前を入力し、アイコンの形と色を選びます
3. 「配布条件を追加」を押します
4. トークンを配りたいフェーズ、配る数を設定します

<figure><img src="../packages/ja/.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

### 山札でのトークン消費設定 <a href="#deck" id="deck"></a>

1. 山札の編集画面で「消費トークン追加」を押します
2. 消費トークン欄に先程作成したトークンを設定し、消費数を決めます
3. 「消費数と所持数を表示」は、アプリで山札調査を実行する画面での表示のON／OFFを指します（基本ONでよい）

<figure><img src="../packages/ja/.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

調査トークンと合わせて別のトークンも消費する設定にすることで、スキルが必要な山札や特殊調査にも対応できます。

<div align="left"><figure><img src="../packages/ja/.gitbook/assets/image (2).png" alt="" width="563"><figcaption></figcaption></figure></div>



## アイコン・カラーテーマの変更

アイコンやカラーテーマなど状態のON／OFFをトークンの個数に紐づける使い方です。

例えば、以下のような変身スキルを組み込みたいとします。

<div align="left"><figure><img src="../packages/ja/.gitbook/assets/image (223).png" alt="" width="315"><figcaption></figcaption></figure></div>

1. 「変身トークン」を新規作成します
2. 「変身するアクション」と「変身をとくアクション」を[シンプルアクション](../packages/ja/basic-features/action.md#shinpuruakushonno)で作成します
3. それぞれの中身として、「変身トークンをリセットして＋１」 「変身トークンをリセットして０」を設定します
4. キャラクター編集画面で「条件つきアイコン」を追加し、条件として「数値カウント：該当キャラの変身トークンが１と等しい」を設定します（２段階の変身がある場合は同様に「変身トークンが２」の場合も作成）

<figure><img src="../packages/ja/.gitbook/assets/image (224).png" alt=""><figcaption></figcaption></figure>

<div align="left"><figure><img src="../packages/ja/.gitbook/assets/image (225).png" alt="" width="563"><figcaption></figcaption></figure></div>



上記はアイコン変更の例ですが、ニックネーム・カラーテーマ・背景画像でも同様の設定が可能です。

<figure><img src="../packages/ja/.gitbook/assets/image (226).png" alt=""><figcaption></figcaption></figure>



