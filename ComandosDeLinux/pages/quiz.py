import reflex as rx
import ComandosDeLinux.utils as utils
from ComandosDeLinux.components.quiz_navbar import quiz_navbar
from ComandosDeLinux.views.footer import footer
from ComandosDeLinux.routes import Route
from ComandosDeLinux.components.question_card import question_card
from ComandosDeLinux.state.state import State
from ComandosDeLinux.data import quiz_data

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
                rx.foreach(
                    quiz_data,
                    lambda item, index: question_card(
                        f"pregunta {index + 1}",
                        item["question"],
                        item["answers"][0],
                        item["answers"][1],
                        item["answers"][2],
                        lambda answer: State.set_answers(answer, index, 0),
                        lambda answer: State.set_answers(answer, index, 1),
                        lambda answer: State.set_answers(answer, index, 2),
                        )),
                        rx.hstack(
                            rx.button("Submit", bg="red", on_click=State.submit),
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
