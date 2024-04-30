import reflex as rx

# Común
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


_meta = [
    {"name": "og:type", "content": "website"}
]

# Index
index_title = "Comandos de linux By Sergio Ruiz"
index_description = "Documentación de comandos linux para distintos propósitos de desarrollo"

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)

# quiz
quiz_title = "Ponte a prueba!"
quiz_description = "Ponte a prueba con este pequeño quiz"

quiz_meta = [
    {"name": "og:title", "content": quiz_title},
    {"name": "og:description", "content": quiz_description},
]
quiz_meta.extend(_meta)

# resultados
results_title = "Resultados"
results_description = "Resultados des test"

results_meta = [
    {"name": "og:title", "content": results_title},
    {"name": "og:description", "content": results_description},
]
results_meta.extend(_meta)