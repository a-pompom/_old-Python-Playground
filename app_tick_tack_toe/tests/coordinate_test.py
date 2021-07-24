import pytest

from app_tick_tack_toe.coordinate import Coordinate
from app_tick_tack_toe.exception import InvalidCoordinateException


# 座標バリデーションのテスト
class TestAssignForValid:
    """ 正常系 """

    @pytest.mark.parametrize(('expected', 'raw_input'), [
        ((0, 2), '0,2'), ((1, 0), '    1 ,     0   ')
    ], ids=['with_no_space', 'with_space'])
    def test_valid(self, expected: tuple[int, int], raw_input: str):
        # GIVEN
        sut = Coordinate('')
        expected = (0, 2)

        # WHEN
        sut.assign('0,2')
        actual = (sut.x, sut.y)

        # THEN
        assert actual == expected


class TestAssignForInvalid:
    """ 異常系 """

    @pytest.mark.parametrize('raw_coordinate', [
        '01', '1.2', '0,0,0,1', '-1,-2', '9999,9999'
    ], ids=['no_separator', 'separator_is_not_comma', 'too_many_elements', 'under_min_range', 'over_max_range'])
    def test_invalid(self, raw_coordinate: str):
        # GIVEN
        sut = Coordinate('')

        # WHEN, THEN
        with pytest.raises(InvalidCoordinateException):
            sut.assign(raw_coordinate)
