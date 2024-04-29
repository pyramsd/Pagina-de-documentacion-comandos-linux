import reflex as rx
from ComandosDeLinux.components.navbar import navbar
from ComandosDeLinux.views.header import header
from ComandosDeLinux.views.documentation import documentation
from ComandosDeLinux.views.footer import footer
from ComandosDeLinux.views.menu import menu


@rx.page(
        title="Comandos de linux by Sergio Ruiz",
        description="Documentación de comandos linux para distintos propósitos de desarrollo",
        image="/splash.png",
)
def index() -> rx.Component:
    return rx.center(
        rx.script("document.documentElement.lang='es'"),
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
    rx.blockquote:{
        "color":"white"
    },
    rx.card:{
        "background-color":"#0C1119",
        "border_width":"2px",
        "border_color":"white"},
    rx.chakra.menu_list:{
        "background-color":"#2d3748"
    },
    rx.chakra.menu_item:{
        "background-color":"#2d3748"
    }
}

app = rx.App(style=style,
    theme=rx.theme(
        appearance="dark", has_background=True, accent_color="blue"
        )
    )
app.add_page(index)
