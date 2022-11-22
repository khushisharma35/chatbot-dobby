def create_table():
    sql=['''create TABLE talk(
            id SERIAL primary key,
            speaker varchar(100),
            text varchar(100),
            time TIMESTAMP default CURRENT_TIMESTAMP);''']
    return sql
