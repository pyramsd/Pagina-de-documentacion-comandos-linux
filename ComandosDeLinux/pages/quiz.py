import reflex as rx
import ComandosDeLinux.utils as utils
from ComandosDeLinux.components.quiz_navbar import quiz_navbar
from ComandosDeLinux.views.footer import footer
from ComandosDeLinux.routes import Route
from ComandosDeLinux.components.question_card import question_card
#from ComandosDeLinux.state.state import State
from .results import results

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
        return rx.redirect("/result")
    
    @rx.var
    def percent_score(self):
        return f"{self.score}%"


@rx.page(
        route=Route.QUIZ.value,
        title=utils.quiz_title,
        description=utils.quiz_description,
        meta=utils.quiz_meta,
        on_load=State.onload
)
def quiz() -> rx.Component:
    return rx.center(
        utils.lang(),
        rx.vstack(
            rx.center(
                quiz_navbar(),
                question_card("Preguna 1",
                              "Indica el comando para listar el constenido de un directorio:",
                              "ls", "cd", "dd",
                              lambda answer: State.set_answers(answer, 0, 0),
                              lambda answer: State.set_answers(answer, 0, 1),
                              lambda answer: State.set_answers(answer, 0, 2)),

                question_card("Preguna 2",
                              "Indica el comando para crear un nuevo usuario:",
                              "usermod", "useradd", "groupdel",
                              lambda answer: State.set_answers(answer, 1, 0),
                              lambda answer: State.set_answers(answer, 1, 1),
                              lambda answer: State.set_answers(answer, 1, 2)),
                
                question_card("Preguna 3",
                              "Indica el comando para mostrar los procesos en tiempo real:",
                              "jobs", "top", "kill",
                              lambda answer: State.set_answers(answer, 2, 0),
                              lambda answer: State.set_answers(answer, 2, 1),
                              lambda answer: State.set_answers(answer, 2, 2)),
                
                question_card("Preguna 4",
                              "Gestor de paquetes de sistema basados en debian:",
                              "yum", "apt-get", "pacman",
                              lambda answer: State.set_answers(answer, 3, 0),
                              lambda answer: State.set_answers(answer, 3, 1),
                              lambda answer: State.set_answers(answer, 3, 2)),
                
                question_card("Preguna 5",
                              "Indica el comando que permita conxión remota de forma segura:",
                              "traceroute", "telnet", "ssh",
                              lambda answer: State.set_answers(answer, 4, 0),
                              lambda answer: State.set_answers(answer, 4, 1),
                              lambda answer: State.set_answers(answer, 4, 2)),
                
                question_card("Preguna 6",
                              "Indica el comando para mostrat o configurar el nombre del host:",
                              "iostat", "journalctl", "hostname",
                              lambda answer: State.set_answers(answer, 5, 0),
                              lambda answer: State.set_answers(answer, 5, 1),
                              lambda answer: State.set_answers(answer, 5, 2)),
                
                question_card("Preguna 7",
                              "Indica el comando para modificar los permisos de un archivo",
                              "chmod", "chown", "chgrp",
                              lambda answer: State.set_answers(answer, 6, 0),
                              lambda answer: State.set_answers(answer, 6, 1),
                              lambda answer: State.set_answers(answer, 6, 2)),
                
                question_card("Preguna 8",
                              "Indica el comando para ostrar el espacio en disco disponible y utilizado",
                              "df", "fdisk", "mount",
                              lambda answer: State.set_answers(answer, 7, 0),
                              lambda answer: State.set_answers(answer, 7, 1),
                              lambda answer: State.set_answers(answer, 7, 2)),
                
                question_card("Preguna 9",
                              "Indica el comando para matar un proceso",
                              "kill", "killall", "renice",
                              lambda answer: State.set_answers(answer, 8, 0),
                              lambda answer: State.set_answers(answer, 8, 1),
                              lambda answer: State.set_answers(answer, 8, 2)),
                
                question_card("Preguna 10",
                              "Indica los comandos para mostra información acerca de las interfaces de red",
                              "ifconfig", "ip", "ping",
                              lambda answer: State.set_answers(answer, 9, 0),
                              lambda answer: State.set_answers(answer, 9, 1),
                              lambda answer: State.set_answers(answer, 9, 2)),
                
                question_card("Preguna 11",
                              "Indica el comando para mostrar la tabla de enrutamiento del kernel",
                              "ping", "route", "ifup",
                              lambda answer: State.set_answers(answer, 10, 0),
                              lambda answer: State.set_answers(answer, 10, 1),
                              lambda answer: State.set_answers(answer, 10, 2)),
                
                question_card("Preguna 12",
                              "Indica el comando para programar tareas que se ejecuten en momentos específicos",
                              "jobs", "nice", "cron",
                              lambda answer: State.set_answers(answer, 11, 0),
                              lambda answer: State.set_answers(answer, 11, 1),
                              lambda answer: State.set_answers(answer, 11, 2)),

                rx.hstack(
                    rx.button("Submit", bg="black", color="white", width="6em", padding="1em", on_click=State.submit),
                    rx.spacer(),
                    rx.button("Página principal", on_click=lambda: rx.redirect(Route.INDEX.value))),
                footer(),
                align="center",
                direction="column",
                width="100%",
                spacing="7",
            ),
            width="100%"
        )
    )
@rx.page(route="/result")
def result():
    return results(State)
