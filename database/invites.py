from database.database import Database

class InvitesDatabase(Database):
    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Invites (
                code TEXT PRIMARY KEY,
                uses INTEGER,
                inviter_id INTEGER,
                created_at TIMESTAMP
            )
        ''')

    def close(self):
        self.conn.close()

    def insert_invite(self, code, uses, inviter_id, created_at):
        self.cursor.execute('''
            INSERT OR REPLACE INTO Invites (code, uses, inviter_id, created_at)
            VALUES (?, ?, ?, ?)
        ''', (code, uses, inviter_id, created_at))

    def update_invite_uses(self, code, uses):
        self.cursor.execute('''
            UPDATE Invites
            SET uses = ?
            WHERE code = ?
        ''', (uses, code))

    def delete_invite(self, code):
        self.cursor.execute('DELETE FROM Invites WHERE code = ?', (code,))

    def get_invite_uses(self, code):
        self.cursor.execute('SELECT uses FROM Invites WHERE code = ?', (code,))
        result = self.cursor.fetchone()
        self.close()
        return result

    def get_all_invites(self):
        self.cursor.execute('SELECT code, uses FROM Invites')
        result = self.cursor.fetchall()
        self.close()
        return result

    # Add other Invites specific methods
