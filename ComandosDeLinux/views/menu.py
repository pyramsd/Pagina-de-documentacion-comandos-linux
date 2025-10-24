import reflex as rx
import reflex_chakra as rc

def menu() -> rx.Component:
    return rx.container(rc.menu(
            rc.menu_button(rx.icon("menu", stroke_width=2, color="white", size=30, margin="10px"), 
                                  border_radius="100%", background_color="teal"),
            rc.menu_list(
                rc.menu_item(rx.link("Iniciando en linux", href="#iniciandoEnLinux")),
                rc.menu_item(rx.link("Gestión de usuarios y grupos", href="#gestionUsuariosGrupos")),
                rc.menu_item(rx.link("Gestión de procesos", href="#gestionProcesos")),
                rc.menu_item(rx.link("Gestión de paquetes", href="#gestionPaquetes")),
                rc.menu_item(rx.link("Redes y conectividad", href="#redesConectividad")),
                rc.menu_item(rx.link("Programación de tareas", href="#programacionTareas")),
                rc.menu_item(rx.link("Monitoreo y registro del sistema", href="#administracionSistema")),
                rc.menu_item(rx.link("Gestión de permisos de archivos", href="#gestionPermisosArchivos")),
                rc.menu_item(rx.link("Gestión de discos y almacenamiento", href="#gestionDiscosAlmacenamiento")),
                rc.menu_item(rx.link("Gestión de archivos comprimidos", href="#gestionArchivosComprimidos")),
                rc.menu_item(rx.link("Virtualización y contenedores", href="#virtualizacionContenedores")),
                rc.menu_item(rx.link("Administración de servicios", href="#administracionServicios")),
            ),  auto_select=False
        ), position="fixed", bottom="40px", right="10px")
