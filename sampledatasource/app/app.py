import psycopg2


def main():
    print("Starting app...")
    conn = connect()
    mock_data(conn)


def connect():
    return psycopg2.connect(
        host="postgres",
        user="postgres",
        password="postgres",
        dbname="postgres"
    )


def mock_data(conn):
    drop_table_sql = """
        DROP TABLE IF EXISTS test
    """

    create_table_sql = """
        CREATE TABLE test (
            col1 int,
            col2 varchar
        )
    """

    insert_sql = """
        insert into test
        select
            generate_series(1, 100000)
            , (generate_series(1, 100000) * 76)::text
    """

    with conn.cursor() as cur:
        cur.execute(drop_table_sql)
        cur.execute(create_table_sql)
        cur.execute(insert_sql)

    print("Committing!")
    conn.commit()


if __name__ == '__main__':
    main()
