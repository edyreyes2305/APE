from .entities.User import User

class ModelUser ():
    
    @classmethod
    def login(self, mysql, user):
        try:
            cursor = mysql.connection.cursor()
            sql = "SELECT id, nom_usuario, password, nombre FROM datos WHERE nom_usuario = '{}' ".format(user.nom_usuario)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3])
                return user
            else:
                return None            
        except Exception as ex:
            raise Exception(ex)
        
        
    @classmethod
    def get_by_id(self, mysql, id):
        try:
            cursor = mysql.connection.cursor()
            sql = "SELECT id, nom_usuario, nombre, semestre FROM datos WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                logged_user = User(row[0], row[1], None, row[2])
                return logged_user
            else:
                return None            
        except Exception as ex:
            raise Exception(ex)