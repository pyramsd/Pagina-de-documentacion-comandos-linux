import reflex as rx
import copy
from typing import Any, List
from ComandosDeLinux.data import quiz_data

class State(rx.State):
    """The app state."""
    default_answers = [[False, False, False], [False, False, False], [False, False, False],
                       [False, False, False], [False, False, False], [False, False, False],
                       [False, False, False], [False, False, False], [False, False, False],
                       [False, False, False], [False, False, False], [False, False, False]]
    answers: List[Any]
    answer_key = [item["correct"] for item in quiz_data]
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

    @rx.var
    def user_answers_str(self) -> list[str]:
        result = []
        for i, answer in enumerate(self.answers):
            answer_indices = [j for j, x in enumerate(answer) if x]
            result.append(", ".join([quiz_data[i]["answers"][j] for j in answer_indices]))
        return result

    @rx.var
    def correct_answers_str(self) -> list[str]:
        result = []
        for i, answer in enumerate(self.answer_key):
            answer_indices = [j for j, x in enumerate(answer) if x]
            result.append(", ".join([quiz_data[i]["answers"][j] for j in answer_indices]))
        return result
