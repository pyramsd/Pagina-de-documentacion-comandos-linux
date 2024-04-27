import reflex as rx

displays=["none", "none", "none", "flex", "flex"]

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(rx.text.strong("Comandos de linux"),
                width="bold",
                size="4", align="center"),
        rx.spacer(),
        rx.flex(rx.link(rx.icon("github", size=30), href="https://github.com/pyramsd", is_external=True),
        rx.link(rx.icon("instagram", size=30), href="https://www.instagram.com/_sergio_ruiz_21_", is_external=True),
        direcction="row", spacing="3"),
        position="sticky",
        padding="1em",
        width="100%",
        align="center",
        z_index="1",
        id="navbar"
    )
