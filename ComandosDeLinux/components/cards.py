import reflex as rx

widths = ["350px", "350px", "500px", "900px", "900px"]

def cards() -> rx.Component:
    return rx.vstack(
        rx.card(rx.vstack(
            rx.text("Iniciando en linux", color_scheme="teal", size="3"),
            rx.container(rx.blockquote("Listar un directorio:", size="2"),
                         rx.code_block("""ls [directorio]""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Ver alchivos ocultos:", size="2"),
                         rx.code_block("""ls -a""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),
            
            rx.container(rx.blockquote("Navegar entre directorios:", size="2"),
                         rx.code_block("""cd [ruta de directorio]""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Leer archivos:", size="2"),
                         rx.code_block("""cat [archivo]""", language="bash", 
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Mover archivos o directorios:", size="2"),
                         rx.code_block("""mv [archivo o diretorio] [ruta destino]""", language="bash", 
                                       width="100%", font_size="0.8em"), 
                                       rx.text("Tabién se usa para cambiar el nombre ",
                                               rx.code("mv [nombre] [nombre nuevo]")), width="100%"),

            rx.container(rx.blockquote("copiar archivos o directorios:", size="2"),
                         rx.code_block("""cp [archivo o directorio] [ruta destino]""", language="bash", 
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Crear archivos:", size="2"),
                         rx.code_block("""touch [nombre de archivo]""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Editar archivos:", size="2"),
                         rx.code_block("""vim [nombre de archivo]""", language="bash",
                                       width="100%", font_size="0.8em"), 
                        rx.code_block("""nano [nombre de archivo]""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"), 
            spacing="4"
        ), width=widths, variant="surface", id="iniciandoEnLinux"),

        rx.card(rx.vstack(
            rx.text("Gestión de usuarios y grupos", color_scheme="teal", size="3"),
            rx.container(rx.blockquote("Añadir un nuevo usuario:", size="2"),
                         rx.code_block("""useradd [nombre de usuario]""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Cambiar contraseña de usuario:", size="2"),
                         rx.code_block("""passwd [nombre de usuario]""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),
            
            rx.container(rx.blockquote("Modificar atributos de usuario:", size="2"),
                         rx.code_block("""usermod [opción] LOGIN""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Añadir un nuevo grupo:", size="2"),
                         rx.code_block("""groupadd [nombre de grupo]""", language="bash", 
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Eliminar usuario:", size="2"),
                         rx.code_block("""userdel [nombre de usuario]""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Eliminar grupo:", size="2"),
                         rx.code_block("""groupdel [nombre del grupo]""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),
            spacing="4"
        ), width=widths, variant="surface", id="gestionUsuariosGrupos"),

        rx.card(rx.vstack(
            rx.text("Gestión de procesos", color_scheme="teal", size="3"),
            rx.container(rx.blockquote("Mostrar procesos en ejecución:", size="2"),
                         rx.code_block("""ps -e""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Mostrar procesos en tiempo real:", size="2"),
                        rx.code_block("""top""", language="bash",
                                      width="100%", font_size="0.8em"), width="100%"),
                        
            rx.container(rx.blockquote("Terminar un proceso:", size="2"),
                        rx.code_block("""kill [PID]""", language="bash",
                                      width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Terminar todos los procesos con un nombre específico:", size="2"),
                        rx.code_block("""killall""", language="bash",
                                      width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Iniciar un proceso con una prioridad específica:", size="2"),
                            rx.code_block("""nice [nivel de prioridad] [comando]""", language="bash",
                                          width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Cambiar de prioridad de ejecución de un proceso:", size="2"),
                            rx.code_block("""renice [nivel de prioridad] [comando]""", language="bash",
                                          width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Colocar un proceso en segundo plano:", size="2"),
                         rx.code_block("""bg""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Traer un proceso en segundo plano al primer plano:", size="2"),
                         rx.code_block("""fg""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Mostrar los trabajos en segundo plano y detenidos:", size="2"),
                         rx.code_block("""jobs""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Ejecutar un comando de forma que siga funcionando incluso después de cerrar la sesión:", size="2"),
                         rx.code_block("""nohup""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),
            spacing="4",
        ), width=widths, variant="surface", id="gestionProcesos"),

        rx.card(rx.vstack(
            rx.text("Gestión de paquetes", color_scheme="teal", size="3"),
            rx.container(rx.blockquote("Gestinar paquetes en sistemas basados en Debian:", size="2"),
                        rx.code_block("""apt-get""", language="bash",
                        width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Gestinar paquetes en sistemas basados en Red Hat:", size="2"),
                        rx.code_block("""yum""", language="bash",
                        width="100%", font_size="0.8em"), width="100%"),
                        
            rx.container(rx.blockquote("Gestinar paquetes en sistemas basados en Fedora:", size="2"),
                                rx.code_block("""dnf""", language="bash",
                                width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Gestinar paquetes en sistemas basados en Arch Linux:", size="2"),
                        rx.code_block("""pacman""", language="bash",
                                      width="100%", font_size="0.8em"), width="100%"),               
            spacing="4"
        ), width=widths, variant="surface", id="gestionPaquetes"),

        rx.card(rx.vstack(
            rx.text("Gestión de redes y conectividad", color_scheme="teal", size="3"),
            rx.container(rx.blockquote("Mostrar información sobre interfaces de red:", size="2"),
                         rx.code_block("""ifconfig""", language="bash", width="100%", font_size="0.8em"), 
                         rx.code_block("""ip""", language="bash", width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Verificar la conectividad con un host remoto:", size="2"),
                         rx.code_block("""ping [ip]""", language="bash",
                         width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Rastrear la ruta de los paquetes a un host remoto:", size="2"),
                         rx.code_block("""traceroute [ip]""", language="bash",
                         width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Mostrar estadísticas de red y conexiones de red:", size="2"),
                         rx.code_block("""netstat""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Conectar a un servidor remoto de forma segura:", size="2"),
                         rx.code_block("""ssh""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Generar y administrar claves SSH para autenticación segura:", size="2"),
                         rx.code_block("""ssh-keygen""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Configurar reglas de firewall:", size="2"),
                         rx.code_block("""iptables""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Herramienta de configuración simplificada de firewall (Uncomplicated Firewall):", size="2"),
                         rx.code_block("""ufw""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Habilitar o deshabilitar interfaces de red:", size="2"),
                         rx.code_block("""ifup / ifdown""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Mostrar y manipular la tabla de enrutamiento del kernel:", size="2"),
                         rx.code_block("""route""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("(Network Manager Command Line Interface): Controlar y configurar conexiones de red utilizando NetworkManager:", size="2"),
                         rx.code_block("""nmcli""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),
                    spacing="4"
        ), width=widths, variant="surface", id="redesConectividad"),
        
        rx.card(rx.vstack(
            rx.text("Programación de tareas", color_scheme="teal", size="3"),
            rx.container(rx.blockquote("Programar tareas para que se ejecuten en momentos específicos:", size="2"),
                         rx.code_block("""cron""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Ejecutar comandos o scripts en un momento específico:", size="2"),
                         rx.code_block("""at""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),
            spacing="4"
        ), width=widths, variant="surface", id="programacionTareas"),

        rx.card(rx.vstack(
            rx.text("Monitoreo y registro del sistema", color_scheme="teal", size="3"),
            rx.container(rx.blockquote("Apagar o reiniciar el sistema:", size="2"),
                         rx.code_block("""shutdown""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Reiniciar el sistema:", size="2"),
                         rx.code_block("""reboot""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Mostrar o configurar el nombre del host:", size="2"),
                         rx.code_block("""hostname""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Mostrar o establecer la fecha y la hora del sistema:", size="2"),
                         rx.code_block("""date""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Mostrar cuánto tiempo ha estado encendido el sistema:", size="2"),
                         rx.code_block("""uptime""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Ver y manipular registros del sistema y del servicio:", size="2"),
                         rx.code_block("""journalctl""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),
            
            rx.container(rx.blockquote("Mostrar el registro del kernel del sistema:", size="2"),
                         rx.code_block("""dmesg""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Administrar y rotar archivos de registro para evitar el desbordamiento de disco:", size="2"),
                         rx.code_block("""logrotate""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Mostrar estadísticas de memoria virtual", size="2"),
                         rx.code_block("""vmstat""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Mostrar estadísticas de utilización de la CPU y del dispositivo de entrada/salida:", size="2"),
                         rx.code_block("""iostat""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Recolectar, informar y guardar datos de actividad del sistema:", size="2"),
                         rx.code_block("""sar""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Mostrar estadísticas de uso de la CPU:", size="2"),
                         rx.code_block("""mpstat""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),
                    spacing="4"
        ), width=widths, variant="surface", id="administracionSistema"),

        rx.card(rx.vstack(
            rx.text("Gestión de permisos de archivos", color_scheme="teal", size="3"),
            rx.container(rx.blockquote("Cambiar los permisos de un archivo o directorio:", size="2"),
                         rx.code_block("""chmod""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Cambiar el propietario y el grupo de un archivo o directorio:", size="2"),
                         rx.code_block("""chown""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Cambiar el grupo de un archivo o directorio:", size="2"),
                         rx.code_block("""chgrp""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),
            spacing="4"
        ), width=widths, variant="surface", id="gestionPermisosArchivos"),

        rx.card(rx.vstack(
            rx.text("Gestión de discos y almacenamiento", color_scheme="teal", size="3"),
            rx.container(rx.blockquote("Mostrar el espacio en disco disponible y utilizado:", size="2"),
                         rx.code_block("""df""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Mostrar el uso del espacio en disco de archivos y directorios:", size="2"),
                         rx.code_block("""du""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Manipular las tablas de particiones de los discos:", size="2"),
                         rx.code_block("""fdisk""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Montar sistemas de archivos en el árbol de directorios:", size="2"),
                         rx.code_block("""mount""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Desmontar sistemas de archivos:", size="2"),
                         rx.code_block("""umount""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),
            spacing="4"
        ), width=widths, variant="surface", id="gestionDiscosAlmacenamiento"),

        rx.card(rx.vstack(
            rx.text("Gestión de archivos comprimidos", color_scheme="teal", size="3"),
            rx.container(rx.blockquote("Manipular archivos de formato tar:", size="2"),
                         rx.code_block("""tar""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Comprimir/descomprimir archivos usando el formato gzip:", size="2"),
                         rx.code_block("""gzip / gunzip""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Comprimir/descomprimir archivos usando el formato zip:", size="2"),
                         rx.code_block("""zip / unzip""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Comprimir/descomprimir archivos usando el formato bzip2:", size="2"),
                         rx.code_block("""bzip2 / bunzip2""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),
            spacing="4"
        ), width=widths, variant="surface", id="gestionArchivosComprimidos"),

        rx.card(rx.vstack(
            rx.text("Virtualización y contenedores", color_scheme="teal", size="3"),
            rx.container(rx.blockquote("Crear, gestionar y desplegar contenedores:", size="2"),
                        rx.code_block("""docker""", language="bash",
                        width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Herramienta de contenedor ligero:", size="2"),
                        rx.code_block("""lxc""", language="bash",
                        width="100%", font_size="0.8em"), width="100%"),
                        
            rx.container(rx.blockquote(" Plataforma de virtualización para ejecutar múltiples sistemas operativos:", size="2"),
                                rx.code_block("""virtualbox""", language="bash",
                                width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Módulo de virtualización del kernel de Linux:", size="2"),
                        rx.code_block("""kvm""", language="bash",
                                      width="100%", font_size="0.8em"), width="100%"),               
            spacing="4"
        ), width=widths, variant="surface", id="virtualizacionContenedores"),

        rx.card(rx.vstack(
            rx.text("Administración de servicios", color_scheme="teal", size="3"),
            rx.container(rx.blockquote("Controlar el sistema y los servicios del sistema:", size="2"),
                         rx.code_block("""systemctl""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),

            rx.container(rx.blockquote("Iniciar, detener, reiniciar y administrar servicios del sistema", size="2"),
                         rx.code_block("""service""", language="bash",
                                       width="100%", font_size="0.8em"), width="100%"),
                    spacing="4"
        ), width=widths, variant="surface", id="administracionServicios"),
        top="50px",
        spacing="4",
        width="100%"
    )
