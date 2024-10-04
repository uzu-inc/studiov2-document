---
description: 可以設定超越簡單線索獲取或牌庫調查的各種動作。
---

# 動作

## 新建動作・種類

從左側菜單移動到「動作」。

點擊「添加動作」，選擇動作的種類，即可新建。

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

動作有以下兩種類型（截至2023.12.7）。

<table><thead><tr><th width="141">名稱</th><th>內容</th></tr></thead><tbody><tr><td><a href="action.md#shinpuruakushonno">簡單</a></td><td>只需按下「執行」即可觸發動作</td></tr><tr><td><a href="action.md#pasuwdoakushonno">密碼</a></td><td>按下「執行」後需要輸入密碼，輸入正確的密碼後動作將被觸發</td></tr></tbody></table>

<figure><img src="../.gitbook/assets/image (54).png" alt="" width="563"><figcaption></figcaption></figure>

## 可設定的動作列表

截至2023.12.7，可以設定以下動作。

<table><thead><tr><th width="226">項目</th><th>內容</th></tr></thead><tbody><tr><td>發送通知</td><td>動作執行時在畫面上方以文字形式發送通知。</td></tr><tr><td>播放音效</td><td>動作執行時播放效果音。</td></tr><tr><td>公開線索</td><td>將特定的線索公開。所有權不會轉移。</td></tr><tr><td>階段轉換</td><td>強制轉移到特定的階段。<br>例如，在推理發表階段等一個玩家的判斷下可以轉移到下一階段的情況下使用是推薦的。</td></tr><tr><td>線索所有權</td><td>將特定的線索分配給角色。</td></tr><tr><td>線索查看權</td><td>將特定的線索查看權賦予角色。</td></tr><tr><td>移動通話房間</td><td>強制移動到特定的通話房間。</td></tr></tbody></table>

## 簡單動作的設定

### 在動作編輯畫面中的設定

* **標題**：動作的標題。可以在右側的預覽中確認顯示方式。
* **說明文**：動作的按鈕固定為「**執行**」，請撰寫與執行這一詞相符的說明文。
* **動作的執行條件**：如果僅限於角色限制，可以通過勾選框輕鬆設置。若要設置其他詳細條件，請使用「[**高級設置**](action.md#na)」。
* **結果動作**：設定按下「執行」後會發生什麼。在圖片的例子中，設定為執行後分配特定的線索。

<figure><img src="../.gitbook/assets/image (55).png" alt=""><figcaption></figcaption></figure>

#### 設定多個結果動作

可以像下圖一樣，設定多個結果動作。

這些動作會在玩家按下「執行」按鈕一次時**作為一系列動作全部執行**。按照從上到下的順序處理，因此如果希望按「分配線索→發送通知」的順序處理，請在此畫面中從上到下排列。

<figure><img src="../.gitbook/assets/image (59).png" alt="" width="515"><figcaption></figcaption></figure>

### 動作的配置（線索/階段中的設定）

動作僅在動作編輯畫面中設定是不會在遊戲中出現的。需要設定創建的動作要配置在哪裡。

可以配置在「線索中」和「基本階段中」兩個地方。這裡說明配置在「線索中」的情況。若要放置在「基本階段中」，請參考[這裡](action.md#akushonnofzugakarideno-1)。

以下示例中，想在「日記」這個線索中放置「查看內容（添加分發第1頁的內容）」這個動作。

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

①從左側菜單移動到「線索」。

②移動到想配置動作的線索的編輯畫面。

③點擊動作欄的「添加」。

④選擇想配置的動作並點擊確定。

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption></figcaption></figure>

若在動作欄中顯示如下，即為成功。

<figure><img src="../.gitbook/assets/image (58).png" alt="" width="563"><figcaption></figcaption></figure>

## 密碼動作的設定

### 在動作編輯畫面中的設定

* **標題**：動作的標題。可以在右側的預覽中確認顯示方式。
* **說明文**：動作的按鈕固定為「**執行**」，請撰寫與執行這一詞相符的說明文。
* **回答**：輸入密碼的正確答案。可以用逗號分隔設定多個表記揺れ等。空白空間會被忽略。
  * 添加回答標籤後，可以設定如輸入「早安」時回應「早安」，輸入「你好」時回應「你好」等根據輸入內容的反應。
* **動作的執行條件**：如果僅限於角色限制，可以通過勾選框輕鬆設置。若要設置其他詳細條件，請使用「[**高級設置**](action.md#na)」。
* **結果動作**：設定按下「執行」後會發生什麼。分為正確輸入密碼的情況和未能正確輸入的情況。
  * **共通標籤**：若設定了多個正確的回答標籤，且它們有共通的結果動作，則在共通標籤中設定。例如，輸入正確的回答後，首先播放效果音，然後根據輸入內容分別執行動作，則可以在共通標籤中設定「效果音」，在回答1以後分別設定各自的結果動作。

<figure><img src="../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

在圖片的例子中，結果動作的內容如下。

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

### 動作的配置（線索/階段中的設定）

動作僅在動作編輯畫面中設定是不會在遊戲中出現的。需要設定創建的動作要配置在哪裡。

可以配置在「線索中」和「基本階段中」兩個地方。這裡說明配置在「基本階段中」的情況。若要放置在「線索中」，請參考[這裡](action.md#akushonnogakarifzudeno)。

以下示例中，想在「討論階段」中配置可以用密碼打開保險箱的動作。

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="563"><figcaption></figcaption></figure>
```plaintext
caption></figure>

①從左側選單移動到「階段」。

②移動到想要放置動作的線索的「基本階段（討論階段等）」。

③點擊階段內容底部的「添加」按鈕。

④選擇「動作」。

⑤勾選相應的動作並點擊「決定」。

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

如果像以下這樣正確添加則成功。

<figure><img src="../.gitbook/assets/image (66).png" alt="" width="563"><figcaption></figcaption></figure>

## 進階篇：執行條件的高級設定

解釋可在簡單動作和密碼動作中使用的高級條件設定。

### 想限制動作的執行次數為1次

如果不設置特定條件，動作在成功後任何人都可以多次執行。

例如，若設定為「執行」時將特定線索分配給執行者，當A先生執行後，B先生再執行時，線索會從A先生手中消失，轉移到B先生手中（因為動作的執行被覆蓋）。

若想避免這種情況，需要設置條件，使動作成功執行後，之後無法再執行。以下以圖片示例設置。

**簡單動作的情況**

<figure><img src="../.gitbook/assets/image (67).png" alt="" width="563"><figcaption></figcaption></figure>

**密碼動作的情況**

若如上所述設定簡單動作，即使在密碼輸入錯誤時也會被判定為「已執行」，之後任何人都無法再嘗試輸入，因此需要稍微改進設定。

<figure><img src="../.gitbook/assets/image (68).png" alt="" width="563"><figcaption></figcaption></figure>

### 其他限制

也可以設置「僅在某個階段進行中時」、「僅在某個通話房間中時」、「僅持有某個線索的人」等條件。

請根據劇本內容靈活運用。
```