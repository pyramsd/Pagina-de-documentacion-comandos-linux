import reflex as rx
from ComandosDeLinux.components.custom_card import custom_card
from ComandosDeLinux.data import card_data

def cards() -> rx.Component:
    return rx.vstack(
        *[custom_card(card_data[card_id]["title"], card_data[card_id]["commands"], card_id) for card_id in card_data],
        top="50px",
        spacing="4",
        width="100%",
        align="center"
    )
