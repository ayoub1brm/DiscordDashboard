from database.database import Database

class RolesDatabase(Database):
    def create_tables(self):
        self.execute('''
            CREATE TABLE IF NOT EXISTS Roles (
                role_id INTEGER,
                role_name TEXT
            )
        ''')

    def insert_role(self, role_data):
        self.execute('''
            INSERT INTO Roles (role_id, role_name)
            VALUES (?, ?)
        ''', role_data)

    def get_role_distribution(self):
        self.cursor.execute('''
            SELECT Roles.role_name, COUNT(Members.member_id) 
            FROM Members 
            JOIN Roles ON Members.role_id = Roles.role_id
            WHERE Members.is_bot = 0
            GROUP BY Roles.role_name
        ''')
        result = self.cursor.fetchall()
        self.close()
        return result

    # Add other Roles specific methods
