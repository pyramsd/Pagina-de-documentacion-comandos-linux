import reflex as rx
from ComandosDeLinux.components.cards import cards

def documentation() -> rx.Component:
    return rx.vstack(
        cards()
    )
