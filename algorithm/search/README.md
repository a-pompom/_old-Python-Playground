# 探索

## 線形探索

シンプルな探索。
単純にループでリストを走査するだけなので、検討事項もないか。


## 二分探索

探索範囲を二分しながら、現在要素と探索対象の大小関係から探索方向を決める。
一度にまとめて実装すると混乱しそうなので、前方/後方に分けるか。

無限ループにならないよう、更新条件を意識する。
今回は、小数を一律切り捨て。


## 二分探索木

木構造を探索。
二分探索木は、子の数が2つ以下で、左・親・右の大小関係が「左 < 親 < 右」を
満たすものを指す。

### 単純な探索

二分探索木となっていれば、目的の要素との大小関係をたどるだけで、
目的の要素が得られる。

ここでは、二分探索木の構築・探索を組んでみるか。

#### 二分探索木の構築

TODO 木の構築ロジック

### 深さ優先探索-通りがけ

探索ロジックは、

* 左が空になるまで左の要素を走査
* 空になったら、右を持つ親へたどりつくまで親をさかのぼる
* 右へ移動したら、再度左が空になるまで左の要素を走査
* 探索済みの状態でルートへ戻ってきたら打ち切り

といったところか。
人目では少ない手数で探索できるように見えるが、実装で効率よく組めるか...。
ある程度考えても、上記ロジックぐらいしか思いつかなかったので、一旦組んでみた上で、
効率の良い組み方との考え方の差を吸収したい。