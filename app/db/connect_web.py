from psycopg2 import connect


class ConnectDataBase:
    def __init__(self):
        pass

    def connect_db(self):
        conn = connect(database="web_flask", user="postgres", password="postgres", host='localhost')
        return conn

    def insert_user_in_db(self, user_name, user_email, password, city):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users(user_name, user_email, password, city) VALUES('{user_name}', '{user_email}', "
            "'{password}', '{city}');".format(
                user_name=user_name, user_email=user_email, password=password, city=city))
        conn.commit()

    def update_user_in_db(self):
        pass

    def select_users_from_db(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('select * from users')
        colnames = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        return [colnames, rows]

    def parse_users(self):
        colnames, users = self.select_users_from_db()
        users_dict = dict()
        for user in users:
            users_dict[user[1]] = {colnames[2]: user[2],
                                   colnames[3]: user[3],
                                   colnames[4]: user[4]}
        return users_dict

    def close_db(self):
        conn = self.connect_db()
        conn.close()
