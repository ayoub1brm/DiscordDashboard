__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import sqlite3
from datetime import datetime, timedelta

import sqlite3
import time
from datetime import datetime, timedelta

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None
        self.cursor = None

    def connect(self):
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_path, timeout=30)
            self.conn.execute('PRAGMA journal_mode=WAL;')
            self.cursor = self.conn.cursor()

    def close(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()
            self.conn = None
            self.cursor = None

    def execute(self, query, params=(), retries=5):
        for _ in range(retries):
            try:
                self.connect()
                self.cursor.execute(query, params)
                self.conn.commit()
                return
            except sqlite3.OperationalError as e:
                if 'database is locked' in str(e):
                    time.sleep(2)  # wait for 2 seconds before retrying
                else:
                    raise
            finally:
                self.close()

    def create_tables(self):
        raise NotImplementedError("Subclasses should implement this!")

    # Add other common methods if necessary
