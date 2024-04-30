import reflex as rx
import copy
from typing import Any, List

class State(rx.State):
    """The app state."""
    default_answers = [[False, False, False], [False, False, False], [False, False, False],
                       [False, False, False], [False, False, False], [False, False, False],
                       [False, False, False], [False, False, False], [False, False, False],
                       [False, False, False], [False, False, False], [False, False, False]]
    answers: List[Any]
    answer_key = [[True, False, False], [False, True, False], [False, True, False],
                  [False, True, False], [False, False, True], [False, False, True],
                  [True, False, False], [True, False, False], [True, False, False],
                  [True, True, False], [False, True, False], [False, False, True]]
    score: int

    def onload(self):
        self.answers = copy.deepcopy(self.default_answers)

    def set_answers(self, answer, index, sub_index=None):
        if sub_index is None:
            self.answers[index] = answer
        else:
            self.answers[index][sub_index] = answer

    def submit(self):
        total, correct = 0, 0
        for i in range(len(self.answers)):
            if self.answers[i] == self.answer_key[i]:
                correct += 1
            total += 1
        self.score = int(correct / total * 100)
        return rx.redirect("/resultados")
