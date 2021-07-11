class StringBuilder:
    """ 改行などを含む文字列生成を責務に持つ """

    LINE_BREAK = '\n'

    def __init__(self):
        self.text = ''

    def append(self, text: str) -> None:
        """
        文字列を追加

        :param text: 対象文字列
        """
        self.text += text

    def append_line(self, text: str) -> None:
        """
        改行つき文字列を追加

        :param text: 対象文字列
        """
        self.text += f'{text}{self.LINE_BREAK}'
