def create_table():
    sql=''''create TABLE conversation(
            id SERIAL primary key,
            speaker varchar(100),
            text varchar(100),
            time TIMESTAMP);'''
    return sql