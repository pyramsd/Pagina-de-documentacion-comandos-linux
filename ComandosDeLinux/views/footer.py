import reflex as rx

def footer() -> rx.Component:
    return rx.hstack(
        rx.text("© 2024 Comandos de linux by",
                rx.text.strong(" Sergio Ruiz"),
                width="bold",
                size="2", color="white"),
        padding="1em",
        width="100%",
        align="center",
        justify="center"
    )