
from database import postgresdb


def insert_detail(speaker, text):
    sql = f"""INSERT INTO talk(speaker, text)
                 VALUES('{speaker}', '{text}');"""
    db_obj = postgresdb.Database()
    db_obj.connect()
    db_obj.insert_rows(sql)