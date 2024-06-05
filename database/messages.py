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
        
    def close(self):
        self.conn.close()
        
    def insert_message(self, message_data):
        self.cursor.execute('''
            INSERT INTO Messages (message_id, channel_id, channel_type, member_id, message_content, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', message_data)

    def get_latest_message_id_for_channel(self, channel_id):
        cursor = self.execute('''
            SELECT message_id 
            FROM Messages 
            WHERE channel_id = ? 
            ORDER BY timestamp DESC 
            LIMIT 1
        ''', (channel_id,))
        result = cursor.fetchone()
        return result[0] if result else None
