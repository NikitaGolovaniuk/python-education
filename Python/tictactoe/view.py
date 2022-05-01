from abc import ABC, abstractmethod


class View(ABC):

    @abstractmethod
    def show_menu(self):
        raise NotImplementedError

    @abstractmethod
    def get_menu_val(self):
        raise NotImplementedError

    @abstractmethod
    def show_log(self):
        raise NotImplementedError

    @abstractmethod
    def get_player_names(self):
        raise NotImplementedError

    @abstractmethod
    def show_board(self, board: object):
        raise NotImplementedError

    @abstractmethod
    def who_won(self, value):
        raise NotImplementedError

    @abstractmethod
    def revanche(self):
        raise NotImplementedError

    @abstractmethod
    def reset_list_turns(self):
        raise NotImplementedError

    @abstractmethod
    def show_score(self, score: list):
        raise NotImplementedError

    def turn(self, param):
        pass
