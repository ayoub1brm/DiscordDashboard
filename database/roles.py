from database.database import Database

class RolesDatabase(Database):
    def create_tables(self):
        self.execute('''
            CREATE TABLE IF NOT EXISTS Roles (
                role_id INTEGER ,
                role_name TEXT
            )
        ''')

    def insert_role(self, role_data):
        self.execute('''
            INSERT INTO Roles (role_id, role_name)
            VALUES (?, ?)
        ''', role_data)

    def insert_roles(self, roles_data):
        self.executemany('''
            INSERT INTO Roles (role_id, role_name)
            VALUES (?, ?)
        ''', roles_data)
