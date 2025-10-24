import reflex as rx
from ComandosDeLinux.styles.styles import cards_widths

def command_block(command_text, command_code):
    if isinstance(command_code, list):
        return rx.container(
            rx.blockquote(command_text, size="3"),
            *[rx.code_block(code, language="bash", width="100%", font_size="0.8em") for code in command_code],
            width="100%"
        )
    else:
        return rx.container(
            rx.blockquote(command_text, size="3"),
            rx.code_block(command_code, language="bash", width="100%", font_size="0.8em"),
            width="100%"
        )

def custom_card(title: str, commands: list, card_id: str) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.text(title, color_scheme="teal", size="4"),
            *[command_block(text, code) for text, code in commands],
            spacing="1"
        ),
        width=cards_widths,
        variant="surface",
        id=card_id
    )
