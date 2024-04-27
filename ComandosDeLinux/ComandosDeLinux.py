import reflex as rx
from ComandosDeLinux.components.navbar import navbar
from ComandosDeLinux.views.header import header
from ComandosDeLinux.views.documentation import documentation
from ComandosDeLinux.views.footer import footer
from ComandosDeLinux.views.menu import menu

class State(rx.State):
    """The app state."""


def content():
    return rx.box(
        rx.heading("Welcome to My App"),
        rx.text("This is the main content of the page."),
    )

@rx.page(
        title="Comandos de linux by Sergio Ruiz",
        description="Documentación de comandos linux para distintos propósitos de desarrollo",
        image="/preview_img.png"
)
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.center(
                rx.fragment(navbar(), rx.container(header(), max_width="60em")),
                documentation(),
                footer(),
                align="center",
                direction="column",
                width="100%",
                spacing="9",
            ),
            menu(),
            width="100%"
        )
    )

style={
    "background-color":"#0C1119",
    "box_sizing": "border_box",
    rx.card:{
        "background-color":"#0C1119",
        "border_width":"2px",
        "border_color":"white"}
}

app = rx.App(style=style,
    theme=rx.theme(
        appearance="dark", has_background=False, accent_color="teal"
        )
    )
app.add_page(index)
