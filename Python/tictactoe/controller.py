from view import View
from model import Model
import logging
import logging.config
import yaml


def logger():
    with open('logger_conf.yaml', 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)


class Controller:
    def __init__(self, view: View, model: Model):
        self.score = None
        self.view = view
        self.model = model
        logger()
        self.logger = logging.getLogger(__name__)
        self.player1 = None
        self.player2 = None
        self.actions = {
            '1': self.gameloop,
            '2': self.show_log,
            '3': self.clear_log,
            '4': self.exit,
        }

    def start(self):
        while True:
            self.view.show_menu()
            menu_val = self.view.get_menu_val()
            try:
                self.actions[menu_val]()
            except StopIteration:
                break

    def gameloop(self):
        if self.player1 is None and self.player2 is None:
            names_tupple = self.view.get_player_names()
            self.player1 = names_tupple[0]
            self.player2 = names_tupple[1]
            self.score = [0, 0]
        flag = False
        while not flag:
            self.view.show_score(self.score)
            self.view.show_board(self.model.board)
            turn = (self.view.turn(True) if self.model.turn_count % 2 == 0 else self.view.turn(False))
            self.model.turn(int(turn[0]), int(turn[1]), turn[2])
            flag = self.model.get_game_state()
            if flag:
                tmp = self.view.who_won(self.model.last_turn)
                if tmp == self.player1:
                    self.score[0] += 1
                else:
                    self.score[1] += 1
                self.view.show_board(self.model.board)
                self.logger.debug(f"{tmp} won")
                if self.view.revanche():
                    self.model.board.reset_board()
                    self.view.reset_list_turns()
                    self.gameloop()

    def show_log(self):
        self.view.show_log()

    @staticmethod
    def clear_log():
        with open("games.log", 'w'):
            pass

    def exit(self):
        raise StopIteration
