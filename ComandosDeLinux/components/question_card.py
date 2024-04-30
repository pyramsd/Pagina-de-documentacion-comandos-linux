import reflex as rx
from ComandosDeLinux.styles.styles import question_widths

def question_card(head, title, val1, val2, val3, onchange1, onchange2, onchange3) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading(head, size="8"),
            rx.divider(),
            rx.blockquote(title, size="5"),
            rx.spacer(),
            rx.vstack(
                rx.checkbox(
                    rx.text(val1, color_scheme="blue", size="3"),
                    size="3",
                    on_change=onchange1,
                    spacing="3"
                ),
                rx.checkbox(
                    rx.text(val2, color_scheme="blue", size="3"),
                    size="3",
                    on_change=onchange2,
                    spacing="3"
                ),
                rx.checkbox(
                    rx.text(val3, color_scheme="blue", size="3"),
                    size="3",
                    on_change=onchange3,
                    spacing="3"
                )
            )
        ), width=question_widths, variant="surface", style={"background-color":"#282C34"}
    )
