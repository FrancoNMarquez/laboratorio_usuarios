class Usuario:
    cantUsuarios = 0

    @classmethod
    def aumentarCant(cls):
        cls.cantUsuarios+=1
        return cls.cantUsuarios
    def __init__(self,username=None,password=None):
        #El autoincremento iria aca, o pasa por parametro el id, y se autoincrementa en la base de datos?
        self._id_usuario = Usuario.aumentarCant()
        self._username=username
        self._password = password

    @property
    def id_usuario (self):
        return self._id_usuario

    @property
    def username(self):
        return self._username
    @property
    def password(self):
        return self._password

    @username.setter
    def username(self,username):
        self._username = username

    @password.setter
    def password(self,password):
        self._password = password

    def __str__(self):
        return f'ID Usuario: {self._id_usuario} Usuario:{self._username} Password: *****'