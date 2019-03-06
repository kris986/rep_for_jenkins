from psycopg2 import connect
from config import DB_USER, DB_NAME, DB_PASSWORD, DB_HOST


class ConnectDataBase:
    def __init__(self):
        pass

    def connect_db(self):
        conn = connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        # conn = connect(database="web_flask", user="postgres", password="postgres", host='localhost')
        return conn

    def insert_user_in_db(self, user_name, user_email, password, country, city):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users(user_name, user_email, password, country, city) VALUES('{user_name}', '{user_email}', "
            "'{password}', '{country}', '{city}');".format(
                user_name=user_name, user_email=user_email, password=password, country=country, city=city))
        conn.commit()
        self.close_db()

    def insert_users_avatar(self, avatar):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (avatar) VALUES('{avatar}');".format(avatar=avatar))
        conn.commit()
        self.close_db()

    def insert_users_dog_in_db(self, owner, breed, sex, dog_bday, pet_name, kennel, country=None, city=None):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "WITH temp_for_users_dogs AS ("
            "SELECT users.id as user_id, breeds.id as breed_id "
            "FROM users, breeds "
            "where users.user_name = '{owner}' and breeds.breed_name = '{breed}')"
            "INSERT INTO users_dogs"
            "(user_id, owner, breed_id, breed, sex, dog_bday, pet_name, kennel, country, city)"
            "VALUES("
            "(select user_id from temp_for_users_dogs),"
            "'{owner}',"
            "(select breed_id from temp_for_users_dogs),"
            "'{breed}',"
            "'{sex}',"
            "'{dog_bday}',"
            "'{pet_name}',"
            "'{kennel}',"
            "Null,"
            "Null);".format(
                owner=owner,
                breed=breed,
                sex=sex,
                dog_bday=dog_bday,
                pet_name=pet_name,
                kennel=kennel,
                country=country,
                city=city))
        conn.commit()
        self.close_db()

    def select_users_from_db(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('select * from users')
        colnames = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        self.close_db()
        return [colnames, rows]

    def select_breeds(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('select * from breeds')
        colnames = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        self.close_db()
        return [colnames, rows]

    def select_sex(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('select sex_nm from sex')
        rows = cursor.fetchall()
        self.close_db()
        return rows

    def select_users_dogs(self, user_name):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "select owner, pet_name, breed, sex, kennel, to_char(dog_bday, 'DD Mon YYYY') from users_dogs where owner = '{user_name}'".format(
                user_name=user_name))
        colnames = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        self.close_db()
        return [colnames, rows]

    def select_all_users_dogs(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("select owner, pet_name, breed, sex, kennel, to_char(dog_bday, 'DD Mon YYYY') from users_dogs")
        colnames = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        self.close_db()
        return [colnames, rows]

    def parse_users(self):
        colnames, users = self.select_users_from_db()
        users_dict = dict()
        for user in users:
            users_dict[user[1]] = {colnames[2]: user[2],
                                   colnames[3]: user[3],
                                   colnames[4]: user[4],
                                   colnames[5]: user[5]}
        return users_dict

    def close_db(self):
        conn = self.connect_db()
        conn.close()


# a = ConnectDataBase()
# print(a.select_users_from_db())
class Photo(ConnectDataBase):
    def __init__(self, filename):
        self.filename = filename

    def insert_photo_to_db(self, photo_id=None):
        return photo_id
