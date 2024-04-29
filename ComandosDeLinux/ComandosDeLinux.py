import reflex as rx
from ComandosDeLinux.styles.styles import BASE_STYLE
from ComandosDeLinux.pages.index import index

app = rx.App(
    style=BASE_STYLE,
    theme=rx.theme(
        appearance="dark", has_background=False, accent_color="teal"
        )
    )