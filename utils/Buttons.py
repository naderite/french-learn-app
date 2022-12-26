from PyQt5.QtWidgets import QButtonGroup
from utils.SwitchScreen import Scroll


class Group:

    @staticmethod
    def create_groups(widget):
        Group.goto_vocab(widget)
        Group.goto_gram(widget)
        Group.goto_conj(widget)
        Group.return_to_menu_buttons(widget)

    @staticmethod
    def goto_vocab(widget):
        widget.goto_vocab_buttons = QButtonGroup()
        widget.goto_vocab_buttons.addButton(
            widget.gram_menu.ui.btn_to_vocab, 0)
        widget.goto_vocab_buttons.addButton(
            widget.conj_menu.ui.btn_to_vocab, 1)

    @staticmethod
    def goto_gram(widget):
        widget.goto_gram_buttons = QButtonGroup()
        widget.goto_gram_buttons.addButton(widget.vocab_menu.ui.btn_to_gram, 0)
        widget.goto_gram_buttons.addButton(widget.conj_menu.ui.btn_to_gram, 1)

    @staticmethod
    def goto_conj(widget):
        widget.goto_conj_buttons = QButtonGroup()
        widget.goto_conj_buttons.addButton(widget.gram_menu.ui.btn_to_conj, 0)
        widget.goto_conj_buttons.addButton(widget.vocab_menu.ui.btn_to_conj, 1)

    @staticmethod
    def return_to_menu_buttons(widget):
        widget.return_to_menu_buttons = QButtonGroup()
        widget.return_to_menu_buttons.addButton(
            widget.vocab_level.ui.btn_goto_menu, 0)
        widget.return_to_menu_buttons.addButton(
            widget.gram_level.ui.btn_goto_menu, 1)
        widget.return_to_menu_buttons.addButton(
            widget.conj_level.ui.btn_goto_menu, 2)
        widget.return_to_menu_buttons.addButton(
            widget.solution_box.ui.btn_goto_menu, 2)


class Connect:
    @staticmethod
    def connect_all(widget):
        Connect.side_menu(widget)
        Connect.conjugation_grp1_menu(widget)
        Connect.conjugation_grp2_menu(widget)
        Connect.conjugation_grp3_menu(widget)
        Connect.grammar_menu_acc(widget)
        Connect.grammar_menu_nom(widget)
        Connect.vocabulary_menu_adj(widget)
        Connect.vocabulary_menu_vrb(widget)
        Connect.return_buttons(widget)

    @staticmethod
    def side_menu(widget):
        widget.goto_vocab_buttons.buttonClicked.connect(
            lambda: Scroll.vocab_menu(widget))
        widget.goto_gram_buttons.buttonClicked.connect(
            lambda: Scroll.gram_menu(widget))
        widget.goto_conj_buttons.buttonClicked.connect(
            lambda: Scroll.conj_menu(widget))

    @staticmethod
    def vocabulary_menu_adj(widget):
        widget.vocab_menu.ui.btn_adj_lvl0.clicked.connect(
            lambda: Scroll.vocab_lvl(widget, widget.vocab_level, "adj", 0, widget.solution_box))
        widget.vocab_menu.ui.btn_adj_lvl1.clicked.connect(
            lambda: Scroll.vocab_lvl(widget, widget.vocab_level, "adj", 1, widget.solution_box))
        widget.vocab_menu.ui.btn_adj_lvl2.clicked.connect(
            lambda: Scroll.vocab_lvl(widget, widget.vocab_level, "adj", 2, widget.solution_box))
        widget.vocab_menu.ui.btn_adj_lvl3.clicked.connect(
            lambda: Scroll.vocab_lvl(widget, widget.vocab_level, "adj", 3, widget.solution_box))

    @staticmethod
    def vocabulary_menu_vrb(widget):
        widget.vocab_menu.ui.btn_vrb_lvl0.clicked.connect(
            lambda: Scroll.vocab_lvl(widget, widget.vocab_level, "vrb", 0, widget.solution_box))
        widget.vocab_menu.ui.btn_vrb_lvl1.clicked.connect(
            lambda: Scroll.vocab_lvl(widget, widget.vocab_level, "vrb", 1, widget.solution_box))
        widget.vocab_menu.ui.btn_vrb_lvl2.clicked.connect(
            lambda: Scroll.vocab_lvl(widget, widget.vocab_level, "vrb", 2, widget.solution_box))
        widget.vocab_menu.ui.btn_vrb_lvl3.clicked.connect(
            lambda: Scroll.vocab_lvl(widget, widget.vocab_level, "vrb", 3, widget.solution_box))

    @staticmethod
    def grammar_menu_acc(widget):
        widget.gram_menu.ui.btn_acc_lvl0.clicked.connect(
            lambda: Scroll.gram_lvl(widget, widget.gram_level, "acc", 0, widget.solution_box))
        widget.gram_menu.ui.btn_acc_lvl1.clicked.connect(
            lambda: Scroll.gram_lvl(widget, widget.gram_level, "acc", 1, widget.solution_box))
        widget.gram_menu.ui.btn_acc_lvl2.clicked.connect(
            lambda: Scroll.gram_lvl(widget, widget.gram_level, "acc", 2, widget.solution_box))
        widget.gram_menu.ui.btn_acc_lvl3.clicked.connect(
            lambda: Scroll.gram_lvl(widget, widget.gram_level, "acc", 3, widget.solution_box))

    @staticmethod
    def grammar_menu_nom(widget):
        widget.gram_menu.ui.btn_nom_lvl0.clicked.connect(
            lambda: Scroll.gram_lvl(widget, widget.gram_level, "nom", 0, widget.solution_box))
        widget.gram_menu.ui.btn_nom_lvl1.clicked.connect(
            lambda: Scroll.gram_lvl(widget, widget.gram_level, "nom", 1, widget.solution_box))
        widget.gram_menu.ui.btn_nom_lvl2.clicked.connect(
            lambda: Scroll.gram_lvl(widget, widget.gram_level, "nom", 2, widget.solution_box))
        widget.gram_menu.ui.btn_nom_lvl3.clicked.connect(
            lambda: Scroll.gram_lvl(widget, widget.gram_level, "nom", 3, widget.solution_box))

    @staticmethod
    def conjugation_grp1_menu(widget):

        widget.conj_menu.ui.btn_gr1_pr.clicked.connect(
            lambda: Scroll.conj_lvl(widget, widget.conj_level, "present", 0, widget.solution_box))
        widget.conj_menu.ui.btn_gr1_fu.clicked.connect(
            lambda: Scroll.conj_lvl(widget, widget.conj_level, "future", 0, widget.solution_box))
        widget.conj_menu.ui.btn_gr1_im.clicked.connect(
            lambda: Scroll.conj_lvl(widget, widget.conj_level, "imparfait", 0, widget.solution_box))
        widget.conj_menu.ui.btn_gr1_ps.clicked.connect(
            lambda: Scroll.conj_lvl(widget, widget.conj_level, "passe simple", 0, widget.solution_box))
        widget.conj_menu.ui.btn_gr1_pc.clicked.connect(
            lambda: Scroll.conj_lvl(widget, widget.conj_level, "passe compose", 0, widget.solution_box))

    @staticmethod
    def conjugation_grp2_menu(widget):

        widget.conj_menu.ui.btn_gr2_pr.clicked.connect(
            lambda: Scroll.conj_lvl(widget, widget.conj_level, "present", 1, widget.solution_box))
        widget.conj_menu.ui.btn_gr2_fu.clicked.connect(
            lambda: Scroll.conj_lvl(widget, widget.conj_level, "future", 1, widget.solution_box))
        widget.conj_menu.ui.btn_gr2_im.clicked.connect(
            lambda: Scroll.conj_lvl(widget, widget.conj_level, "imparfait", 1, widget.solution_box))
        widget.conj_menu.ui.btn_gr2_ps.clicked.connect(
            lambda: Scroll.conj_lvl(widget, widget.conj_level, "passe simple", 1, widget.solution_box))
        widget.conj_menu.ui.btn_gr2_pc.clicked.connect(
            lambda: Scroll.conj_lvl(widget, widget.conj_level, "passe compose", 1, widget.solution_box))

    @staticmethod
    def conjugation_grp3_menu(widget):

        widget.conj_menu.ui.btn_gr3_pr.clicked.connect(
            lambda: Scroll.conj_lvl(widget, widget.conj_level, "present", 2, widget.solution_box))
        widget.conj_menu.ui.btn_gr3_fu.clicked.connect(
            lambda: Scroll.conj_lvl(widget, widget.conj_level, "future", 2, widget.solution_box))
        widget.conj_menu.ui.btn_gr3_im.clicked.connect(
            lambda: Scroll.conj_lvl(widget, widget.conj_level, "imparfait", 2, widget.solution_box))
        widget.conj_menu.ui.btn_gr3_ps.clicked.connect(
            lambda: Scroll.conj_lvl(widget, widget.conj_level, "passe simple", 2, widget.solution_box))
        widget.conj_menu.ui.btn_gr3_pc.clicked.connect(
            lambda: Scroll.conj_lvl(widget, widget.conj_level, "passe compose", 2, widget.solution_box))

    @staticmethod
    def return_buttons(widget):
        widget.return_to_menu_buttons.buttonClicked.connect(
            lambda: Scroll.main_menu(widget, widget.currentIndex() - 3, widget.solution_box))
