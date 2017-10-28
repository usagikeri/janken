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

    now_hand = "0"

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
        self.now_hand = r
        return self.hands[r]


class Judge:
    """
    勝敗判定をするためのクラス
    １対１のじゃんけんバトルだけではなく，複数人にも対応したい．
    処理としてはインスタンスを引数にとり，クラス変数の勝敗の変数を加算することを想定している．
    引数は可変長?

    全員が同じ手，もしくは三種類の手ならばすべてのインスタンスのdrawフィールドに+1
    二種類の場合，勝ちの手をだしたインスタンスのwinフィールドに+1，
    負けの手を出したインスタンスのloseフィールドに+1
    set()を使った重複の削除によって実装する予定
    """
    def __init__(self):
        pass

    """
    hand_listを使って勝敗を判断し，それをplayer_listのフィールドに加算する．
    """
    def judge(self,player_list,hand_list):
        #judge_list = list(set(hand_list))
        player_list[0].name = "fjsla;j"
        """
        if len(judge_list) == 1 or len(judge_list) == 3:
            #全部にdrawを追加する処理
            map(lambda x: x.draw + 1,hand_list)

        elif
        """



if __name__ == '__main__':
    x = 2
    y = []
    J = Judge()

    for i in range(x):
        y.append(Player("Player{}".format(i+1)))


    for i in range(3):
        [y[j].show_hand() for j in range(len(y))]

    [print(y[k].now_hand) for k in range(len(y))]

    J.judge(y,"aaa")

    print(y[0].name)
