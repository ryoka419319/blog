Title: Chrome Dev Summit 2018 Day1
Date: 2018-11-12 00:00
Category: Conference
Tags: conference, google, chrome
Author: rkamikaw
Summary: Chrome Dev Summit 2018 Day1 についてのまとめ

# Chrome Dev Summit Day1

## 全体

Chrome Dev Summit は、年に１回、Chrome のエンジニアと Web デベロッパが交わるためのイベントです。

今年でこのイベントは、６回目となり、Chrome は、ちょうど１０年経ちました。

* 期間：2018/11/12,13
* 参加費：無料
* 場所：サンフランシスコ
* URL：[リンク](https://developer.chrome.com/devsummit/)

## 8:00~ Registration and Breakfast

まずはじめに、列に並び、参加登録と朝食を食べました。

どんな感じか分からず、8時半にはついていましたが、

そんなに時間はいらなかったです。

![受付](img_chromedevsummitday1/chrome_dev_summit_29.png)

朝食を食べた後は、やることもなかったので、近くを散策。

![朝食](img_chromedevsummitday1/chrome_dev_summit_28.png)

## 10:00~ Day 1 Keynote

### オープニングビデオ

割とギリギリで入ったので、後ろの方で見ることになりました。

![会場](img_chromedevsummitday1/chrome_dev_summit_30.png)

Chrome ブラウザがリリースされてちょうど１０年ということで

誕生日ケーキを作る映像から始まりました。

内容は、[Chrome の今までを料理になぞらえた物](https://www.youtube.com/watch?v=CbU9GzgS0HY&list=PLNYkxOF6rcIDjlCx1PcphPpmf43aKOAdF&index=14)で、
会場内でもかなり笑いが起きていました。

### Web の今まで

* Chrome comics では、マルチタスク、V8 JavaScript Runtime が使われました。

* Google map では、ajax が使われました。

* ブラウザ上で、360度見渡せるベクターマップ、3Dモデル、衛星画像を表示できるようになりました。

* AutoCAD や figma も使えるようになりました。

* ハイクオリティーなゲーム「CROSSY ROAD 」も開発されました。

* この10年で Chrome のロゴや検索画面のデザインも変わりました。

* autofill （自動でフォーム入力を行う）機能も追加されました。

* 9月には、dino ゲームの birthday バージョンを実施し、2億7千万回プレイされました。

* Chrome のリリース時は、安定性と安全性のためタブごとに別々のプロセスで実行させるようにしました。

* その後この機能は、スタンダードとなりました。

* iframe も同様に別プロセスで実行されます。

* 現在では、HTTP の場合、検索バーに「Not Secure」と表示されるようになりました。

    form フィールドを使用する際に強調表示されます。

    現在では、上位 100 サイトの 80 % が完全に HTTPS になっています。

* 10年を節目に V8 では、100倍 ガベージコレクションできるようになりました。

* V8 は、Web アセンブリにも対応しました。

* これによって、C や C++ も使えるようになり、10 倍読み込み時間が高速にもなりました。

* Chrome は、AV1 という次世代のメディアコーデックに対応しました。

* WebP という画像フォーマットは、30% 他のフォーマットより容量を減らすことができました。

Web にとって、速度改善は欠かせないものであり、
JavaScript は、ダウンロード、コンパイル、実行するのでそのボトルネックにもなります。

それは、Lighthouse というページスピードを分析するツールで見ることができます。

### pinterst の例

pinterest は、Service Worker を使うことで、
悪い環境でも 23 秒から 3.9 秒でページ読み込みをするように短縮することができました。

Web Packaging は、Web ページに署名するための鍵を持ったり、
それを配って安全にアクセスできたりすることができます。

portals（新しい形の iframe）はシームレスに動かすことができます。

### squoosh について

google は、最近の Web 技術を使った [squoosh](https://squoosh.app/) をリリースしました。

簡単にスタイルを変えたりできます。

squoosh は、複雑な操作をスムーズに行うことができます。

### 新しい API

Worklets API は、アニメーションを作り、カスタム描画、カスタムレイアウト が簡単にできます。

Virtual Scroller API は、スムーズなスクロールを実現できます。

Scheduler API は、ブラウザで過ごす時間を制御することができます。

### Twitter の例

Twitter は、Chrome canaly で PWA を実現しています。

さらに新たな API として、WebAuthn に対応しています。

これは、バイオ認証が可能で複数認証に使われます。

### web.dev について

ハイクオリティな Web 体験のため、web.dev beta を開発しました。

スピード, 見つけやすさ, 信頼性 を見ることができます。

チュートリアルとサンプルによって、使い方を学ぶことができます。

### Service Worker

serviceworkies.com では Service Worker について、見ることができます。

### Project VisBug

Project VisBug は、エンジニアとデザイナーが意思疎通するためのツールです。

## 10:30~ Get Down to Business: Why the Web Matters

![投資企業](img_chromedevsummitday1/chrome_dev_summit_32.png)
これらの企業がwebパフォーマンスのために投資を行い、ビジネスに影響を与えました。

### spotify

モバイルweb音楽プレーヤーを使用すれば、より早く企業は成長するのか？

今まで、spotify を知らない人に対して、聞かせたい音楽のリンクを送ると
１曲の音楽を聴くためだけにダウンロードを促されていました。

多くの人が Web 経由でリンクを訪問したが、アプリのダウンロードが必要だったため、諦めるユーザが多かったです。

spotify のユーザは、ブラジル人が多く、その多くが1G以下のスマートフォンを使用していたので、
ブラジルのユーザを対象にテストを行いました。

試しに限られたユーザに対して、ダウンロード前に1曲再生できるようにすると25%再生数が増加しました。

次にテストは、以下のパターンで行ないました。

1. アプリでのみ再生できるパターン

2. webでも再生できるパターン

その後、54%の再生数増加、14%のアクティブユーザの増加、30%のログインユーザの増加しました。

Web での再生ができることでネイティブアプリへのアクセスが減る懸念があったが、
結果は、30%のダウンロード数が増加しました。

#### まとめ

1. 顧客がそのサービスへアクセスする際の障壁を理解する

2. その後、その障壁を取り除くことができるかを理解する

3. 最後にテストを行うことで spotify のように成功するだろう

### STARBUCKS

どのようにして、Web を使用してユーザへの良い経験を届けられるか？

これを考える前にすでにいくつかのことは分かっていました。

1. 月に600万人以上のユーザが iOS のネイティブアプリより Web を使用していました。

2. いろんな場所に店舗を持っているため、いろんなネットワーク環境が存在していました。

それらの環境ですぐにアクセスでき、使用することが求められていました。

これに対応するために Web の様々な機能を使用しました。

* JS,CSSを小さくすること

* キャッシング

* CDN を使って画像は最適化

これらによって、STARBUCKS では、Web アクセスの時間は２倍になりました。

Credential Management API を使用することでサインインをより安全に行うようにしました。

ホームスクリーンへ保存することで素早くアプリを使用することができるようにしました。

PWA 対応しているので、ネイティブアプリのように動作します。

結果として、Web 経由で STARBUCKS のユーザとして登録した数は65%増加しました。

### Pinterest

Pinterest では、3ヶ月で１からアプリを作り直しました。

* 最初のページロード時間を４倍に

* その後のページロードは６倍に

* JSは650kbから200kbに

* CSSは160kbから6kbに

pinterest では、これらの状態を保つために2つの指標を重視しています。

1. JSバンドルサイズ

    ロギングすることで js バンドルサイズを確認できるようにしました。

    そして、アラート付きのダッシュボードを作りました。

    １行のコードから膨大なサイズの js をダウンロードするものもあったので、
    特定のソースからのみダウンロードできるようにホワイトリストを作りました。

2. Pinner Wait Time

    これは、インタラクティブな時間と画像の読み込み時間

そして、pinterestでは、

* 週に 103% のユーザ増加

* 300% のセッション時間の増加

の結果を残しています。

さらにネットワーク帯域の少ない新興国では、

* 週に 300% のユーザ増加

* 見られたピンの数は 600% 増加

という結果になっています。

pinterest では、見られたピンの数が直接収益に影響しているので、これは大きな成果でした。

#### まとめ

* ユーザ数を増やしたいのなら摩擦をなくすこと

* ユーザとの接触を増やしたいのなら workbox によってキャッシュすること

* パフォーマンスを気にするならパフォーマンスバジェットを重要視すること

## 11:00~ Break

## 11:30~ State of the Union for Speed Tooling

あなたが何かをよくしたいなら、まずは測定することが大切です。

指標として、以下を使いました。
![指標](./img_chromedevsummitday1/chrome_dev_summit_1.png)

Lighthouse は、OSS で誰でも使えますが、認証は必要です。

### Lighthouse

Lighthouse は、以下の変更を行いました。

* ランタイム時間の短縮

* スコアの範囲を変更（より厳しくなった）

* プリセット名の変更。Fast 3G → Slow 4G

### Chrome UX Report

これは、メトリックスを Web 上で提供します。

パフォーマンスツールは統合されました。

### PageSpeed Insights

PageSpeed Insights は、今は lighthouse で動いています。

### PageSpeed API

PageSpeed API は、Lighthouse APIに変更しました。

APIについては、[こちら](https://developers.google.com/speed/docs/insights/v5/get-started) を見てください。

#### まとめ

1. 頻繁に測定を行うこと

2. Lighthouse での分析を素早く行うために PageSpeed Insights を使うこと

3. ユーザパフォーマンス観点をまとめるために Chrome UX Report を使う

4. PageSpeed Insights API を使ってパフォーマンスを評価すること

## 12:00~ Speed Essentials: Key Techniques for Fast Websites

画像ファイル、Web フォント、JS がパフォーマンスに重大な影響を与えます。

### 画像ファイルについて

* 適切なフォーマット

* 適切に圧縮を行う

* 表示に適したサイズにすること

* 必要な時のみロードすること

これらを自動でシステム化しておくことが重要です

### Animation GIF について

1.4s のもので 6.8MB になります。

これが、MPEG4では、420kbになります。

なので、例えば、twitter では、Animation GIF をアップロードすると自動的に MPEG に変換しています。

以下のコマンドで変換できます。

```bash
ffmpeg -i dog.gif dog.mp4
```

次に

```html
<img src="dog.gif">
```

から

```html
<video autoplay loop muted playsinline>
    <source src="dog.mp4" type="video/mp4">
</video>
```

に書き換えます。

こうすることで Animation GIF のように見せることができます。

### WebP

![サポート環境](img_chromedevsummitday1/chrome_dev_summit_2.png)

JPEG や PNG  より25~35% 小さいです。

```html
<picture>
    <source type="image/webp" srcset="flower.webp">
    <source type="image/jpeg" srcset="flower.jpg">
    <img src="flower.jpg">
</picture>
```

このようにすることでサポートしているブラウザのみ WebP を使うことができます。

### AV1

１番の特徴は 45~50% 圧縮できるということです。

ただ、まだ新しいので、実用的ではないです。

### 画像ファイルの圧縮について

オススメは、80~85% の品質レベルを試してみることです。

こうすることで、ファイルサイズを 30~40% 減らすことができます。

最も一般的なツールとしては、imagemin があります。

ほとんどのサイトでは、3~5 サイズを用意しています。

サイズ変更するツールは、Sharp と Jimp が有名です。

Sharp は、C/C++ コンパイラのインストールが必要だが、リサイジングは高速です。

複数サイズの画像を用意した場合は、HTML を以下のようにする必要があります

```html
<img srcset="flower-small.jpg 480w, flower-large.jpg 1080w" sizes="50vw" src="flower-large.jpg">
```

※ pxの代わりにwを使います。

### lazy loading

よく使われるツールは、npm パッケージの lazysizes と lozad です。

そして、HTML は、以下のようにします。

```html
<head>
    <script src="lazysizes.min.js" async></script>
</head>
<body>
   <img data-src="flower.jpg" class="lazyload">
</body>
```

現在、Chrome でもネイティブで lazy load を行おうとしています。

```html
<img src="flower.jpg" lazyload="auto">

<img src="flower.jpg" lazyload="on">

<img src="flower.jpg" lazyload="off">
```

### Fonts

まずは、システムフォントを使用して、カスタムフォントのダウンロードが完了したタイミングで
それを表示することをお勧めします。

```css
@font-face {
    font-family: 'Pacifico';
    src: url(...pacifico.woff2) format('woff2');
    font-display: swap; // これを追加するのみ
}
```

### Javascript

まずは、バンドルを分けることを考えます。

```js
import('module')
   .then(module => module.default)
   .then(module => doSomethingCool(module))
```

このようにして、必要なモジュールを必要になったタイミングで読み込むようにします。

Vue.js や Angular、React でもこれらは抽象化されて実装されています。

### preload

```html
<link rel="preload" as="script" href="critical.js">
```

### @babel/preset-envを使う

NewYork Timesで、これは使用されています。

Sapper+rollup を使用してモジュール分割を行なっています。

Coverage タブからバンドルサイズを確認できます。

### webpack bundle analyzer

bundlephobia でライブラリのコストを確認できます。

CI で Lighthouse を動かすことができるので定期的にバンドルサイズを確認することができます。

### ユニクロ

ユニクロは、パフォーマンスの改善を行うことにより以下の結果を得ました。

* 直帰率（初めてサイト内の ページ に訪問した後に、サイト内の他の ページに行くことなく離脱したセッションの割合）が 14% 低下

* 平均滞在時間が31%増加

* セッションあたりの閲覧ページ数が25%増加

## 12:30~ Building Faster, More Resilient Apps with Service Worker: A Caching Strategy Deep Dive

Service Worker は、すべてのブラウザの最新版でサポートされています。

### Service Worker のメリットデメリット

#### メリット

* ネットワークリクエストをスキップすることができます。

* バックグラウンドで更新を探しつつ、レスポンスを返すことができます。

* 毎回、完全なHTMLを読み込まず、一部のみ読み込むことができます。

* 通常、パース、コンパイル、実行するJSコードだが、自動的にバイトコードをキャッシュに格納することができます。

    （これにより、繰り返しアクセスの場合、より早く処理できます。）

#### デメリット

* Service Worker を起動する時間が必要になります。

    ![Service Worker](img_chromedevsummitday1/chrome_dev_summit_3.png)
    Service Worker を使う場合、通常、リクエストを中継する形になります。

    ![Service Worker](img_chromedevsummitday1/chrome_dev_summit_4.png)
    なので、多少の遅延は発生します。

    以下のコードによって、Service Worker のスタートアップタイムを計ることができます。

    ```js
    const entry = performance.getEntriesByName(url)[0];
    const swStartupTime = entry.requestStart - entry.workerStart;
    ```

* キャッシュ読み込みの時間は、常に一定ではないです。

    初めは、キャッシュにデータを取りに行きますが、
    ![Service Worker](img_chromedevsummitday1/chrome_dev_summit_5.png)
    エラーやタイムアウトになると、ネットワークに取りに行きます。
    ![Service Worker](img_chromedevsummitday1/chrome_dev_summit_6.png)

    ![Service Worker](img_chromedevsummitday1/chrome_dev_summit_7.png)
    さらに遅延は、このようになります。

    キャッシュタイムも計ることができます。

    ```js
    const entry = performance.getEntriesByName(url)[0];
    // transferSize が 0 ということは、キャッシュが使用されたということ
    if (entry.transferSize === 0) {
       const cacheTime = entry.responseStart - entry.requestStart;
    }
    ```

    もっと細かく見たい場合は、以下のようにもできます。

    ```js
    const cacheStart = performance.now();
    const response = await caches.match(event.request);
    const cacheEnd = performance.now();
    ```

* 過度なプリキャッシングがネットワーク帯域を奪います。

    これに対応するためには、サービスワーカーをloadまで登録しないことです。

    ```js
    addEventListener('load', () => {
        navigator.serviceWorker.register('sw.js');
    });
    ```

### workbox

Service Worker を実装するためのライブラリです。

ナビゲーションリクエストをスピードアップする3つの方法

* すぐにキャッシュからレスポンスを返します。（その後、更新を確認する）

    ![workbox](img_chromedevsummitday1/chrome_dev_summit_8.png)

* ネットワークが必要な時は、必要なコンテンツのみ取得し、他の部分と結合させます。

    workbox を使用すれば、簡単にこれが実装できます

    ![workbox](img_chromedevsummitday1/chrome_dev_summit_9.png)

* navigation preload を使用することで、ネットワークリクエストとサービスワーカーの移動を並列に行います。

    ![preload](img_chromedevsummitday1/chrome_dev_summit_10.png)
    ![preload](img_chromedevsummitday1/chrome_dev_summit_11.png)

    アプリの現在のストレージ使用量の確認は、以下でできます。
    ![preload](img_chromedevsummitday1/chrome_dev_summit_12.png)

   workbox には、gulp と webpack の両方のキャッシュの更新を行うプラグインがあります。

* 常に Slow 3G を使ってテストしてください。

* アプリケーションによって占められるストレージ量を確認してください。

* save-data モードを使用している場合、積極的なプリキャッシングはしないでください。

* どれくらいキャッシュを使うかは、effectiveType を使って決定してください。

* 必要な場合は、opt-in UX パターンを使ってください。

この Service Worker についても web.dev に記載しているのでそこで学ぶことができます。

![key points](img_chromedevsummitday1/chrome_dev_summit_13.png)

## 13:00~ Lunch

## 14:30~ Smooth Moves: Rendering at the Speed of Right ®

スムーズであることは、アプリと直接つながっているように感じることができます。

46% の人がモバイルエクスペリエンスが中断されたら、以降、そのサイトから購入することがないと答えました。

また、79% の人が使いやすいサイトだと再度訪れて誰かと共有すると答えました。

### パフォーマンスを認識する4つの指標

![RAIL](img_chromedevsummitday1/chrome_dev_summit_14.png)

スムーズなサイトを作るためには、ローエンドのハードウェアで 60FPS 必要です。

### Chrome DevTools

いくつか便利な機能がありますので、ぜひ使ってみてください。

* Rendering パネル

* Layers パネル

* Performance monitor パネル

* Audit パネル（Lighthouse）

ブラウザの要素を描画するには、まず、DOMツリーを作ります。
![DOMツリー作成](img_chromedevsummitday1/chrome_dev_summit_15.png)

次にスタイルの計算を行います。
![スタイルの計算](img_chromedevsummitday1/chrome_dev_summit_16.png)

次にレイアウトを決めます。
![レイアウト](img_chromedevsummitday1/chrome_dev_summit_17.png)

次にペイントします。
![ペイント](img_chromedevsummitday1/chrome_dev_summit_18.png)

その後、それを表示します。
![描画](img_chromedevsummitday1/chrome_dev_summit_19.png)

例えば、div.style.left を変える場合は、かなりのタスクをし直さないといけないですが、
translateX を使うことでそのいくつかは省けます。
![タスク](img_chromedevsummitday1/chrome_dev_summit_20.png)

パフォーマンスに影響するので max-height にアニメーションしないでください。

レイアウト情報が必要なプロパティを読み込むことがレイアウトを変更する前に重要なことです。

送信ボタンを押した後に実際に送信されるまで次のメッセージを送信させないようにするのではなく、
非同期に次々送信できるようにするとより良いです。

![HEART](img_chromedevsummitday1/chrome_dev_summit_21.png)
UI の影響を測定するために役立ちます。

### アプリケーションのパフォーマンスを向上させる方法

1. ブラウザプリミティブを見つけること
    これは、スクロールしている間、スクロールハンドラ内でレイアウト情報を問い合わせる必要があるため、
    コストがかかります。

    ```css
    .avatar {
        position: sticky;
    }
    ```

2. ネイティブスクロールを活用すること

    ```js
    function scrollToEnd() {
       requestIdleCallback(() => {
          scrollView.scrollIntoView({
             behavior: 'smooth',
             block: 'end',
         });
      });
    }
    ```

カルーセルは、以下のように実装できます。
![カルーセル](img_chromedevsummitday1/chrome_dev_summit_22.png)

#### まとめ

![まとめ](img_chromedevsummitday1/chrome_dev_summit_23.png)

* レイアウトのアニメーション化は、避けてください

* DOMアクセスは、同期して読み込んでください

* 楽観的なやり取りをすることを考えてください

## 15:00~ Complex JS-heavy Web Apps, Avoiding the Slow

より簡単に画像ファイルを変換するためのツール([squoosh.app](https://squoosh.app/))を紹介します。

簡単にアップロードして、変換前後の違いをすぐに確認できます。

コマンドラインだと、完了するまで結果は見れないが、GUI だとすぐに結果を見ることができるメリットがあります。

C 言語で WebAssembly を使って作られています。

emscripten は、C++ コードをコンパイルして wasm バイナリで JS ファイルを提供します。

PREACT + webpack

squoosh は、400kb で gzip されています。

squoosh は、2つの worker スレッドを使用しています。

![workerスレッド](img_chromedevsummitday1/chrome_dev_summit_24.png)

こうすることで同時性を実現するのとエンコードを中断することを可能としています。

worker とは、ID を使って、メッセージをやり取りしています。

squoosh も PWA で実装されているので、ホーム画面に保存してみてください。

## 15:30~ Building Modern Web Media Experiences: Picture-in-Picture and AV1

### なぜメディアがWebにとって重要か？

* Chrome では毎日 40000 年分の動画が再生されています。

* 30% が Chrome Desktop で再生されています。

* 15% が Chrome for Android で再生されています。

### Picture-in-Picture

[BBC](https://www.bbc.com/news/world-europe-46340283) も Picture-in-Picture に対応しました。

[Picture-in-Picture](https://developers.google.com/web/updates/2018/10/watch-video-using-picture-in-picture)

### AV1（ビデオコーデック）

AV1 は、その前身である VP9 より 30% 小さくすることができます。

この[デモ](https://storage.googleapis.com/change_type/index.html)で瞬時に AV1-H.264 の変換ができることが見れます。

## 16:00~ Break

## 16:30~ Modern Websites for E-commerce in the Real World

AMPを使って、コマース体験を高速化するテストを行いました。

商品を選択して、カートに入れるまでの処理を 3step → 2step に変更して、
50% のコンバージョンの向上が見られました。

* 組織的な連携

    職務上の枠を超えた賛同は、パフォーマンスイニシアチブの成功の鍵

* 技術的なアプローチ

    長期的なビジョンと短期的な目標

* 測定

    メトリックが共有された、ツールで自動化された、すぐ次のステップへ移れる測定戦略を作る

## 17:00~ Progressive Content Management Systems

現在、Web サイトの 54% が CMS 上に構築されています。

WordPress は、全体の 30% を占めています。

### AMP for WordPress

現在 1.0 RCバージョン

### PWA in WordPress

![PWA in WordPress](img_chromedevsummitday1/chrome_dev_summit_25.png)
これらを実現しようとしています。

### App Shell Model

ネイティブ アプリのように瞬時に、そして確実にユーザーの画面に読み込めるアーキテクチャです。

## 17:30~ Making Modern Web Content Discoverable for Search

Google の検索エンジンは、このようにしてインデックスを付与しています。
![インデックス](img_chromedevsummitday1/chrome_dev_summit_26.png)

![インデックス](img_chromedevsummitday1/chrome_dev_summit_27.png)
Process には、Render という処理があり、
ページのコンテンツを開き、JS を実行し、最終的な HTML を吐き出します。

Google Search では、JS 対応の Web サイトは、Googlebot が処理するまで遅延されます。

なので、最大で1週間かかることもあります。

いくつか便利なツールを紹介します。

1. [モバイルフレンドリーテスト](https://search.google.com/test/mobile-friendly)

    * スクリーンショットを撮る

    * JS のログメッセージを出す

2. [リッチリザルトツール](https://search.google.com/test/rich-results)

    Googlebotは、Chrome v41なので、ES6は、サポートしていない

    Googlebotは、メモリも持っていない（stateless）

### Polyfill.io

dynamic rendering を使うことで確実に Googlebot にインデックスさせることができます。

ただ、dynamic rendering を使うことは、一時的な回避策なので、
これを使わなくても良いように努力しているところです。

## 18:00~ After party

最後にパーティーがありました。
![アフターパーティ](img_chromedevsummitday1/chrome_dev_summit_31.png)

人が多すぎるのと疲れていたので、すぐ帰ってしまいましたが。。