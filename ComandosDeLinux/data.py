import reflex as rx

card_data = {
    "iniciandoEnLinux": {
        "title": "Iniciando en linux",
        "commands": [
            ("Listar un directorio:", "ls [directorio]"),
            ("Ver alchivos ocultos:", "ls -a"),
            ("Navegar entre directorios:", "cd [ruta de directorio]"),
            ("Leer archivos:", "cat [archivo]"),
            ("Mover archivos o directorios:", "mv [archivo o diretorio] [ruta destino]"),
            ("copiar archivos o directorios:", "cp [archivo o directorio] [ruta destino]"),
            ("Crear archivos:", "touch [nombre de archivo]"),
            ("Editar archivos:", ["vim [nombre de archivo]", "nano [nombre de archivo]"]),
        ]
    },
    "gestionUsuariosGrupos": {
        "title": "Gestión de usuarios y grupos",
        "commands": [
            ("Añadir un nuevo usuario:", "useradd [nombre de usuario]"),
            ("Cambiar contraseña de usuario:", "passwd [nombre de usuario]"),
            ("Modificar atributos de usuario:", "usermod [opción] LOGIN"),
            ("Añadir un nuevo grupo:", "groupadd [nombre de grupo]"),
            ("Eliminar usuario:", "userdel [nombre de usuario]"),
            ("Eliminar grupo:", "groupdel [nombre del grupo]"),
        ]
    },
    "gestionProcesos": {
        "title": "Gestión de procesos",
        "commands": [
            ("Mostrar procesos en ejecución:", "ps -e"),
            ("Mostrar procesos en tiempo real:", "top"),
            ("Terminar un proceso:", "kill [PID]"),
            ("Terminar todos los procesos con un nombre específico:", "killall"),
            ("Iniciar un proceso con una prioridad específica:", "nice [nivel de prioridad] [comando]"),
            ("Cambiar de prioridad de ejecución de un proceso:", "renice [nivel de prioridad] [comando]"),
            ("Colocar un proceso en segundo plano:", "bg"),
            ("Traer un proceso en segundo plano al primer plano:", "fg"),
            ("Mostrar los trabajos en segundo plano y detenidos:", "jobs"),
            ("Ejecutar un comando de forma que siga funcionando incluso después de cerrar la sesión:", "nohup"),
        ]
    },
    "gestionPaquetes": {
        "title": "Gestión de paquetes",
        "commands": [
            ("Gestinar paquetes en sistemas basados en Debian:", "apt-get"),
            ("Gestinar paquetes en sistemas basados en Red Hat:", "yum"),
            ("Gestinar paquetes en sistemas basados en Fedora:", "dnf"),
            ("Gestinar paquetes en sistemas basados en Arch Linux:", "pacman"),
        ]
    },
    "redesConectividad": {
        "title": "Gestión de redes y conectividad",
        "commands": [
            ("Mostrar información sobre interfaces de red:", ["ifconfig", "ip"]),
            ("Verificar la conectividad con un host remoto:", "ping [ip]"),
            ("Rastrear la ruta de los paquetes a un host remoto:", "traceroute [ip]"),
            ("Mostrar estadísticas de red y conexiones de red:", "netstat"),
            ("Conectar a un servidor remoto de forma segura:", "ssh"),
            ("Generar y administrar claves SSH para autenticación segura:", "ssh-keygen"),
            ("Configurar reglas de firewall:", "iptables"),
            ("Herramienta de configuración simplificada de firewall (Uncomplicated Firewall):", "ufw"),
            ("Habilitar o deshabilitar interfaces de red:", "ifup / ifdown"),
            ("Mostrar y manipular la tabla de enrutamiento del kernel:", "route"),
            ("(Network Manager Command Line Interface): Controlar y configurar conexiones de red utilizando NetworkManager:", "nmcli"),
        ]
    },
    "programacionTareas": {
        "title": "Programación de tareas",
        "commands": [
            ("Programar tareas para que se ejecuten en momentos específicos:", "cron"),
            ("Ejecutar comandos o scripts en un momento específico:", "at"),
        ]
    },
    "administracionSistema": {
        "title": "Monitoreo y registro del sistema",
        "commands": [
            ("Apagar o reiniciar el sistema:", "shutdown"),
            ("Reiniciar el sistema:", "reboot"),
            ("Mostrar o configurar el nombre del host:", "hostname"),
            ("Mostrar o establecer la fecha y la hora del sistema:", "date"),
            ("Mostrar cuánto tiempo ha estado encendido el sistema:", "uptime"),
            ("Ver y manipular registros del sistema y del servicio:", "journalctl"),
            ("Mostrar el registro del kernel del sistema:", "dmesg"),
            ("Administrar y rotar archivos de registro para evitar el desbordamiento de disco:", "logrotate"),
            ("Mostrar estadísticas de memoria virtual", "vmstat"),
            ("Mostrar estadísticas de utilización de la CPU y del dispositivo de entrada/salida:", "iostat"),
            ("Recolectar, informar y guardar datos de actividad del sistema:", "sar"),
            ("Mostrar estadísticas de uso de la CPU:", "mpstat"),
        ]
    },
    "gestionPermisosArchivos": {
        "title": "Gestión de permisos de archivos",
        "commands": [
            ("Cambiar los permisos de un archivo o directorio:", "chmod"),
            ("Cambiar el propietario y el grupo de un archivo o directorio:", "chown"),
            ("Cambiar el grupo de un archivo o directorio:", "chgrp"),
        ]
    },
    "gestionDiscosAlmacenamiento": {
        "title": "Gestión de discos y almacenamiento",
        "commands": [
            ("Mostrar el espacio en disco disponible y utilizado:", "df"),
            ("Mostrar el uso del espacio en disco de archivos y directorios:", "du"),
            ("Manipular las tablas de particiones de los discos:", "fdisk"),
            ("Montar sistemas de archivos en el árbol de directorios:", "mount"),
            ("Desmontar sistemas de archivos:", "umount"),
        ]
    },
    "gestionArchivosComprimidos": {
        "title": "Gestión de archivos comprimidos",
        "commands": [
            ("Manipular archivos de formato tar:", "tar"),
            ("Comprimir/descomprimir archivos usando el formato gzip:", "gzip / gunzip"),
            ("Comprimir/descomprimir archivos usando el formato zip:", "zip / unzip"),
            ("Comprimir/descomprimir archivos usando el formato bzip2:", "bzip2 / bunzip2"),
        ]
    },
    "virtualizacionContenedores": {
        "title": "Virtualización y contenedores",
        "commands": [
            ("Crear, gestionar y desplegar contenedores:", "docker"),
            ("Herramienta de contenedor ligero:", "lxc"),
            ("Plataforma de virtualización para ejecutar múltiples sistemas operativos:", "virtualbox"),
            ("Módulo de virtualización del kernel de Linux:", "kvm"),
        ]
    },
    "administracionServicios": {
        "title": "Administración de servicios",
        "commands": [
            ("Controlar el sistema y los servicios del sistema:", "systemctl"),
            ("Iniciar, detener, reiniciar y administrar servicios del sistema", "service"),
        ]
    }
}
