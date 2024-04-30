import reflex as rx
import ComandosDeLinux.constants as const


def quiz_navbar() -> rx.Component:
    return rx.hstack(
        rx.text(rx.text.strong("Ponte a prueba"),
                width="bold",
                size="4", align="center", color="white"),
        rx.spacer(),
        rx.link(rx.icon("github", size=30), href=const.GITHUB_URL, is_external=True),
        position="sticky",
        padding="1em",
        width="100%",
        align="center",
        z_index="1",
        id="navbar"
    )
