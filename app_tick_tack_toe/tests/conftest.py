import sys


def pytest_sessionstart(session):
    """
    前処理 相対importを解決するため、pathへアプリのディレクトリを追加

    """
    sys.path.append('/home/Python/app_tick_tack_toe')
