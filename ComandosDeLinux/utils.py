import reflex as rx

# Común
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

preview = "/assets/preview.jpg"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
]

# Index
index_title = "Comandos de linux By Sergio Ruiz"
index_description = "Documentación de comandos linux para distintos propósitos de desarrollo"

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)