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



## 15:00~ State of Houdini

## 15:30~ Building Engaging Immersive Experiences

## 16:00~ Break

## 16:30~ Using WebAssembly and Threads

## 17:00~ The Virtue of Laziness: Leveraging Incrementality for Faster Web UI

## 17:30~ Chrome OS: Ready for Web Development