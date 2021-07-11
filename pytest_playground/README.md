# 概要

pytestの使い方を復習したい。

## Hello World

pytestは、`assert`文の真偽値比較によりテストの成否を判定。
jestのようにMatcherを使うのではなく、Pythonの構文で判定していくことになりそう。

### サンプル

```Python
import pytest
from Python.pytest_playground.hello import say_hello

def test_hello():
    actual = say_hello()
    expected = 'Hello pytest'

    assert actual == expected
```

