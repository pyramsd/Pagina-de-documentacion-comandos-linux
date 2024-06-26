import reflex as rx
import ComandosDeLinux.constants as const


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(rx.text.strong("Comandos de linux"),
                width="bold",
                size="4", align="center", color="white"),
        rx.spacer(),
        rx.flex(
                rx.link(rx.icon("github", size=30), href=const.GITHUB_URL, is_external=True),
                rx.link(rx.icon("instagram", size=30), href=const.INSTAGRAM_URL, is_external=True),
                direcction="row", spacing="3"),
        position="sticky",
        padding="1em",
        width="100%",
        align="center",
        z_index="1",
        id="comandosdelinux"
    )
