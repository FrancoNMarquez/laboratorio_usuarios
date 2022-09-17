from Usuario import Usuario
from Log.logger_base import log
from Conexiones.CursorDelPool import CursorDelPool
class UsuarioDAO:
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR ='INSERT INTO usuario(username,password) VALUES (%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall() #Guardo en registros todos los usuarios seleccionados, con sus respectivos
                                        #atributos
            usuarios = [] #Aca guardo todos los usuarios
            for registro in registros:
                usuario = Usuario(registro[0],registro[1])
                usuarios.append(usuario)
            return usuarios #retorno el array con todos los usuarios

    @classmethod
    def insertar(cls,persona):
        with CursorDelPool() as cursor:
            cursor.execute(cls._INSERTAR)
            pass
        