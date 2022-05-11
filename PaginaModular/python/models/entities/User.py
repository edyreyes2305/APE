from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):       
    
    def __init__(self, id, nom_usuario, password, nombre="") -> None:
        self.id = id
        self.nom_usuario = nom_usuario
        self.password = password
        self.nombre = nombre
        
    
    
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
    
print(generate_password_hash("suscribete"))