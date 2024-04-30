import reflex as rx
import ComandosDeLinux.styles.styles as Style

def footer() -> rx.Component:
    return rx.hstack(
        rx.text("© 2024 ", rx.link("Comandos de linux", href="#navbar", color="white", underline="always"), " by",
                rx.text.strong(" Sergio Ruiz"),
                width="bold",
                size="2", color="white"),
        padding="1em",
        width="100%",
        align="center",
        justify="center"
    )