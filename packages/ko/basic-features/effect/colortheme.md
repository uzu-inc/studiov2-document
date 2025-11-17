---
description: 컬러 테마
---

# 컬러 테마

컬러 테마 페이지에서 컬러 테마 설정을 할 수 있습니다.

<figure><img src="../../.gitbook/assets/image (110).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>

테마는 2024/01/12 현재 다음 종류를 사용할 수 있습니다。

<table data-view="cards"><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td><strong>라이트</strong></td><td><img src="../../.gitbook/assets/light (1) (1).png" alt="" data-size="original"></td><td></td></tr><tr><td><strong>다크</strong></td><td><img src="../../.gitbook/assets/dark.png" alt="" data-size="original"></td><td></td></tr><tr><td><strong>마린</strong></td><td><img src="../../.gitbook/assets/marine (1) (1).png" alt="" data-size="original"></td><td></td></tr><tr><td><strong>앤티크</strong></td><td><img src="../../.gitbook/assets/antique.png" alt="" data-size="original"></td><td></td></tr><tr><td><strong>드림</strong></td><td><img src="../../.gitbook/assets/dream.png" alt="" data-size="original"></td><td></td></tr><tr><td><strong>모던</strong></td><td><img src="../../.gitbook/assets/modern.png" alt="" data-size="original"></td><td></td></tr><tr><td><strong>메카니컬</strong></td><td><img src="../../.gitbook/assets/mechanical.png" alt="" data-size="original"></td><td></td></tr><tr><td><strong>노스탤지어</strong></td><td><img src="../../.gitbook/assets/nostalgia.png" alt="" data-size="original"></td><td></td></tr><tr><td><strong>사이버펑크</strong></td><td><img src="../../.gitbook/assets/cyberpunk.png" alt="" data-size="original"></td><td></td></tr></tbody></table>

글자색은 자동으로 최적화되므로, 모드에 맞춰 바꿀 필요는 없습니다。

![](../../images/mode2.png)



### 설정한 시점에 컬러 테마가 변하지 않나요? <a href="#why-not-change" id="why-not-change"></a>

컬러 테마 설정 화면의 위에서부터 순서대로, ‘라이트: 페이즈 1이 시작됨’, ‘다크: 페이즈 2가 시작됨’이라는 테마를 설정했다고 가정합니다.

페이즈 2 시작 시점에 라이트에서 다크로 바뀌기를 바라지만, 이 설정으로는 바뀌지 않습니다。

페이즈 1 → 페이즈 2로 진행된 경우, ‘페이즈 1이 시작됨’이라는 조건은 페이즈 2가 시작되어도 여전히 충족되기 때문입니다. 조건은 더 위에 있는 이미지가 우선되므로, 라이트의 조건이 충족되는 한 계속 다크로 바뀌지 않습니다。



개선 방법* 라이트의 조건을 「페이즈１이 진행 중」으로 바꾼다
* 라이트의 조건을 「페이즈１이 시작했으며 페이즈２가 밟히지 않았다」로 바꾼다