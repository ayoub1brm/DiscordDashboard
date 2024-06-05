from database.database import Database

class ChannelsDatabase(Database):
    def create_tables(self):
        self.execute('''
            CREATE TABLE IF NOT EXISTS Channels (
                channel_id INTEGER PRIMARY KEY,
                channel_name TEXT
            )
        ''')

    def insert_channel(self, channel_id, channel_name):
        self.execute('''
            INSERT OR IGNORE INTO Channels (channel_id, channel_name)
            VALUES (?, ?)
        ''', (channel_id, channel_name))

    def get_channels(self):
        self.cursor.execute('SELECT channel_id, channel_name FROM Channels')
        result = self.cursor.fetchall()
        self.close()
        return result

    # Add other Channels specific methods
