from Dominio.Usuario import Usuario
from Log.logger_base import log
from Conexiones.CursorDelPool import CursorDelPool
class UsuarioDAO:
    '''
    DAO - Data Access Object para la tabla de usuario
    CRUD- Create - Read - Update - Delete para la tabla de usuario
    '''
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR ='INSERT INTO usuario(username,password) VALUES (%s,%s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            log.debug('Seleccionando usuarios')
            registros = cursor.fetchall() #Guardo en registros todos los usuarios seleccionados, con sus respectivos
                                        #atributos
            usuarios = [] #Aca guardo todos los usuarios
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios #retorno el array con todos los usuarios

    @classmethod
    def insertar(cls,usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls,usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a actualizar: {usuario} ')
            valores = (usuario.id_usuario, usuario.username, usuario.password)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    @classmethod
    def eliminar(cls,usuario):
        with CursorDelPool() as cursor:
            valores = usuario.id_usuario
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
