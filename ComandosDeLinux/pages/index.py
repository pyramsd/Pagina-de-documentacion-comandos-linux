import reflex as rx
import ComandosDeLinux.utils as utils
from ComandosDeLinux.components.navbar import navbar
from ComandosDeLinux.views.header import header
from ComandosDeLinux.views.cards import cards
from ComandosDeLinux.views.footer import footer
from ComandosDeLinux.views.menu import menu
from ComandosDeLinux.routes import Route


@rx.page(
        title=utils.index_title,
        description=utils.index_description,
        meta=utils.index_meta
)
def index() -> rx.Component:
    return rx.center(
        utils.lang(),
        rx.vstack(
            rx.center(
                rx.fragment(navbar(), rx.container(header(), max_width="60em")),
                cards(),
                rx.button("Quiz!", on_click=lambda: rx.redirect(Route.QUIZ.value)),
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
