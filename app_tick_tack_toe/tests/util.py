from pytest import FixtureRequest as __FixtureRequest
from typing import Generic, TypeVar

T = TypeVar('T')


class FixtureRequest(__FixtureRequest, Generic[T]):
    param: T


class FixtureParam(Generic[T]):
    """ パラメータフィクスチャの生成を責務に持つ """

    def __init__(self):
        self.params: list[T] = []
        self.ids: list[str] = []

    def append_param(self, param: T):

        self.params.append(param)
        return self

    def append_id(self, test_id: str):

        self.ids.append(test_id)
        return self
