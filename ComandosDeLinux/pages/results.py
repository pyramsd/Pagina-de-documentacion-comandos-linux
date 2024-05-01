import reflex as rx
from ComandosDeLinux.styles.styles import question_widths
from ComandosDeLinux.routes import Route
import ComandosDeLinux.utils as utils
from ComandosDeLinux.state.state import State as State


def render_answer(State, index):
    return rx.table.row(
        rx.table.cell(index + 1),
        rx.table.cell(
            rx.cond(
                State.answers[index].to_string() == State.answer_key[index].to_string(),
                rx.icon(tag="check", color="green"),
                rx.icon(tag="x", color="red"),
            )
        ),
        rx.table.cell(State.answers[index].to_string()),
        rx.table.cell(State.answer_key[index].to_string()),
    )


def results(State):
    """The results view."""
    return rx.center(
        rx.vstack(
            rx.heading("Resultados:", size="8"),
            rx.divider(),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("#"),
                        rx.table.column_header_cell("Result"),
                        rx.table.column_header_cell("Your Answer"),
                        rx.table.column_header_cell("Correct Answer"),
                    ),
                ),
                rx.table.body(
                    rx.foreach(State.answers, lambda answer, i: render_answer(State, i)),
                ), width=question_widths,
            ), 
            rx.box(rx.link(rx.button("Intentalo otra vez!"), href="/quiz")),
            width=question_widths,
        ),
        padding="1em",
    )

@rx.page(
        route=Route.RESULTS.value,
        title=utils.results_title,
        description=utils.results_description,
        meta=utils.results_meta
)
def result():
    return results(State)
