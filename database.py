from constans import connection


class Database:
    def __init__(self):
        pass

    def create_account(self, login, password, name):
        """
        Function for creating account and adding all his data to database
        :param login: email of user
        :param password: password for account
        :param name: name of user
        :return:
        """
        try:
            # create a new table
            with connection.cursor() as cursor:
                cursor.execute(f"CREATE TABLE IF NOT EXISTS user_data(id serial PRIMARY KEY, login VARCHAR, password VARCHAR, name VARCHAR)")
                print("[INFO] Table created successfully")

                cursor.execute("INSERT INTO user_data (login, password, name) VALUES (%s, %s, %s);", (login, password, name))
                print("[INFO] Data was successfully inserted")

        except Exception as _ex:
            print("[ERROR] Error while working with PostgreSQL", _ex)

    def check_exist_account(self, login):
        """
        Function checking if data of user in the database or no
        :param login: email from user
        :return:
        """
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM user_data WHERE login='{login}'")
                result = cursor.fetchall()
                return result

        except Exception as _ex:
            print("[ERROR] Error:", _ex)

        finally:
            print("[INFO] PostgreSQL connection closed")

    def new_password(self, login, password):
        """

        :param login: users email
        :param password: new password from user
        """

        try:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT name FROM user_data WHERE login='{login}'")
                self.name = cursor.fetchone()

                cursor.execute(f"DELETE from user_data WHERE login='{login}'")
                print("[INFO] Password was delete")

                cursor.execute("INSERT INTO user_data (login, password, name) VALUES (%s, %s, %s);",
                               (login, password, self.name))
                print("[INFO] New password was added")

        except Exception as _ex:
            print("[ERROR] Error with login to account", _ex)

        finally:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection closed")

    def select_name(self, login):
        """
        Function for select name from database
        :param login: login from user
        :return: name of user
        """
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT name FROM user_data WHERE login='{login}'")
                self.name = cursor.fetchone()
                return self.name

        except Exception as _ex:
            print("[ERROR] Error:", _ex)

        finally:
            print("[INFO] PostgreSQL connection closed")

    def log_in(self, login, password):
        """
        Function for checking if user_data compare with data from database
        :param login: login from user
        :param password: password from user
        """
        flag = None

        try:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM user_data WHERE login='{login}' and password='{password}'")
                self.query_result = cursor.fetchall()
                if len(self.query_result) == 0:
                    flag = False

        except Exception as _ex:
            print("[ERROR] Error with login to account", _ex)

        finally:
            if connection:
                if flag == True:
                    connection.close()
                    print("[INFO] PostgreSQL connection closed")

    def return_query_result(self):
        """
        Function for checking user have a record in database
        :return: all data about user
        """
        return self.query_result