import random #使用するモジュールのimport

# クラス名の宣言
class Player:
    """
    プレイヤーに関係するクラス
    クラス変数に以下の変数を持つ．
    name:名前
    history:戦歴
    now_hand:今出している手
    win:勝数
    lose:負け数
    draw:引き分け数
    """
    now_hand = 0
    win = 0
    lose = 0
    draw = 0

    """
    初期化の関数．クラスがインスタンス化された時はまずこの関数が呼び出される．
    名前と戦歴を記録するhistoryリストの初期化を行う．

    nに初期値John Doeを設定しているため引数がない場合はJohn Doeになる．
    クラスを呼び出す際にnを指定することでnameが設定される．
    クラス内の変数に値を代入する場合は，
    self.変数名 で指定する．

    e.g.)p1 = Player("Shibayama")
         p2 = Player()

         print(p1.name) -> Shibayama
         print(p2.name) -> John Doe

    """
    def __init__(self,n="John Doe"):
        self.name = n
        self.history = []

    """
    じゃんけんの手をだす関数（メソッド）
    random.randintでランダムで数字を生成
    randintの引数に(0,2)を指定しているため，0から2の数字が生成される
    勝敗を手の数字を計算して，判定するため乱数は数値型の方が望ましい．

    random.choiceを使うのであれば，random.choice("012")ではなく，
    ranodm.choice([0,1,2])とすることで数値型で生成できる．

    for文の時と同じ．文字列なら一文字，リストなら一要素として判定してランダムを作り出すため．
    """
    def show_hand(self):
        r = random.randint(0,2)
        self.now_hand = r

        return r

class Judge:
    """
    勝敗判定，結果の出力をするためのクラス
    """

    """
    クラス内で使用する変数の宣言
    """
    hands = {0:"グー",
             1:"チョキ",
             2:"パー"}

    def __init__(self):
        pass

    """
    勝敗の判定を行うメソッド（関数）


    全員が同じ手，もしくは三種類の手ならばすべてのインスタンスのdrawフィールドに+1
    二種類の場合，勝ちの手をだしたインスタンスのwinフィールドに+1，
    負けの手を出したインスタンスのloseフィールドに+1
    """
    def judge(self,player_list):
        """
        全員分の手を一つのリストに集める．
        """
        hand_list = []
        for player in player_list:
            hand_list.append(player.now_hand)

        """"
        重複を除いた手のリストを作成する．
        重複の削除には，set()を利用している．
        setはリストではなく，集合を作る関数であるため，順番が保存されず，
        ソートされ，リスト[0]から数が小さいものが順番に格納されている．
        e.g.) hand_list = [2,2,1,1,1,0,2,0]
              judgelist -> [0,1,2]
        """
        judge_list = list(set(hand_list))

        """
        judge_listの要素数が1もしくは3．つまり全員が同じ手を出してもしくは，全員が違う手を出した場合に，全Playerのdraw変数に1を加算する．
        そしてhistoryには，出した手と，勝敗結果を記録する．
        """
        if len(judge_list) == 1 or len(judge_list) == 3:
            #全部にdrawを追加する処理
            for player in player_list:
                player.draw += 1
                player.history.append("{0}:draw".format(self.hands[judge_list[0]]))


        elif judge_list[0] == 0 and (judge_list[0] - judge_list[1]) == -1:
            for player in player_list:
                if player.now_hand == 0:
                    player.win += 1
                    player.history.append("{0}:win".format(self.hands[0]))
                elif player.now_hand == 1:
                    player.lose += 1
                    player.history.append("{0}:lose".format(self.hands[1]))

        elif judge_list[0] == 1 and (judge_list[0] - judge_list[1]) == -1:
            for player in player_list:
                if player.now_hand == 1:
                    player.win += 1
                    player.history.append("{0}:win".format(self.hands[1]))
                elif player.now_hand == 2:
                    player.lose += 1
                    player.history.append("{0}:lose".format(self.hands[2]))

        elif (judge_list[0] - judge_list[1]) == -2:
            for player in player_list:
                if player.now_hand == 0:
                    player.lose += 1
                    player.history.append("{0}:lose".format(self.hands[0]))
                elif player.now_hand == 2:
                    player.win += 1
                    player.history.append("{0}:win".format(self.hands[2]))

    def print_score(self,player_list):
        for player in player_list:
            print("|{0}|{1}勝|{2}敗|{3}分|".format(player.name,player.win,player.lose,player.draw))

    def print_history(self,player_list):
        for player in player_list:
            print("|{0}|{1}|".format(player.name,"|".join(player.history)))

def create_player(num):
    player_list = []
    for i in range(num):
        player_list.append(Player("Player{0}".format(i+1)))

    return player_list

if __name__ == '__main__':
    Players = create_player(3)
    Judgeman = Judge()

    for i in range(3):
        for player in Players:
            player.show_hand()

        Judgeman.judge(Players)
    Judgeman.print_score(Players)
    Judgeman.print_history(Players)
