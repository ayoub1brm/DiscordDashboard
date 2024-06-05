__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import sqlite3
from datetime import datetime, timedelta
from threading import Lock

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def close(self):
        self.conn.close()
        
    def create_tables(self):
        raise NotImplementedError("Subclasses should implement this!")
