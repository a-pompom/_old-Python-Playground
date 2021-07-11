# 何がtruthy/falsyか

# falsyなオブジェクト
# None, False, 0, 空のコンテナオブジェクト, __bool__()がFalseを返すオブジェクト,
# __bool__()が未定義で__len__()が0を返すオブジェクト

if not None:
    print('None is falsy.')

if not False:
    print('Flase is falsy')

if not 0:
    print('zero is falsy')

if not '' and not []:
    print('empty container object is falsy')

class BoolFalse:

    def __bool__(self):
        return False

boolFalse = BoolFalse()
if not boolFalse:
    print('object which __bool__ returns False is falsy')

class ZeroLength:

    def __len__(self):
        return 0

zeroLength = ZeroLength()
if not zeroLength:
    print('zero length object is falsy')