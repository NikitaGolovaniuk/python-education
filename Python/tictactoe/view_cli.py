from view import View


class ViewCli(View):
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.turn_list = []

    def show_menu(self):
        print("1.Start\n2.Show log\n3.Clear log\n4.Exit\n")

    def get_menu_val(self):
        return input(': ')

    def get_player_names(self):
        self.player1 = input("type player1 name:\n")
        self.player2 = input("type player2 name:\n")
        return self.player1, self.player2

    def show_log(self):
        output = ''
        with open("games.log", 'r') as f:
            tmp = f.readlines()
        for i in tmp:
            output += i
        print(output)

    def show_board(self, board):
        tmp_str = ''
        tmp_vals = {
            None: '~',
            True: 'X',
            False: 'O',
        }
        for i in range(3):
            for k, j in enumerate(board.get_row(i)):
                if k < 2:
                    tmp_str += f" {tmp_vals[j.val]} |"
                else:
                    tmp_str += f" {tmp_vals[j.val]} "
            if i < 2:
                tmp_str += '\n'
                tmp_str += '-_-_-_-_-_-'
                tmp_str += '\n'
        print(tmp_str)

    def turn(self, player):
        possible_val = range(3)
        if player:
            x = input(f"{self.player1}  x: ")
            y = input(f"{self.player1}  y: ")
        else:
            x = input(f"{self.player2}  x: ")
            y = input(f"{self.player2}  y: ")
        try:
            if int(x) in possible_val and int(y) in possible_val:
                tmp = (x, y)
                if tmp not in self.turn_list:
                    self.turn_list.append(tmp)
                    return *tmp, player
                else:
                    return self.turn(player)
            else:
                return self.turn(player)
        except ValueError:
            return self.turn(player)

    def who_won(self, value):
        if value:
            print(f"{self.player1} WON!")
            return self.player1
        else:
            print(f"{self.player2} WON!")
            return self.player2

    def revanche(self):
        val = input("Play again? y/n : ")
        return True if val == 'y' else False

    def reset_list_turns(self):
        self.turn_list = []

    def show_score(self, score):
        print(f"{self.player1}: {score[0]} || {self.player2}: {score[1]}")
