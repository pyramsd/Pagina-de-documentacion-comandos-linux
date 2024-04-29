import reflex as rx

# Común
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

# Index
index_title = "Comandos de linux By Sergio Ruiz"
index_description = "Documentación de comandos linux para distintos propósitos de desarrollo"

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]