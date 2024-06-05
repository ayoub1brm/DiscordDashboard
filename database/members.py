from database.database import Database

class MembersDatabase(Database):
    def create_tables(self):
        self.execute('''
            CREATE TABLE IF NOT EXISTS Members (
                member_id INTEGER,
                username TEXT,
                discriminator TEXT,
                join_date DATETIME,
                leave_date DATETIME,
                is_bot INTEGER,
                activity_status TEXT,
                role_id INTEGER,
                FOREIGN KEY (role_id) REFERENCES Roles(role_id)
            )
        ''')
        
    def insert_member(self, member_data):
        self.execute('''
            INSERT INTO Members (member_id, username, discriminator, join_date, leave_date, is_bot, activity_status, role_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', member_data)

    def update_member_leave_date(self, member_id, leave_date):
        self.execute('''
            UPDATE Members SET leave_date = ? WHERE member_id = ?
        ''', (leave_date, member_id))

    def get_total_member_count(self):
        cursor = self.execute('''
            SELECT COUNT(*) FROM (SELECT * FROM Members GROUP BY member_id) WHERE leave_date is NULL AND is_bot = 0
        ''')
        result = cursor.fetchone()[0]
        self.close()
        return result

   def get_latest_member_joined_at(self):
        cursor = self.execute('SELECT MAX(join_date) FROM Members')
        result = cursor.fetchone()[0]
        if result:
            return datetime.fromisoformat(result)
        return None

