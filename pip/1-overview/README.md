# 概要

本章では、pipとは何か、そして、何のために使うか理解することを目指します。
最初、pipの概要を記し、その後、いわゆるHello Worldに相当するものとして、シンプルなパッケージをインストールし、動かしてみます。

## pipとは

pipは、[公式](https://pip.pypa.io/en/stable/)いわく、

> pip is the package installer for Python

と定義されています。pipはPythonのための「パッケージインストーラ」であるようです。
ここでのパッケージは、モジュールの集まりを指しており、pipにより、標準ライブラリのように
使うことができます。

### pip関連用語

pipに入門する前に、pipとあわせて使われることが多い用語を理解しておきましょう。
用語とあわせて全体像を知ることができれば、pipのイメージがより明確になってくるはずです。

#### PyPA(Python Packaging Authority)

[PyPA](https://www.pypa.io/en/latest/)は、Pythonのパッケージングツールをメンテナンスする団体です。
パッケージングツールには、pipも含まれるので、pipを学ぶときには、何度か目にすることになると思います。

#### PyPI(The Python Package Index)

[PyPI](https://pypi.org/)は、その名の通り、Pythonパッケージのリポジトリの役割を持ちます。
リポジトリは貯蔵庫を意味し、pipで扱うパッケージの取得元を指しています。

---

用語を踏まえた上で再度pipとは何か考えてみましょう。

PyPAによりメンテナンスされている、pipと呼ばれるパッケージインストーラを使うことで、
さまざまなPythonパッケージを利用することができます。
Pythonパッケージの実体は、PyPIと呼ばれるリポジトリに保管されています。


## pipを試す

言葉だけではpipで何ができるのか、見えづらいかもしれません。
手を動かし、パッケージをインストールしてみることで、理解を深めていきましょう。

### sampleprojectのインストール

例として、pipでsampleprojectパッケージをインストールします。
`pip <パッケージ名>`で検索すると、[パッケージ用のPyPIのWebページ](https://pypi.org/project/sampleproject/)が見つかります。

Webページでは、パッケージの説明や、ドキュメント・GitHubなどへのリンク、そして、pipによるインストールコマンドが書かれています。
本章は、pipを試してみるぐらいの理解を目指しているので、各項目の詳細には踏み込まず、インストールコマンドである、
`pip install sampleproject`のみに着目します。

これをpipが導入された環境で実行すれば、パッケージを手に入れることができそうです。

#### いざインストール

インストールコマンドを実行してみます。
その前に、自身の環境にpipが存在するか確認しておきましょう。
[公式ガイド](https://pip.pypa.io/en/stable/user_guide/)に従い、下記のコマンドを実行します。

```bash
$ python3.9 -m pip --version
# 出力例
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.9)
```

---

pipが導入されていることが確認できたので、sampleprojectパッケージを取りに行きます。
インストールコマンドの実行例を下記に示します。

```bash
$ python3.9 -m pip install sampleproject

# 出力例
Collecting sampleproject
  Downloading sampleproject-2.0.0-py3-none-any.whl (4.2 kB)
Collecting peppercorn
  Downloading peppercorn-0.6-py3-none-any.whl (4.8 kB)
Installing collected packages: peppercorn, sampleproject
Successfully installed peppercorn-0.6 sampleproject-2.0.0
```

出力に`Successfully installed`とあるので、どうやらうまくインストールできたようです。

#### 補足: なぜmオプションが必要なのか

pythonコマンドの`-m`オプションについて、少し補足しておきます。
`-m`オプションを付与してPythonインタプリタを呼び出すと、`sys.path`と呼ばれるリストに格納されたパスから
コマンドライン引数に与えられたモジュール名を探しに行ってくれます。

`sys.path`の中身を覗いてみましょう。

```bash
$ python3.9
# ...省略
>>> import sys
# sys.pathを表示
>>> sys.path
# リストの値が探索対象パスとなる
['', '/usr/lib/python39.zip', '/usr/lib/python3.9', '/usr/lib/python3.9/lib-dynload', '/usr/local/lib/python3.9/dist-packages', '/usr/lib/python3/dist-packages']
```

先ほどpipのバージョンを表示したとき、`from /usr/lib/python3/dist-packages/pip`と書かれていました。
`/usr/lib/python3/dist-packages`は、`sys.path`の要素であるため、`-m`オプションを付与することで、
pipモジュールをPythonインタプリタが見つけられるようになりました。

[参考](https://docs.python.org/3/using/cmdline.html#cmdoption-m)


#### 補足: pipコマンドはどう書くべきか

※ 以下の話はUNIX系OSのみを対象としております。

さて、PyPI上で書かれていたコマンドは、`pip install <パッケージ名>`でしたが、実行したのは、
`python -m pip install <パッケージ名>`でした。
どちらもPythonパッケージのための操作であることは共通していますが、何か違いはあるのでしょうか。
両者の違いは、呼び出し元がpipの実行ファイルであるか、指定されたバージョンのPythonインタプリタであるかによるものです。

`pip`コマンドは、実行ファイルなのでshebangが存在します。実行ファイルには、次のように書かれています。

```bash
$ cat /usr/bin/pip3

# shebang python3を指す
#!/usr/bin/python3
# ...省略
```

python3コマンドでは、ディストリビューションがデフォルトとして指定したバージョンのPythonインタプリタを参照します。
Ubuntu20.04の場合は、`Python3.8`が対象となります。
以下がその実行例です。

```bash
$ python3
# 出力例
Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

一方、`python3.9 -m`コマンドの場合は、インタプリタを明示しているため、ディストリビューションのデフォルトによらず、
指定したバージョンでpipモジュールを実行することができます。

---

以上より、明確にバージョンを指定できる、`python3.x -m pip ...`コマンドが推奨されるようになりました。

[参考](https://stackoverflow.com/questions/25749621/whats-the-difference-between-pip-install-and-python-m-pip-install)


### sampleprojectを呼び出す

インストールしたsampleprojectを呼び出す前に、pipでパッケージをインストールすることで何ができるようになるか、復習してみましょう。
パッケージがあれば、他の人がつくってくれた便利な機能を、標準ライブラリと同じような形式で簡単に呼び出せるようになります。

ということは、sampleprojectパッケージも、標準ライブラリのように呼び出すことで、何かの機能が使えるようになるはずです。
まずはお試しということで、REPLでさらっと確認してみましょう。

```bash
$ python3.9
# 出力
Python 3.9.0+ (default, Oct 20 2020, 08:43:38) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

# sampleprojectと対応するsampleモジュールをimport
>>> import sample
# __init__.pyに定義されたmain関数を呼び出し
>>> sample.main()
# main関数のprint文により出力される
Call your main application code here
```

`import sample`により、パッケージを標準ライブラリのようにimportし、パッケージ内に定義された処理を呼び出すことができました。

---

とりあえず書いて動かすことで、本章の目的は達成されました。
しかし、「なぜそう書くことで動いたのか」を理解しておくことも、とても重要です。

以降では、なぜパッケージをimportできたのか・なぜパッケージ名であるsampleprojectでimportしないのか・なぜmain関数が呼び出せると分かったのか、
といった、「なぜ」をもう少し掘り下げてみます。

#### なぜpipでインストールしたパッケージをimportできるのか

まずは、そもそもパッケージがimportできる理由から始めます。
なぜimportできるか、明らかにするには、Pythonがimport文でどこを探しに行くのか知る必要があります。

具体的には、下記の通りです。

* 最初にビルトインモジュール(ex: os, sys)に一致するモジュール名が無いか探索
* 無ければ、sys.pathに存在するディレクトリ内に一致するモジュール名が無いか探索

[参考](https://docs.python.org/3/tutorial/modules.html#the-module-search-path)

pipで新たにインストールしたパッケージはビルトインモジュールではないので、`sys.path`を見れば何かが分かりそうです。
REPLで中身を覗いてみます。

```bash
>>> import sys
>>> sys.path

# import対象ディレクトリの一覧 最初の要素は、Pythonインタプリタを呼び出したディレクトリを指す
['', '/usr/lib/python39.zip', '/usr/lib/python3.9', '/usr/lib/python3.9/lib-dynload', '/usr/local/lib/python3.9/dist-packages', '/usr/lib/python3/dist-packages']
```

いくつかのディレクトリがありますが、これらを全て探すのは骨が折れそうです。
ここで、pipは、[`python -m pip show <パッケージ名>`コマンド](https://pip.pypa.io/en/stable/user_guide/#listing-packages)により、パッケージの詳細情報(実体のパスを含む)を見ることができます。

実行して結果を見てみましょう。

```bash
$ python3.9 -m pip show sampleproject
# 出力例
Name: sampleproject
Version: 2.0.0
Summary: A sample Python project
Home-page: https://github.com/pypa/sampleproject
Author: A. Random Developer
Author-email: author@example.com
License: UNKNOWN
# ここにパッケージの実体がある
Location: /usr/local/lib/python3.9/dist-packages
Requires: peppercorn
Required-by:
```

パッケージ情報より、`/usr/local/lib/python3.9/dist-packages`ディレクトリ配下に存在することが分かりました。
これは、`sys.path`の中に存在するので、importで見つけることができます。

---

以上より、パッケージの実体が`sys.path`の中にあるディレクトリ上に存在するため、import文で見つけることができました。

#### なぜimport文で指定したモジュール名がパッケージ名と一致しないのか

直感的には、インストール時に指定したパッケージ名でimportできることを期待したいところです。
大抵のパッケージはそのようになっているはずですが、sampleprojectは少々勝手が違うようです。

パッケージは、インストールしてしまえば、自分でつくったモジュールと大きな違いはありません。
ですので、importするときの名称は、先ほど確認したパッケージの実体が格納されているディレクトリの名前によって決まります。

ディレクトリ名を確認してみましょう。

```bash
$ ls /usr/local/lib/python3.9/dist-packages/    
# 出力例
peppercorn  peppercorn-0.6.dist-info  sample  sampleproject-2.0.0.dist-info
```

sampleprojectパッケージは、実体が「sampleディレクトリ」に存在するため、import文では、`import sample`のように
書かなければなりませんでした。

---

記述の必要性は分かりましたが、なぜsampleprojectがこのような構成をとったのかまでは記述されていませんでした。
多くのパッケージは、ドキュメントに使い方が書かれていたり、そもそもパッケージ名とモジュール名が一致しているはずです。
ですので、この辺りは、あまり意識することはないかもしれません。

ただ、意識しないことと知らないことは大きく異なるので、頭の片隅にでも置いておくとよいかと思います。

#### なぜ呼び出せる処理がmain関数だと分かるのか

こういったことは、通常はパッケージのドキュメントから読み解いていくものですが、
せっかくの機会なので、パッケージ本体を少し探ってみましょう。

import対象にモジュール名を指定した場合、`__init__.py`に定義された属性が参照できます。
これは、import結果の`dir属性`から確かめることができます。

REPLで確かめてみます。

```bash
$ python3.9

# 出力
Python 3.9.0+ (default, Oct 20 2020, 08:43:38) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sample
# dir関数でモジュールの属性リストを表示
>>> dir(sample)
# リストの末尾にある「main」が呼び出した処理
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'main']
>>> sample.main()
Call your main application code here
```

更に、`__init__.py`の中身も見ておきます。

```bash
$ cat /usr/local/lib/python3.9/dist-packages/sample/__init__.py 
# 出力
def main():
    """Entry point for the application script"""
    print("Call your main application code here")
```

dir属性を参照することで、パッケージの中身がどうなっているか、その一部を知ることができました。
本来はドキュメントからたどっていくのが正道ですが、このようにコードを覗いてみるのも勉強になるので、
気になったパッケージで試してみてください。

---

## まとめ

何度か横道にそれてしまいましたが、pipの概要をなんとなくでも掴めていれば幸いです。
復習のため、「pipは何か」・「pipで何ができるのか」もう一度言葉にしてみましょう。

* pipは、PyPIと呼ばれるリポジトリを起点に、Pythonパッケージを操作するためのツールである
* pipでパッケージをインストールすることで、第三者が開発した機能を、標準ライブラリを使うかのように扱える