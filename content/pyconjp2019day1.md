Title: PyCon JP 2019 Day1
Date: 2019-09-16 00:00
Category: Conference
Tags: conference, python
Author: rkamikaw
Summary: PyCon JP 2019 Day1 についてのまとめ

# PyCon JP 2019 Day1

## 全体

[YouTube](https://www.youtube.com/user/PyConJP/videos?view=2&sort=dd)

ネットワークをコントロールしているところがあって、Wi-Fiもかなり快適。

![Wi-Fi Controll](img_pyconjp2019day1/1.JPG)

## スケジュール

* 09:45 - 10:00 オープニング (大展示ホール1F)
* 10:10 - 11:10 キーノート (大展示ホール1F)
* 11:25 - 12:10 Pythonと便利ガジェット、サービス、ツールを使ってセンシング〜見える化してみよう (小展示ホール2F)
* 12:10 - 13:40 ランチ & LT
* 13:40 - 14:25 Djangoで実践ドメイン駆動設計による実装 (D会議室6F)
* 14:40 - 15:10 Pie Meets Py ― PythonでAndroidアプリをつくろう (コンベンションホール鶯4F)
* 15:10 - 16:00 Coffee Break
* 16:00 - 16:15 Python ウェブアプリケーションのためのプロファイラの実装 (A+B会議室1F)
* 16:30 - 16:45 ListはIteratorですか？ (D会議室6F)
* 17:00 - 17:20 Lightning Talks (大展示ホール1F)
* 17:20 - 17:30 Photo Session1 (大展示ホール1F)
* 17:30 - 18:00 Same Day LT & Day1 Closing (大展示ホール1F)
* 18:00 - パーティ

## 内容

### キーノート

#### Pythonがなぜ流行っているのか

* 初心者でも学びやすい

  Hello world するプログラムだけでも Java と比べて、かなりシンプルになる。

* 需要

  Python開発者の給与はほか言語と比べて高い。

  [参考](https://www.bizreach.co.jp/pressroom/pressrelease/2018/0807.html)

  プログラムについて質問するサイトでの質問数を見てもPythonは、かなり伸びているので、成長していると言える。

  ![Stock Overflowでのpythonの成長率](img_pyconjp2019day1/2.png)

* コミュニティ

  多くのエバンジェリストによって、Pythonのコミュニティが開催されている。

  さらにPyConは、42ヶ国で開催されている。

#### Pythonの求人数

  ![Pythonの求人数](img_pyconjp2019day1/3.JPG)

  Pythonの求人は、かなり増加傾向。

### Pythonと便利ガジェット、サービス、ツールを使ってセンシング〜見える化してみよう

#### IoTシステム構成

  ![システム構成の図（デバイス）](img_pyconjp2019day1/4.png)

  ![システム構成の図（クラウド）](img_pyconjp2019day1/5.png)

  ![システム構成の図（Web）](img_pyconjp2019day1/6.png)

  [SORACOM](https://qiita.com/Junpei_Takagi/items/2db77582890a02c9b03e)

#### センシングとは

  センサー（感知器）などを使用してさまざまな情報を計測・数値化する技術。

  ![センシングの図（計測）](img_pyconjp2019day1/7.png)

  ![センシングの図（監視）](img_pyconjp2019day1/8.png)

  ![センシングの図（通知）](img_pyconjp2019day1/9.png)

#### Grove System

  センサー関連のPythonライブラリ。IoTが手軽にできる。

  [リンク](https://qiita.com/mine820/items/3a4fea28bfeb48c0e24e)

#### LINE Notify

  他のwebサービスと連携させ、そのwebサービス上でアクションが起きたら、

  LINEのチャットに通知を飛ばすことができる。

  [参考](https://liginc.co.jp/358121)

### Djangoで実践ドメイン駆動設計による実装

#### MVC設計の問題点

  ビジネスロジックをどこに書くのか・・（Modelに書くかControllerに書くか）

#### DDD(ドメイン駆動設計)

  1. ドメインの中核となる複雑さと機会に焦点を当てる

  2. ドメイン専門家とソフトウェア専門家のコラボレーションでモデルを探求する

  3. 明示的にそれらのモデルを表現するソフトウェアを書く

  4. 境界付けられたコンテキストの中のユビキタス言語で話す

  [参考](https://little-hands.hatenablog.com/entry/2018/12/10/ddd-architecture)

#### DIコンテナ

  依存関係を増やさないために使用する。

  [python-inject](https://qiita.com/ledmonster/items/3b108be6f0967bfe1093)

### Pie Meets Py ― PythonでAndroidアプリをつくろう

#### Transcript

  Python -> Javascript に変換する AltJS

  typescript で良さそう・・

#### Pyjnius

  Python から Java のコードを触ることができる。

### Python ウェブアプリケーションのためのプロファイラの実装

#### wsgi_lineprof

  行毎のプロファイリングを行うことができる。

  簡単に実装でき、ボトルネックを見つけるのも簡単なのが特徴。

  [参考](https://github.com/ymyzk/wsgi_lineprof)

#### CPythonの評価過程

  1. コードを読み込む

  2. ツリーをパース

  3. ASTに変換

  4. CFGに変換

  5. バイトコードに変換

  6. バイトコードを評価

#### プロファイラを作る

  C のコードを書いて middleware で実装する


[2日目に続く>>](https://ryoka419319.github.io/pycon-jp-2019-day2.html)
