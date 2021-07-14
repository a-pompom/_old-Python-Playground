from ..player import Player


def test_initial_state():
    # GIVEN
    expected = Player.CANDIDATE['player1']
    sut = Player()

    # WHEN
    actual = sut.current

    # THEN
    assert actual == expected


def test_toggle_1p_to_2p():
    # GIVEN
    expected = [Player.CANDIDATE['player1'], Player.CANDIDATE['player2'], Player.CANDIDATE['player1'],
                Player.CANDIDATE['player2']]
    sut = Player()

    # WHEN
    actual = [sut.current]
    # プレイヤー切替
    for _ in range(0, 3):
        sut.change()
        actual.append(sut.current)

    # THEN
    assert actual == expected


def test_player_mark():

    # GIVEN
    expected = ['○', '×']
    sut = Player()

    # WHEN
    actual = [sut.get_mark()]
    sut.change()
    actual.append(sut.get_mark())

    # THEN
    assert actual == expected
