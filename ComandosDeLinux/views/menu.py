import reflex as rx

def menu() -> rx.Component:
    return rx.container(rx.chakra.menu(
            rx.chakra.menu_button(rx.icon("menu", stroke_width=2, color="white", size=30, margin="10px"), 
                                  border_radius="100%", background_color="teal"),
            rx.chakra.menu_list(
                rx.chakra.menu_item(rx.link("Iniciando en linux", href="#iniciandoEnLinux")),
                rx.chakra.menu_item(rx.link("Gestión de usuarios y grupos", href="#gestionUsuariosGrupos")),
                rx.chakra.menu_item(rx.link("Gestión de procesos", href="#gestionProcesos")),
                rx.chakra.menu_item(rx.link("Gestión de paquetes", href="#gestionPaquetes")),
                rx.chakra.menu_item(rx.link("Redes y conectividad", href="#redesConectividad")),
                rx.chakra.menu_item(rx.link("Programación de tareas", href="#programacionTareas")),
                rx.chakra.menu_item(rx.link("Monitoreo y registro del sistema", href="#administracionSistema")),
                rx.chakra.menu_item(rx.link("Gestión de permisos de archivos", href="#gestionPermisosArchivos")),
                rx.chakra.menu_item(rx.link("Gestión de discos y almacenamiento", href="#gestionDiscosAlmacenamiento")),
                rx.chakra.menu_item(rx.link("Gestión de archivos comprimidos", href="#gestionArchivosComprimidos")),
                rx.chakra.menu_item(rx.link("Virtualización y contenedores", href="#virtualizacionContenedores")),
                rx.chakra.menu_item(rx.link("Administración de servicios", href="#administracionServicios")),
            ),  auto_select=False
        ), position="fixed", bottom="40px", right="10px")
