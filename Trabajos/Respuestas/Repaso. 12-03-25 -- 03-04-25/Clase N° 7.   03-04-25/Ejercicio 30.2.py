from Ejercicio_30_2_Extension import Administrador, Privilegios

privilegios_admin = Privilegios([
    "Puede Agregar Publicaciones",
    "Puede Eliminar Publicaciones",
    "Puede Bloquear Usuarios",
    "Puede Editar Publicaciones",
    "Puede Ver Estadísticas",
    "Puede Gestionar Comentarios",
    "Puede Agregar Imágenes",
    "Puede Modificar Perfil",
    "Puede Ver Perfil De Otros Usuarios",
    "Puede Enviar Mensajes Privados"
])

Admin = Administrador("Santino", "Rodriguez", 16,
                      "santinorofu@gmail.com", "CABA", privilegios_admin)
Admin.MostrarPrivilegios()
