import random #使用するモジュールのimport

# クラス名の宣言
class Player:
    """
    プレイヤーに関係するクラス
    クラス変数に以下の変数を持つ．
    name:名前
    win:勝数
    lose:負け数
    draw:引き分け数
    """

    # クラス内で使用する変数の宣言
    hands = {"0":"グー",
             "1":"チョキ",
             "2":"パー"}

    name = ""

    win = 0
    lose = 0
    draw = 0

    """
    初期化の関数．クラスがインスタンス化された時はまずこの関数が呼び出されます．
    今回はselfとnを引数に渡しています．nに初期値Johnを設定しているため引数がない場合はJohnになる．
    クラスを呼び出す際にnを指定することでnameが設定される．
    クラスの内にの変数に値を代入する場合は，
    self.変数名
    で指定する．
    e.g.)p1 = Player("Shibayama")
         p2 = Player()

         print(p1.name) -> Shibayama
         print(p2.name) -> John
    """
    def __init__(self,n="John"):
        self.name = n

    """
    じゃんけんの手をだす関数（メソッド）
    random.choiceでランダムで一文字生成
    random.choice("012")なので文字型，
    ranodm.choice([0,1,2])なら数値型で生成できる．
    for文の時と同じ．文字列なら一文字，リストなら一要素として判定してランダムを作り出す．

    handはクラス内の変数なのでselfが必要
    rはクラス中の関数の変数なのでselfはいらない
    """
    def show_hand(self):
        r = random.choice("012")

        return self.hands[r]

    class Judge:
        def __init__(self):
            pass

if __name__ == '__main__':
    p1 = Player("A")
    p2 = Player("B")
    p3 = Player()

    print(p1.name)
    print(p2.name)
    print(p3.name)
