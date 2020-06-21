import psycopg2
import time

from psycopg2._psycopg import OperationalError


def main():
    conn = connect()
    print("Sleeping...")
    time.sleep(10)
    create_view(conn)


def connect():
    print("Connecting to localhost...")
    try:
        return psycopg2.connect(
            host="localhost",
            user="postgres",
            password="postgres",
            dbname="postgres"
        )
    except OperationalError as oe:
        print("Trying docker internal host instead...")
        return psycopg2.connect(
            host="host.docker.internal",
            user="postgres",
            password="postgres",
            dbname="postgres"
        )


def create_view(conn):
    print("Creating view")
    with conn.cursor() as cur:
        cur.execute(
            """
            DROP TABLE IF EXISTS test_view_staging
            """
        )

        cur.execute(
            """
            CREATE TABLE test_view_staging AS
            select
              col1 * 4 as col1
              , col2
            from test
            order by random()
            """
        )

        conn.commit()
        print("Created table")

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS test_view AS
            SELECT 1
            """
        )

        cur.execute(
            """
            ALTER TABLE test_view RENAME TO test_view_old
            """
        )

        cur.execute(
            """
            ALTER TABLE test_view_staging RENAME TO test_view
            """
        )

        conn.commit()
        print("Swapped table")

        cur.execute(
            """
            DROP TABLE test_view_old
            """
        )

        conn.commit()
        print("Cleaned up old table")


if __name__ == '__main__':
    main()
