Title: Developers Summit 2019 FUKUOKA
Date: 2019-08-29 00:00
Category: Conference
Tags: conference, devsumi
Author: rkamikaw
Summary: Developers Summit 2019 FUKUOKA についてのまとめ

# Developers Summit 2019 FUKUOKA

## 全体

エンジニアの知的交流を促進することで、世の中がもっと豊かになることを目指して年1回開催される、ITエンジニアのお祭り。

外は大雨。

Wi-Fi は、いつもの通り遅かった。。

プレゼンの来る人の求めるものは何かを意識しながらプレゼンすると良さそうな気がしました。

## スケジュール

* 10:30～11:15 コミュニティがもたらすエンジニアのあり方・働き方とは～Geek Studioを例に～

* 11:30～12:15 Yahoo!天気・災害 天神拠点立ち上げ～新米リーダーの悪戦苦闘～

* 12:30～13:00 GKE を本番環境で利用する際に知っておきたい5つのこと（ランチ）

* 13:15～14:00 スタートアップが導入するべきデザインシステムとは

* 14:15～15:00 モバイルゲーム運営における、認知資源をより有効活用していくための取り組み

* 15:15～16:00 ECにおけるAR・VRの今後

* 16:15～17:00 サーバーレスは世界を救う...データエンジニアリング環境を爆速に構築する技術

* 17:15～18:00 ヤフー、メルカリ、ZOZO 東京の会社の福岡拠点で働くということ

## 内容

### コミュニティがもたらすエンジニアのあり方・働き方とは～Geek Studioを例に～

#### Geek Studio・・？

Geek Studioは副業として、オープンした

元は学生エンジニアが学べる場所を作る目的で設立した

#### 運用している中で発生したこと

* 人的リソースの共有（１人を複数企業で共有）

* 会員同士で会社を設立

#### 知見

コミュニティはあくまで補助的な存在

エンジニアとビジネスサイドが接触する場が少ない

#### Neutrino

エンジニアライクでブロックチェーンに特化している

#### ブロックチェーン

エンジニア不足、研究する余地がある、キラーコンテンツもまだまだ

#### 知見

技術者、スタートアップ、大企業がコラボレーションできる場所作りの重要！！

#### 新しいコミュニティのあり方

ビジネスサイドとのコラボレーションすることによって、エンジニア側にもビジネス側にもメリットがある

#### コミュニティの価値

幅広い知識が必要となるのでアイデアを出す段階で役に立つ

#### コミュニティの活用

勉強会はきっかけにはなるがコスパが悪い

コミュニティに入ることによって、何を得るためにやるのかを考えた上で参加するようにした方が良い

アウトプットの場として使うのも良い

#### 非エンジニアとの関わり方

教え合うスタンスで関わりあうのが大事

エンジニアだけだとニーズがないものを作りがちなので、非エンジニア側の人との協力が必要

#### SIerのようなカンパニー型のエンジニアからアジャイル型エンジニアへ動かすにはどうすれば？

まずはイベントに来て、コミュニティに参加しているエンジニアと関わる

その企業に加わってもらい、関わってもらう

### Yahoo!天気・災害 天神拠点立ち上げ～新米リーダーの悪戦苦闘～

#### プロジェクトの発端

人命にも関わる重要なもので、大阪 - 天神で運用してほしいということで新たに天神拠点の立ち上げを行なった

天神３人 - 大阪3,40人

#### 組織の成功循環モデル

関係の質 -> 思考の質 -> 行動の質 -> 結果の質

の順番で高めていく

#### 天神側の初期の問題

ビデオ朝会をすることでリモートでの開発をしやすくなる

顔がわかる & 質問しやすい

大阪側からは、コストがかかることや朝会の意味を問われる

#### 天神側の中期の問題

やることが増え、優先順位・重要度がわからない

インセプションデッキを使用して優先順位を確認して解決

※インセプションデッキとは

  顧客(ステークホルダー)と開発チーム間で認識を合わせるべき重要な項。

  以下の10項目を使用します。

  * 我われはなぜここにいるのか(Why)

  * エレベーターピッチを作る(Why)

  * パッケージデザインを作る(Why)

  * やらないことリストを作る(Why)

  * 「ご近所さん」を探せ(Why)

  * 解決案を描く(How)

  * 夜も眠れなくなるような問題は何だろう(How)

  * 期間を見極める(How)

  * 何を諦めるのかをはっきりさせる(How)

  * 何がどれだけ必要なのか(How)

#### まとめ

立ち上げ初期は、関係の質をあげる

立ち上げ中期は、業務に慣れ、目標に進むことの難しさを認識

立ち上げ成熟期は、ある程度任せて大丈夫で要所要所でヘルプに入る感じ

### GKE を本番環境で利用する際に知っておきたい5つのこと（ランチ）

#### GKEの特徴

* すぐに開始

* 信頼性とか妖精

* GCPとの統合

#### メンテナンス戦略

ダウンタイムが発生しても良いかをマスター・ノードそれぞれで考える

#### スケーリング設計

#### リリース戦略

Blue/Green - ローリングアップデート - カナリア

#### アクセス権の設定

GCPでの制御とGKEでの制御ができる

#### 通信方式の検討

* 同一クラスター内の通信

* クラスター内部から外部サービスへの通信

* インターネットからクラスターへの通信

* クラスターからインターネットへの通信

### スタートアップが導入するべきデザインシステムとは

#### デザインシステムとは

Uber: https://www.uber.design/case-studies/rebrand-2018

自分たちが何を成し遂げるか見失わないための思考軸

#### フェーズの分け方

* PSF(Ploblem Solution Fit)

  解決に値する課題と、その課題の最適な解決方法を見つけること

* PMF(Product Market Fit)

  顧客を満足させる最適なプロダクトを最適な市場に提供している状態

1. PSF前

2. PMF前

3. PMF後

#### まとめ

図を使って、デザインシステムを考え、思考軸を決めておくとよい。

### モバイルゲーム運営における、認知資源をより有効活用していくための取り組み

#### 認知資源

注意や集中を擁する活動をすることで消費される

脳が使えるリソースを指す概念

* プルリクのレビューを催促する作業 -> Botを作って定期的に未レビューのものを通知する

* メンテナンス作業 -> Googleスプレットシートでスケジュールを作る

* アプリのダウンロードサイズの肥大化することによる申請作業 -> 必要な値を自動で計算し、CDNに予測値を申請することで備える

* ブランチ間マージのためのチェックの手間 -> hubコマンドを使った自動化

### ECにおけるAR・VRの今後

#### LOWYA AR

ARでほぼ実寸の家具を試し置きできます

#### LOWYA AR の 3D モデル

ほぼ実物のような感じでモデル化できる（全く見分けがつかない）

#### LOWYA 360

自分がそこにいるような感じで360度見渡すことができる

https://room360.low-ya.com/

###サーバーレスは世界を救う...データエンジニアリング環境を爆速に構築する技術

#### データエンジニアリング

データサイエンスの結果を活用する

CloudでServerlessを活用したら良い



### ヤフー、メルカリ、ZOZO 東京の会社の福岡拠点で働くということ

#### 