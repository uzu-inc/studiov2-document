# 토큰

토큰은 조사 토큰으로서의 용도 외에 상태의 ON/OFF 판정, 수치 비교 등 다양한 활용이 가능합니다.

### 조사 토큰 <a href="#investigation" id="investigation"></a>

단서를 얻을 때 소비하는 토큰으로하는 가장 일반적인 사용법입니다.

#### 토큰 만들기 <a href="#add" id="add"></a>

1. 토큰 편집 화면에서 '토큰 만들기'를 누릅니다(두 번째 이후에는 오른쪽 상단의 '토큰 추가'에서)
2. 설문조사 토큰 등 이름을 입력하고 아이콘의 모양과 색상을 선택합니다.
3. 배포 조건 추가를 누릅니다.
4. 토큰을 배포하고 싶은 단계, 배포할 수를 설정합니다.<br>

<figure><img src="../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>



#### 더미에서 토큰 소비 설정 <a href="#deck" id="deck"></a>

1. 더미 편집 화면에서 '소비 토큰 추가'를 누릅니다.
2. 소비 토큰 필드에 방금 만든 토큰을 설정하여 소비 수를 결정합니다.
3. 「소비수와 소지수를 표시」는, 앱으로 더미 조사를 실행하는 화면에서의 표시의 ON/OFF를 가리킵니다(ON상태를 기본으로 하시면 좋습니다).

### 아이콘 및 컬러 테마 변경 <a href="#change" id="change"></a>

아이콘이나 컬러 테마 등 상태의 ON/OFF를 토큰의 개수에 묶는 사용법입니다.

예를 들어, 다음과 같은 변신 스킬을 통합하고 싶습니다.

<img src="https://docs.studio.uzu-app.com/~gitbook/image?url=https%3A%2F%2F1279302283-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FgOyErfAjeKrNXFgLBxtx%252Fuploads%252FwkFKKliKwK96cI6ORZuq%252Fimage.png%3Falt%3Dmedia%26token%3D5cc76962-e90c-464e-b5d6-b8f13627ea2e&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=e80170e1&#x26;sv=2" alt="" height="528" width="420">

1. "변신 토큰"을 새로 만듭니다.
2. 「변신하는 액션」과 「변신을 취하는 액션」을 [심플 액션](https://docs.studio.uzu-app.com/basic-features/action#shinpuruakushonno) 으로 작성합니다
3. 각 내용으로 "변신 토큰을 리셋하여 +1" "변신 토큰을 리셋하여 0"을 설정합니다.
4.  캐릭터 편집 화면에서 「조건 첨부 아이콘」을 추가해, 조건으로서 「수치 카운트：해당 캐릭터의 변신 토큰이 1과 같다」를 설정합니다(2단계의 변신이 있는 경우는 마찬가지로 「변신 토큰이 2」의 경우도 작성)<br>

    ![](https://docs.studio.uzu-app.com/~gitbook/image?url=https%3A%2F%2F1279302283-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FgOyErfAjeKrNXFgLBxtx%252Fuploads%252FnEzT0J2D5iILOkgXbFKM%252Fimage.png%3Falt%3Dmedia%26token%3D19ce70cd-3bd4-4bac-b3c3-a95576870564\&width=768\&dpr=3\&quality=100\&sign=18ea0a69\&sv=2)

    <img src="https://docs.studio.uzu-app.com/~gitbook/image?url=https%3A%2F%2F1279302283-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FgOyErfAjeKrNXFgLBxtx%252Fuploads%252FGnEFKjzLgPbz0VIv7VIx%252Fimage.png%3Falt%3Dmedia%26token%3Df039fc35-2b91-4c4d-90dd-d2493f0dfee9&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=b3790e8e&#x26;sv=2" alt="" width="375">



위는 아이콘 변경의 예입니다만, 닉네임・컬러 테마・배경 화상에서도 같은 설정이 가능합니다.



![](https://docs.studio.uzu-app.com/~gitbook/image?url=https%3A%2F%2F1279302283-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FgOyErfAjeKrNXFgLBxtx%252Fuploads%252F6F99dPm9k1DJeQPqSGH0%252Fimage.png%3Falt%3Dmedia%26token%3D1a08b169-53d5-41db-ad2b-f40fa87d7af8\&width=768\&dpr=3\&quality=100\&sign=f855b88d\&sv=2)

### 수치 비교 <a href="#count" id="count"></a>

토큰으로 정답수나 투표수를 카운트해, 플레이어 마다의 수치를 비교하는 것과 같은 사용법입니다.

1. 카운트를 위한 새 토큰을 생성합니다(예: "득점")
2. 투표로 응답하는 경우는 「투표로 누군가가(정답 선택지)에 투표했을 때 토큰＋1」과 같이, 액션으로 응답하는 경우는 정답 액션의 결과에 「토큰＋1」과 같이 설정합니다
3. 결과 발표 단계에 각 승리 패턴의 텍스트를 설치합니다.
4. 그 텍스트에 「수치 카운트 토큰 소지수 ●●의 토큰이 ○○보다 큰(미만)」를 설정합니다

텍스트 표시가 아니라 위상 분기에서 사용하고 싶을 때는 같은 설정을 단계 진행 화면에서 수행하십시오.
