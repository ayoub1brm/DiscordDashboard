__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import sqlite3
from datetime import datetime, timedelta
from threading import Lock

class Database:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialize(*args, **kwargs)
            return cls._instance

    def _initialize(self, db_path):
        self.db_path = db_path

    def connect(self):
        conn = sqlite3.connect(self.db_path, timeout=30, check_same_thread=False)
        conn.execute('PRAGMA journal_mode=WAL;')
        return conn

    def execute(self, query, params=(), retries=5):
        for i in range(retries):
            try:
                with self.connect() as conn:
                    cursor = conn.cursor()
                    cursor.execute(query, params)
                    conn.commit()
                    return cursor
            except sqlite3.OperationalError as e:
                if 'database is locked' in str(e):
                    time.sleep(2 ** i)  # Exponential backoff
                else:
                    raise
            except Exception as e:
                print(f"Error executing query: {e}")
                raise

    def executemany(self, query, param_list=(), retries=5):
        for i in range(retries):
            try:
                with self.connect() as conn:
                    cursor = conn.cursor()
                    cursor.executemany(query, param_list)
                    conn.commit()
                    return cursor
            except sqlite3.OperationalError as e:
                if 'database is locked' in str(e):
                    time.sleep(2 ** i)  # Exponential backoff
                else:
                    raise
            except Exception as e:
                print(f"Error executing query: {e}")
                raise

    def create_tables(self):
        raise NotImplementedError("Subclasses should implement this!")
