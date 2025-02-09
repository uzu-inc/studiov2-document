---
description: 此頁面為機器翻譯
---

# 背景圖片

## 背景圖片

可以設定遊戲畫面的背景圖片。

#### 預設背景

<figure><img src="../.gitbook/assets/image4-1.webp" alt=""><figcaption></figcaption></figure>

預設背景是在條件式背景未設定或未滿足條件時持續顯示的圖片。

圖片可以通過拖放或點擊來設定。

未設定預設背景的作品會自動套用與色彩主題相符的純色背景。

設定圖片後會如下所示。進行動作確認時，可以確認背景圖片已設定。

背景圖片會自動套用與色彩主題相符的顏色模糊（淺色模式為白色，深色模式為黑色等）。模糊的濃度設定為無論上傳何種背景圖片都能讀取文字。由於作為UZU STUDIO應用程式，文字可讀性是前提，因此無法關閉模糊。

<figure><img src="../.gitbook/assets/image4-2.webp" alt=""><figcaption></figcaption></figure>

<div align="left">

<figure><img src="../.gitbook/assets/image4-3.avif" alt="" width="179"><figcaption></figcaption></figure>

</div>

#### 條件式背景

條件式背景是在滿足任意條件時顯示的背景。

在「條件式背景」處設定圖片後，可以設定條件。

<figure><img src="../.gitbook/assets/image4-4.webp" alt=""><figcaption></figcaption></figure>

滿足條件時會一直顯示該圖片，因此需要注意。例如，若設定為「〇〇階段開始時」，即使該階段結束後，條件式圖片仍會持續顯示。若只想在特定階段設定背景圖片，建議設定為「〇〇階段進行中」。

這次設定為僅在開場顯示條件式圖片。

<figure><img src="../.gitbook/assets/image4-5.webp" alt=""><figcaption></figcaption></figure>

進行動作確認時，可以看到僅在開場階段圖片發生變化。

<div>

<figure><img src="../.gitbook/assets/image4-6.avif" alt="" width="182"><figcaption></figcaption></figure>

 

<figure><img src="../.gitbook/assets/image4-7.avif" alt="" width="176"><figcaption></figcaption></figure>

</div>

條件式背景可以設定多個，但**優先順序是從左開始**。

## 在設定的時間點背景沒有改變嗎？

假設您在背景上傳畫面中，依次設定了「背景A：階段1開始時」「背景B：階段2開始時」。

當階段2開始時，您希望背景能從背景A變為背景B，但這樣的設定下背景並不會改變。

這是因為當階段1進展到階段2時，「階段1開始」這一條件在階段2開始時仍然被滿足。條件優先級是從左到右，因此只要背景A的條件被滿足，背景就不會變為背景B。



改進方法

* 將背景A的條件更改為「階段1進行中」
* 將背景A的條件更改為「階段1開始 並且 階段2尚未進行」
