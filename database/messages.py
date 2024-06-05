from database.database import Database

class MessagesDatabase(Database):
    def create_tables(self):
        self.execute('''
            CREATE TABLE IF NOT EXISTS Messages (
                message_id INTEGER PRIMARY KEY,
                channel_id INTEGER,
                channel_type TEXT,
                member_id INTEGER,
                message_content TEXT,
                timestamp DATETIME,
                FOREIGN KEY (channel_id) REFERENCES Channels(channel_id),
                FOREIGN KEY (member_id) REFERENCES Members(member_id)
            )
        ''')

    def insert_message(self, message_data):
        self.execute('''
            INSERT INTO Messages (message_id, channel_id, channel_type, member_id, message_content, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', message_data)

    def get_latest_message_timestamp(self):
        self.cursor.execute('SELECT MAX(timestamp) FROM Messages')
        result = self.cursor.fetchone()[0]
        self.close()
        return result

    # Add other Messages specific methods
