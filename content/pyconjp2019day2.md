Title: PyCon JP 2019 Day2
Date: 2019-09-17 00:00
Category: Conference
Tags: conference, python
Author: rkamikaw
Summary: PyCon JP 2019 Day2 についてのまとめ

# PyCon JP 2019 Day2

## 全体

  チェックアウトしないといけなかったので、大きな荷物を持って参加。

  そして、時間の都合上、最後までは見れなかった・・

## スケジュール

* 10:00 - 11:00 キーノート (大展示ホール1F)
* 11:15 - 12:00 Pythonで始めてみよう関数型プログラミング (コンベンションホール梅4F)
* 12:00 - 13:30 ランチ
* 13:30 - 14:00 Python Website is Slow? Think Again! (A+B会議室1F)
* 14:15 - 14:45 入門 自作検索エンジン (A+B会議室1F)
* 14:45 - 15:45 Coffee Break
* 15:45 - 16:15 Getting Started with Asynchronous Python Web Development (コンベンションホール鶯4F)
* 16:15 - 帰福

## 内容

### キーノート

#### Maker Movement

  DIYの延長としてものづくりを行う人がインターネットで繋がることによって怒ったムーブメント。

#### なぜ、組み込み系で Python を使うのか

  * エッジAI, ディープラーニングが必要

  * Web技術の活用が用意

  * 読みやすい・書きやすい（学習コストが低い）

  * 集積回路技術の発達により、構成の・安価なSoCが手に入るようになった

#### MicroPython

  組み込み用に軽量化された Python

  [参考](https://qiita.com/inachi/items/c668a03a03cf04b04f16)

### Pythonで始めてみよう関数型プログラミング

#### 関数型プログラミング

  複数の式を関数の適用によって組み合わせていくプログラミングスタイル。

#### Python での関数型プログラミングの実現方法

  1. 標準機能・標準パッケージで実現

  2. Pythonを生成するコンパイラで実現

  3. AST 変換で実現

  MacroPy3 など・・

  4. 3rd パーティパッケージとして実現

#### 関数合成

  ２つ以上の関数を合成して、１つの関数として提供する。

  Python では、[fn.py](https://github.com/kachayev/fn.py) を使用する。

  ```
  $ pip3 install fn.py
  ```

  ```python
  from fn import F, _
  from operator import add, mul

  # F(f, *args) means partial application
  # same as functools.partial but returns fn.F instance
  assert F(add, 1)(10) == 11

  # F << F means functions composition,
  # so (F(f) << g)(x) == f(g(x))
  f = F(add, 1) << F(mul, 100)
  assert list(map(f, [0, 1, 2])) == [1, 101, 201]
  assert list(map(F() << str << (_ ** 2) << (_ + 1), range(3))) == ["1", "4", "9"]
  ```

#### 永続データ構造

  list を操作する関数の問題点

  * Python の関数は、参照渡しのため、引数で渡したリストを変更すると渡したリストも変更される

  [pyrsistent](https://github.com/tobgu/pyrsistent)

  ```python
  >>> from pyrsistent import v, pvector

  # No mutation of vectors once created, instead they
  # are "evolved" leaving the original untouched
  >>> v1 = v(1, 2, 3)
  >>> v2 = v1.append(4)
  >>> v3 = v2.set(1, 5)
  >>> v1
  pvector([1, 2, 3])
  >>> v2
  pvector([1, 2, 3, 4])
  >>> v3
  pvector([1, 5, 3, 4])

  # Random access and slicing
  >>> v3[1]
  5
  >>> v3[1:3]
  pvector([5, 3])

  # Iteration
  >>> list(x + 1 for x in v3)
  [2, 6, 4, 5]
  >>> pvector(2 * x for x in range(3))
  pvector([0, 2, 4])
  ```

#### 参照透過性

  その式をその式の値に置き換えてもプログラムの振る舞いが変わらないこと。

#### 純粋関数

  引数を受け取って、戻り値を返す以外の副作用を持たない参照透過な関数のこと。

#### パターンマッチ

  構造を持つデータを分解し、構成要素を取り出す。

  構造または分解・取得したデータによって条件分岐を行う。

  [pampy](https://github.com/santinic/pampy)

  ```python
  from pampy import match, _

  input = [1, 2, 3]
  pattern = [1, 2, _]
  action = lambda x: f"it's {x}"

  # pattern にマッチした場合に action が実行される
  match(input, pattern, action)
  ```

#### モナド（Monad）

  モナドは、Haskell で標準ライブラリとして提供され広まった。

  ![モナドとは型クラス](img/img_pyconjp2019day2/1.png)

#### Maybeモナド

  [PythonでMaybeモナドを書いてみる](https://qiita.com/oyenakaw/items/63728d42ac8f716c8d08)

### Python Website is Slow? Think Again!

#### 

### 入門 自作検索エンジン

#### 

### Getting Started with Asynchronous Python Web Development

#### 