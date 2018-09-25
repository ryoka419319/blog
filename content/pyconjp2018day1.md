Title: PyCon JP 2018 Day1
Date: 2018-09-25 00:00
Category: Conference
Tags: conference, python
Author: rkamikaw
Summary: PyCon JP 2018 Day1 についてのまとめ

# PyCon JP 2018 Day1
## 全体
1.  会場のwifiが驚くほど早かった（デブサミは、かなり遅い）
2.  python3.7 から type hints 機能が実装された -> python も型付き言語に・・
3.  jupyter notebook のエクスポートは、github pages にあげることで公開できる

## 9:30~ オープニング
イベントのスケジュールや会場、注意事項などの説明

いつでも食事が準備されている

## 10:15~ Argentina in Python: community, dreams, travels and learning
アルゼンチン人のスピーカーのpythonとの関わりについて

アルゼンチンからpython布教活動

スパニッシュイングリッシュでちょっと聞きづらかった

トラブル & ゼルに戻る & 再考

プログラミングに大事なのは、passion, feel, beleave -> your self

## 11:15~ 東大松尾研流 実践的AI人材育成法
deeplearning -> 特徴量抽出を自動で行う点が特徴

柔軟性・汎用性

google translate の性能向上に貢献

CycleGAN -> リアルタイムでしまうまの特徴を抽出して、馬に割り当てることによって、

馬からしまうまが動いているように合成することができる

画像を入力として、それを説明するようなテキストを出力させる

-> その逆も研究されている

AIに力を入れている国 -> カナダ、フランス、中国

DL4US

numpy test system

## 12:00~ ランチ
弁当が配られ、適当な場所で食事

## 12:20~ ジョブフェア
あるブースでZOZOSUITを無料配布していたのでもらえた

（配布終了後は、人がいなくなっていた）

## 13:30~ Applying serverless architecture pattern to distributed data processing
AIOHTTP

fn project -> serverless

need docker bash fn(etc...)

function has no application limits

## 14:30~ Django REST Framework におけるAPI実装プラクティス
### ページネーションは、次の３つ提供されている

1. PageNumberPagination（相対位置指定）

    http://example.com?page=4

2. LimitOffsetPagination（相対位置指定）

    http://example.com?limit=50&offset=50

3. CursorPagination（絶対位置指定）

    http://example.com?cursor=cdfAdf9gFSfsv

### 相対位置指定の問題
* データの矛盾が起こることがある。ページ遷移後のページ作成・削除などによる。
* クエリパフォーマンス。絶対位置指定の場合、スキャンの範囲が相対位置指定と比べて減る。

### 相対位置指定のクエリパフォーマンスに対する改善
1. そのページの取得対象となるidだけを取り出す
2. IN句を使って1で取得したリソースをSELECTで取り出す
    
    -> 2の時に非クラスタインデックスのみのアクセスとなるので、改善する
「カバリングインデックス」

### 絶対位置指定の問題
* 実装が複雑

AnonRateThrottle: 未認証ユーザのリクエスト制限 -> REMOTE_ADDを使用したIPベース

UserRateThrottle：認証済みユーザのリクエスト制限 -> 認証済みユーザの主キーをベース

ScopedRateThrottle: 特定エンドポイントのリクエスト制限

トークン認証
TokenAuthentication

JWT(JSON Web Token)

JWT: {header}.{payload}.{}

header, payload は、base64

JWTの署名アルゴリズム

HMAC, ディジタル署名

### Tips

HATEOAS(Hypertext As The Engine Of Application State)

次に行う行動、URLをAPIのレスポンスデータに含める

メディアタイプの指定
* クエリパラメータに夜指定 -> デフォルトで有効
* Acceptヘッダに夜指定 -> renderer_classes or DEFAULT_RENDERER_CLASSESで設定
* 拡張子に夜指定 -> rest_framework.urlpatterns.format_suffix_patterns を設定

エラーのレスポンスフォーマット

APIのバージョンの指定

## 15:15~ おやつ&写真タイム

## 15:50~ Jupyterで広がるPythonの可能性
jupyter の使い方

pandas

マジックコマンド

%lsmasic

line masic, cell magic

i-pythonsql

snippets menu

jupyter-black

ipywidgets

jupyter notebook でプレゼン

RISE

Hide_code でコード部分を隠す拡張

jinja2

shpinx

nbdiff-web拡張

nbviewer

binder

colaboratory

## 16:30~ Rust と Python
async await

rust -> memory safety, blazingly fast

install -> curl https://sh.rustup.rs -sSf | sh

rustup -> pyenv みたいな

cargo, crates.io -> パッケージマネージャ

memory safety
* Ownership
* Borrowing

Blazingly fast
* minimal runtime
* zero-cost abstraction

pyO3
* Rust(Nightly)

```
$ rustup default nightly
$ cargo new --lib example
$ cd example
```

## 17:15~ クロージング

## 17:30~ LT
Pycon へ転職してみたその本音

多重継承とmixin

テキストマイニングによるツイッター個人アカウントの推定

Why your Django...

医学研究者が深層学習環境の立ち上げの際に苦労した

ブロックチェーン

## 18:00~ パーティ