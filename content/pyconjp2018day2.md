Title: PyCon JP 2018 Day2
Date: 2018-09-25 00:00
Category: Conference
Tags: conference, python
Author: rkamikaw
Summary: PyCon JP 2018 Day2 についてのまとめ

# PyCon JP 2018 Day2

## 10:00~「Pythonでやってみた」：広がるプログラミングの愉しみ
プログラミングの２つの同期
* めんどくさいことを簡単に
* 一体どうなっているんだ？面白そう（好奇心）

PSG(Programmable Sound Generator)

他人が作った音源を使うより、自分でも作ってみたい

複雑なものを作るときは、まずは、最小限のものを作るところから始める

pysdl

## 11:15~ niconicoにおけるコンテンツレコメンドの取り組み
spark：分散処理フレームワーク

Jubatus：分散処理フレームワーク -> リアルタイムレコメンダーで使用

レコメンダーコーディネータ -> 各種レコメンダーをまとめる

同じような処理を各種レコメンダーで同じような処理が必要だったことと、管理が複雑だった

influxDB & Grafana を使って、クリック率を可視化

APIサーバには、Tornadeを使っている

kubernatesによるリソース管理

datadog

## 12:00~ ランチ
弁当が配られ、適当な場所で食事

## 13:30~ REST API に疲れたあなたへ贈る GraphQL 入門
スピーカーに好意を持つことで集中力が1.8倍に

AppSync(AWS)を利用することで、簡単に始めることができる

GraphQL -> 取得、変更、購読

**なぜ注目されているのか**
APIの仕様のドキュメント管理が大変

叩き方を理解するのが大変

1ページを表示するのに何個もAPIを叩かないといけない

イベントドリブンに作っていてもサーバとの接続はRequest/Responseの形が残る

**メリット**
* クライアント、サーバ間のI/Fがクリーンになる
* 通信のオーバーヘッドが削減される
* ドキュメント化、理解するのが容易になる

1. 型指定されたスキーマ
```
type Todo {
    id: ID!
    name: String
    description: String
    status: TodoStatus
}
```

* ドキュメント自動生成
* Query の実行環境

2. クライアントからのレスポンス形式の指定
クライアント側で欲しい情報のみの取得が可能になる

3. サブスクリプションを利用したリアルタイム処理
REST の場合、pollingを行なってなるべく早く取得するようにするところ

**ユースケース**
* リアルタイム
* コラボレーション
* ソーシャルメディア

AWS AppSync GraphQL Photo Sample -> 認証・認可のサンプル

## 14:30~ Artisanal Async Adventures
**New one**
```
from typing import *
@dataclass
async def hoge():
await Utils() # Utils は、__await__ を定義済み
```

Web Server を socket を使ってコーディング -> 非同期処理をdemo

`print(f'Connection from {addr})`

`nc localhost 30303`

通常は、１クライアントにしか対応できない（同期処理が行われるため）

`async def server(address)`

async をつけると非同期に処理をする

```
class Foo:
    def __await__(self):
        yield 'something'
```

## 15:45~ Pythonによる異常検知入門
1. 外れ値検知

    平均値を測定し、そこから異常を検知する

2. 変化点検知

    異常値からの距離を測定して検知する

    累積和法

    Change Finder

3. 異常値検知

    変化点検知の発展系

    近郊法

ニューラルネットワークを使った異常検知 -> autoencoder

**Tips**
* アイドリング中などの状態も考慮する
* 季節性を考慮する
* 判定結果へのフィードバックを考慮する


## 16:30~ Django を Zappaで構築してServerless Python のベストプラクティスを探る
Zappa - Chalice(AWS公式) - Serverless Framework(AWS,GCP)

AWSの人 -> 今サービスを作るならサーバレス -> 圧倒的に早くサービス提供をできる

**メリット**
* コスト面
* アプリ改善に注力できる
* より早くデプロイできる

Zappa

Pythonistaにとっては、これが良さそう

djangoデフォルト

## 17:15~ LT
### Would you like to join NOC?
conbu (Wi-Fi)

NOC -> アクセスポイントごとのアクセス量を監視して、コントロール

### ユーザのコードを安全に実行する
QuantX Factory

pythonで株式投資アルゴリズムが作れる

-> ユーザが書いたコードを安全に他者に迷惑をかけずに実行させる

既存のpython sandobox
* PyPy sandobox
* ast module
* Jython

-> pythonのnamespace + docker

importできるモジュールを制限、組み込み関数の制限、etc...

ホワイトリスト・ブラックリスト方式を採用

### diff最小限利で導くZen of Python
OCP(Open/Closed Principal)

-> ソフトウェアのランタイム全体でコスト削減

diffを最小限にすることでこれが達成できる

1. 配列の最後にカンマをつける
2. 早期リターンさせる
3. デコレータでは、条件分岐を隠す

### Python * Investment
有価証券報告がXBRL形式で公開されているので、それをpythonで

すクレイビングして、データ分析

### システム開発素人が深層学習を用いて画像認識で麻雀点数計算をするline botを作った話
kurasを使用

heroku -> アプリ立ち上げに60秒以上で再起動 & 容量にも制限

line bot -> メモリ制限
### ポケモンの役割ベクトルの学習とその分析・可視化
分布仮説

word2vec -> 単語ベクトル化

ポケモンの役割の自動計算
### asyncid + aiohttpで作るWebサービス
asyncio python3.4 library

3.5 > async, awaitが標準実装された

coroutines が簡単に使用できる

Coroutine は、Futureに変換可能

aiohttp

asyncio を使用したhttpクライアント

uWSGI not supported

簡単にハイパフォーマンスなアプリ作成ができる

### PyCon 傾向と対策
タイトルでよく使われた単語などを分析

機械学習+web -> 2019？

入門は敬遠？

2,3年前の内容をブラッシュアップ

## 18:30~ クロージング