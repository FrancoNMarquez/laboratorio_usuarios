from Dominio.Usuario import Usuario

from Dominio.UsuarioDAO import UsuarioDAO

from Log.logger_base import log

opcion = None
while opcion != 5:
    print('Opciones:')
    print('1. Listar usuarios')
    print('2. Agregar usuarios')
    print('3. Modificar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')
    opcion = int(input('Seleccione una opcion'))

    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_temporal = input('Ingrese el username: ')
        password_temporal = input('Ingrese la contrasenia')
        usuario = Usuario(username=username_temporal, password=password_temporal)
        usuariosInsertados = UsuarioDAO.insertar(usuario)
        log.info(f'Usuarios insertados: {usuariosInsertados}')
    elif opcion == 3:
        idUsuario_temp = int(input('Escribe el id_usuario a modificar:'))
        username_temporal = input('Ingrese el username nuevo:')
        password_temporal = input('Ingrese la contrasenia nueva')
        usuario = Usuario(idUsuario_temp, username_temporal, password_temporal)
        usuariosActualizados = UsuarioDAO.actualizar(usuario)
    elif opcion == 4:
        idUsuario_temp = int(input('Ingrese el id_usuario a eliminar'))
        usuario = Usuario(id_usuario=idUsuario_temp)
        usuariosEliminados = UsuarioDAO.eliminar(usuario)
        print(f'Usuarios eliminados : {usuariosEliminados}')
else:
    print('Salimos del while')
