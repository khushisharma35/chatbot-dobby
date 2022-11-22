# some_file.py
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '/Users/apple/PycharmProjects/pythonProject')
import config
from database import createtable
import  psycopg2

print(config.databaseName)
# establishing the connection
class Database:
    """PostgreSQL Database class."""

    def __init__(self):
        self.host = config.host
        self.username = config.username
        self.password = config.password
        self.port = config.port
        self.databasebname = config.databaseName
        self.conn = None
        self.cur = None

    def connect(self):
        """Connect to a Postgres database."""
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    username=self.username,
                    password=self.password,
                    port=self.port,
                    databasename=self.dbname
                )
                self.cur = self.conn.cursor()
                try:
                    commands = createtable.create_table()
                    for command in commands:
                        self.cur.execute(command)

                    # close communication with the PostgreSQL database server
                except Exception as e:
                    pass
                self.conn.commit()
                self.cur.close()
            except (Exception, psycopg2.DatabaseError) as error:\
                print(error)
            finally:
                print('Connection done successfully.')
# Connection established to: (
#    'PostgreSQL 11.5, compiled by Visual C++ build 1914, 64-bit',
# )
#

    def insert_rows(self, query):
        print("hellooo")
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        print("hy")
        self.conn.commit()
        print("bye")
        self.cur.close()