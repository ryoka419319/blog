Title: Chrome Dev Summit 2018 Day2
Date: 2018-11-13 00:00
Category: Conference
Tags: conference, google, chrome
Author: rkamikaw
Summary: Chrome Dev Summit 2018 Day2 についてのまとめ

# Chrome Dev Summit Day2

## 8:00~ Registration and Breakfast

１日目に参加登録を行ったので、２日目は、朝食だけ食べて、
Keynote を見に行きました。

## 10:00~ Day 2 Keynote

![Web Stack](img_chromedevsummitday2/chrome_dev_summit_1.png)
Web Primitives - DOM, Fetch API, Service Worker

Build-in modules - 高水準 API(Virtual Scroll, カルーセル)

Frameworks - React, Angular, Polymer, Next.js, Sapper

Web Components - 日付ピッカー,タブ,カルーセル

Web Framework によって、速度が遅くなることもあります。

### React

![React](img_chromedevsummitday2/chrome_dev_summit_3.png)

React は、レンダリングを小さなチャンクに分けて、処理を行います。

なので、大きなアップデートがあっても、長い時間ロックすることなく、
処理していきます。

### Angular

![Angular](img_chromedevsummitday2/chrome_dev_summit_4.png)

Angular は、デフォルトでパフォーマンスバジェットに対応しました。

### Vue

![Vue](img_chromedevsummitday2/chrome_dev_summit_5.png)

Vue は、モダンなコードをモダンなブラウザに提供します。

また、プリロード、プリフェッチをデフォルトで行います。

### Polymer

![Polymer](img_chromedevsummitday2/chrome_dev_summit_6.png)

Firefox にも対応したため、ネイティブ Web コンポーネントに対応しました。

### Svelte

![Svelte](img_chromedevsummitday2/chrome_dev_summit_8.png)

Svelte は、すでに高速に動作します。

[Hacker News](https://news.ycombinator.com/) のアプリは、20 KB 以下で動作します。

### AMP

![AMP](img_chromedevsummitday2/chrome_dev_summit_10.png)

Brotil 圧縮アルゴリズムにより、JS サイズを 20% 削減しました。

### Ember

![Ember](img_chromedevsummitday2/chrome_dev_summit_9.png)

jQuery をデフォルトから削除して、バンドルサイズを 20% 削減しました。

### ディスプレイロック

これは、DOM セクションをロックし、OK を出すまで、
レンダリングなどは行わないようにします。

ただし、真っ白な画面が表示されるだけが長く続くと、
ユーザは、何が起こっているのか分かりません。

クロスオリジンの場合には、解決策がありません。

そこで Portals を使用します。

Portals は、高度なページ遷移を行います。

Feature Policies

「レポートオンリーモード」「強制モード」があります。

そこで以下の項目をチェックします。

* 同期 XHR

* 最適化されていない画像

* 画像のサイズオーバー

* 圧縮していないメディア

### インスタントローディング

ユーザがクリックする前に読み込む必要があります。

これを WebPackaging によって解決します。

WebPackaging は、
証明書と一緒にドキュメントがあり、
誰でも運ぶことができ（どの CDN や BitTorrent でも）、
ブラウザは、それを信用して、表示します。

### Scheduling API

もし、タスクを小さく分割しているなら、ブラウザと連携して、処理を行います。

### その他の Animation API

Web Animation API は、Safari Preview でも対応されます。

また、CSS アニメーションは、どのブラウザでも対応されています。

ただ、現在のアニメーションは、時間軸でしか動作できません。

### Animation worklets
Animation worklets では、スクロールによってアニメーションすることもできます。

### Virtual Scroller

![Virtual Scroller](img_chromedevsummitday2/chrome_dev_summit_11.png)

無限スクローリングでは、画像のようになります。

UITableView が Web にも対応されます。

## 10:30~ Feature Policy & the Well-Lit Path for Web Development

### Feature Policy

これは、あなたとブラウザとの契約のようなものです。

![Unoptimized images](img_chromedevsummitday2/chrome_dev_summit_12.png)

Feature policy を ON にすると、最適化されていないイメージは、ブロックされます。

![How does it work](img_chromedevsummitday2/chrome_dev_summit_13.png)

レスポンスとともにポリシーを送付して、ブラウザをそれを認識します。

Feature policy を設定するには、まずレスポンスヘッダに以下を追加します。

```text
# 元になるポリシーがない
Feature-Policy: oversized-images 'none'

# 最適化されていない写真は、キャッチされます。
Feature-Policy: oversized-images https://cdn.photos.com
```

または、DOM 属性でも指定ができます。

```html
<iframe allow="autoplay" src="...">
```

Feature Policy は、コードが大きくなる前に組み込んだ方が良いです。

![Reporting API](img_chromedevsummitday2/chrome_dev_summit_14.png
)

以下のようにして、Reporting API を実装できます。

![Reporting Observer](img_chromedevsummitday2/chrome_dev_summit_15.png
)

![Sample Report](img_chromedevsummitday2/chrome_dev_summit_16.png
)

このような形でレポートしてくれます。

レスポンスヘッダへのレポートは、以下のように指定します。

![Report to header](img_chromedevsummitday2/chrome_dev_summit_17.png
)

Contents Security Policy は、レポート API と統合します。

![CSP](img_chromedevsummitday2/chrome_dev_summit_18.png
)

![Support](img_chromedevsummitday2/chrome_dev_summit_19.png
)

Feature Policy とレポート API は、Chrome には、入っています。

Firefox では、Feature Policy を実装中です。

Safari では、iframe の Allow 属性は、対応しています。

Chrome では、簡単に ON/OFF 切り替えができるように
[Feature Policy Tester DevTools Extension](https://chrome.google.com/webstore/detail/feature-policy-tester-dev/pchamnkhkeokbpahnocjaeednpbpacop) という拡張機能を作っています。

## 11:00~ Break

## 11:30~ virtual-scroller: Let there be less (DOM)

より高速化を行うために virtual-scroller を紹介します。

![virtual-scroller](img_chromedevsummitday2/chrome_dev_summit_1.gif)

### レンダリング

n = 5 であれば、問題なく動きます。

![virtual-scroller](img_chromedevsummitday2/chrome_dev_summit_2.gif)

n = 50 になると、少し遅くなります。

![virtual-scroller](img_chromedevsummitday2/chrome_dev_summit_3.gif)

これが、n = 500 になるとかなり目立ちます。

![virtual-scroller](img_chromedevsummitday2/chrome_dev_summit_4.gif)

n = 5000 でも virtual-scroller を使用すると、
目立たず、処理を行うことができます。

![virtual-scroller](img_chromedevsummitday2/chrome_dev_summit_5.gif)

### 読み込み時間

![virtual-scroller loading](img_chromedevsummitday2/chrome_dev_summit_20.png
)
読み込み時間も virtual-scroller を使うことで
7s → 3s に短縮可能です。

### スクロール

スクロールは、GPU によって処理されます。

### 実装方法

```html
<script type="module">
    import 'std:virtual-scroller';

    const scroller = document.querySelector('virtual-scroller');

    scroller.updateElement = (el, contact, idx) => el.src = contact.image;

    await function getData() {
        const resp = await fetch('../contacts.json');
        scroller.itemSource = await resp.json();
    }

    getData();
</script>

<virtual-scroller>
    <template>
        <img height="73" width="73" />
    </template>
</virtual-scroller>
```

## 12:00~ A Quest to Guarantee Responsiveness: Scheduling On and Off the Main Thread

JS をスムーズに動かすためには、以下のガイドラインに沿った実装が必要です。

* 10ms 以内に入力ができること

* 16ms 以内にレンダリングを行うこと（出来れば、10ms 以内）

* 100ms 以内でインタラクティブな結果を返すこと

### 対策

* 単純に処理を減らす

* ブロッキングを避けるため、処理を分割する

* 分割した処理に優先度をつける

### 実装

例えば、Google Map では、以下のように実装しています。

![実装](img_chromedevsummitday2/chrome_dev_summit_21.png
)

ユーザのアクションが行われると、そちらを優先して処理を行うようにしています。

### Task Worklet

![Task Worklet](img_chromedevsummitday2/chrome_dev_summit_22.png
)

別スレッドで動作させることができるため、処理をシームレスに行うことができます。

![worker](img_chromedevsummitday2/chrome_dev_summit_23.png
)

Worker は、レンダリングをスムーズに出来ますが、インプットを犠牲にするかもしれないです。

## 12:30~ Architecting Web Apps - Lights, Camera, Action!

### Actor Model

![Actor Model](img_chromedevsummitday2/chrome_dev_summit_24.png
)

preact を使うとこのようになります。

![preact](img_chromedevsummitday2/chrome_dev_summit_25.png
)

UI 以外は、メインスレッドで動作するべきではないです。

## 13:00~ Lunch

## 14:30~ From Low Friction to Zero Friction with Web Packaging and Portals

AMP には、3つのレイヤーがあります。

![AMP](img_chromedevsummitday2/chrome_dev_summit_26.png
)

Web 体験の摩擦を 0 にするために Web Packaging と Portals を提案しています。

### Web Packaging

![Web Packaging](img_chromedevsummitday2/chrome_dev_summit_27.png
)

サーバが高負荷だったり、処理が遅いと読み込み時間が遅くなったりします。

これを改善するためは、プリフェッチが使えます。

![prefetch](img_chromedevsummitday2/chrome_dev_summit_28.png
)

これは、ユーザがそのあとアクセスしそうなページを
予めキャッシュに読み込んでおき、
いざ、ユーザがアクセスするとキャッシュからデータを返します。

ただ、これは、ユーザが Web サイトに訪問しなくても
ユーザの興味ついてデータを取得されます。

これを解決するために Referrer site をキャッシュしておき、
そのキャッシュを使って、 prefetch する方法があります。

![prefetch](img_chromedevsummitday2/chrome_dev_summit_29.png
)

しかし、これもどのリソースから取得しているかを保証することができません。

これに対応するために Web Packaging を使います。

### Portals

![Portals](img_chromedevsummitday2/chrome_dev_summit_6.gif)

次の話を読む際に読み込みに時間がかかります。

これは、別のドメインへのアクセスを行なっていることが原因です。

![Portals](img_chromedevsummitday2/chrome_dev_summit_7.gif)

Portals を使うとシームレスに次の話を読み込むことができます。

![Portals](img_chromedevsummitday2/chrome_dev_summit_30.png
)

Portals とは、iframe のようなものです。

まず、`<portals>` タグを埋め込み、Activate API を呼び出します。

この API が呼び出されると、`<portals>` がトップレベルページになります。

![Portals](img_chromedevsummitday2/chrome_dev_summit_31.png
)

### Bundle Exchanges

これは、複数のリソースを1つのパッケージにバンドルすることができます。

サービスワーカーがダウンロードし、記事をバンドルとして保存します。

その後、オフラインでも複数のサイトから保存された記事を読むことができます。

![bundle cost](img_chromedevsummitday2/chrome_dev_summit_32.png
)

多くのリソースを読み込む際には、コストがかかります。

webpack は、これらに対応するための一般的な方法ですが、それにも負けないくらいの結果を残しています。

![roadmap](img_chromedevsummitday2/chrome_dev_summit_33.png
)

## 15:00~ State of Houdini

Houdini は、CSS の標準的な取り組みです。

4つのハイレベル API と4つのローレベル API で構成されています。

### ハイレベル API

* Parser API

* Painting API

* Layout API

* Animation Worklet API

### ローレベル API

* Typed OM

* Font Metrics API

* Worklets

* Properties & Values API

### Worklets

Worklets と Workers は、別のものです。

この円がイベントループだとすると、Workers は、こんな感じです。

![Workers](img_chromedevsummitday2/chrome_dev_summit_8.gif)

![Worklets](img_chromedevsummitday2/chrome_dev_summit_9.gif)

Worklets は、イベントループをアタッチメントする感じです。

### CSS Paint API

以下のように実装します。

まず、どの Worklets でも js をロードする必要があります。

```js
// main.js
await CSS.paintWorklets.addModule('my-paint.js');
```

```js
// my-paint.js
registerPaint('my-paint', class {
    paint(ctx, geometry, properties) {
        ctx.fillStyle = 'hotpink';
        ctx.arc(
            geometry.width / 2, geometry.height / 2, // center
            Math.min(geometry.width, geometry.height) / 2, // radius
            0, 2 * Math.PI // full circle
        );
        ctx.fill();
    }
})
```

```html
<!-- index.html -->
<style>
    textarea {
        background-image: paint(my-paint);
    }
</style>
```

この API をサポートしているかどうかは、以下のようにして確認できます。
```html
<style>
    @supports (background-image: paint(something)) {
        /* Paint Worklet is supported */
    }
</style>
```

```js
if ("paintWorklet" in CSS) {
    // Paint Worklet is supported
}
```

### Animation Worklet API

![Animation API](img_chromedevsummitday2/chrome_dev_summit_34.png
)

通常のアニメーション API です。

![Animation Worklet API](img_chromedevsummitday2/chrome_dev_summit_35.png
)

これが、Animation Worklet API です。

以下のようにして使います。

```js
// main.js
await CSS.paintWorklets.addModule('my-animation.js');
```

```js
// my-animation.js
registerAnimator('my-animation', class {
    animate(currentTime, effect) {
        efect.localTime = curentTime;
    }
});
```

Safari は、spring timing 機能を提案しましたが、他のブラウザは、実装していないです。

```html
<style>
.selector {
    /* ... */
    animation-timing-function: spring(/*...*/);
}
</style>
```

バウンズアニメーションを行う際は、以下のようにします。

![bounce](img_chromedevsummitday2/chrome_dev_summit_36.png
)

![worklet animation](img_chromedevsummitday2/chrome_dev_summit_37.png
)

### CSS Layout API

```html
<main style="display: layout(random)">
    <div></div>
    <div></div>
    <!-- ... -->
</main>

<script>
    CSS.layoutWorklet.addModule("random.js");
</script>
```

```js
registerLayout('random', class {
    async layout(children, edges, constraints, styleMap) {
        const childFragments = [];
        for(const child of children) {
            const childFragment = await child.layout();
            childFragment.inlineOffset =
                Math.randon() * contraintSpace.fixedInlineSize;
            childFragment.blockOffset =
                Math.random() * constraintSpace.fixedBlockSize;
            childFragments.push(childFragment);
        }
        return { childFragments };
    }
})
```

## 15:30~ Building Engaging Immersive Experiences

Daydream(VR) ユーザの 83% は、Chome VRBrowser で Web を使用しています。

### WebXR Device API

WebVR API から置き換えられたもので、
AR を使用した Web アプリケーションを作ることができます。

試したい場合は、以下のフラグを立てることで実験できます。

* chrome://flags/#webxr

* chrome://flags/#webxr-hit-test

### WebXR Polyfill

これは、js ライブラリでモバイルデバイスやダンボールの VR でも使えます。

### AR

![AR](img_chromedevsummitday2/chrome_dev_summit_10.gif)

左側のは、ユーザが製品について知ることができます。

右側のは、様々な角度から商品を見ることができます。

### Web 3D 実装方法

three.js - Web 3D のためのヘルパーライブラリです。

![three.js](img_chromedevsummitday2/chrome_dev_summit_11.gif)

![code](img_chromedevsummitday2/chrome_dev_summit_38.png
)

現実世界の座標を仮想世界にロックします。

![code](img_chromedevsummitday2/chrome_dev_summit_39.png
)

![code](img_chromedevsummitday2/chrome_dev_summit_40.png
)

[model-viewer](github.com/GoogleWebComponents/model-viewer) で試すことができます。

* 3D モデルを 3D プログラミングなしで使用できること

* 各ブラウザ・各デバイスに対応すること

* 自動で改善していくこと

![gitf](img_chromedevsummitday2/chrome_dev_summit_41.png
)

![gitf](img_chromedevsummitday2/chrome_dev_summit_42.png
)

![gitf](img_chromedevsummitday2/chrome_dev_summit_43.png
)

## 16:00~ Break

## 16:30~ Using WebAssembly and Threads

WebAssembly は、Web の新しい言語で JS のロジックを書くことができます。
（ただし、完全に書き換えられるわけではないです。）

C++ などの Web アプリケーションを作成し、WebAssembly にコンパイルします。

また、主要なブラウザでは、サポートされています。

WebAssembly には、次の特徴があります。

* 最大限の信頼性の高いパフォーマンスを発揮します。

* 高い移植性

* 高い柔軟性

今までは、コンパイルするためには、部分的に送られてくるデータを取得しきってから、
コンパイルしないといけなかったです。

しかし、Streaming Compilation では、部分的に送られてくるデータを
それぞれ、コンパイルすることができます。

![WebAssembly](img_chromedevsummitday2/chrome_dev_summit_44.png
)

WebAssembly + Emscripten を使うことで、Web でアプリケーションを実行できるようになります。

![scketchUp](img_chromedevsummitday2/chrome_dev_summit_12.gif)

workers は、postMessage() によって、やり取りできます。

## 17:00~ The Virtue of Laziness: Leveraging Incrementality for Faster Web UI

Web Component を使用すると独自の HTML タグを作ることができます。

![Web Component](img_chromedevsummitday2/chrome_dev_summit_45.png
)

lit-html は、HTML テンプレートを JS で書くことができます。

![lit-html](img_chromedevsummitday2/chrome_dev_summit_46.png
)

LitElement は、Web Component を記述するのに便利な方法です。

LitElement は、常に非同期です。

![LitElement](img_chromedevsummitday2/chrome_dev_summit_47.png
)

![component](img_chromedevsummitday2/chrome_dev_summit_13.gif)

コンポーネントツリーが左のようにあるとすると、まず A が実行されます。

すると、B、C がキューに入り、次に B が入ります。

このようにして、実行されていき、全て実行されるとブラウザに表示されます。

```js
const content = fetch('./content.txt');
class DemoElement extends LitElement {
    render() {
        return html`
        <p${content}</p>
        `;
    }
}
```

もし、ネットワークから文字列を取得して、画面へ表示する場合は、
最初は、真っ白な画面が表示されます。

その後、必要なデータの取得ができ次第、画面に表示されます。

もし、この真っ白な画面を表示したくない場合は、`until()` を使用してください。

```js
const content = fetch('./content.txt');
class DemoElement extends LitElement {
    render() {
        return html`
        <p${until(content, 'Loading...')}</p>
        `;
    }
}
```

`runSync` は、データが変更された時だけ、非同期で処理が行われます。

```js
class DemoElement extends LitElement {
    @property()
    filename;
    render() {
        return html`
        <p${fetchContent(this.filename,
        (content) => html`content: ${content}`
        )}
        </p>
        `;
    }
}
```

## 17:30~ Chrome OS: Ready for Web Development

開発に Chrome OS を使用する理由は2つあります。

1. Chrome OS は、PWA にもサポートしていて、最新の技術が集まっていること

2. Android アプリも実行することができること

Chrome OS は、次の2つを特徴としています。

* Simplicity

* Speed

* Security

Chrome OS は、Linux システムのようなもので、

* Debian 安定板を基にしています。

* Web 開発者をターゲットにしています。

    localhost にポートフォワーディングします

    DNS のエイリアスとして、penguin.linux.test があります

* 今後のリリースで USB, GPU, audio, FUSE, file system を共有します。

### Crostini

* 開発者がローカルでする必要があることは、すべてできます。

* 開発中だが、ほとんどの Linux アプリを実行できるようにします。

* エディタ、IDE、DB、ローカルサーバを実行できます。

* apt でインストールできます。

![PWA](img_chromedevsummitday2/chrome_dev_summit_14.gif)

![PWA Supports](img_chromedevsummitday2/chrome_dev_summit_48.png
)

## web.dev の紹介

[Youtube ページ](https://www.youtube.com/watch?v=a6pLdPnDvb8&index=28&list=PLNYkxOF6rcIDjlCx1PcphPpmf43aKOAdF)