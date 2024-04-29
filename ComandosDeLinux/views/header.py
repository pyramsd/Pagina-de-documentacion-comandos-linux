import reflex as rx

def header() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.avatar(
                src="/logo.jpg",
                size="9",
                radius="full"
            ),
            rx.text("Para mayor información acerca los comandos puedes visitar la página ",
                    rx.link("man7.org", href="https://man7.org/linux/man-pages", underline="always", 
                            is_external=True), align="center", color="white"), 
            
            rx.text("También puedes escribir en la terminal ",
                    rx.code("[comando] --help/-h"), " o ",
                    rx.code("man [comando]"), align="center", color="white")

        ,align="center")
    )
