from database.database import Database

class RolesDatabase(Database):
    def create_tables(self):
        self.execute('''
            CREATE TABLE IF NOT EXISTS Roles (
                role_id INTEGER PRIMARY KEY,
                role_name TEXT
            )
        ''')

    def insert_role(self, role_data):
        self.execute('''
            INSERT OR IGNORE INTO Roles (role_id, role_name)
            VALUES (?, ?)
        ''', role_data)

    def insert_roles(self, roles_data):
        self.executemany('''
            INSERT OR IGNORE INTO Roles (role_id, role_name)
            VALUES (?, ?)
        ''', roles_data)
