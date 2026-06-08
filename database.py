import sqlite3

DB_NAME = "news.db"


def create_db():

    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS articles(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        link TEXT UNIQUE,
        description TEXT,
        source TEXT,
        published TEXT,
        category TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_article(
    title,
    link,
    description,
    source,
    published
):

    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()

    try:

        cur.execute("""
        INSERT INTO articles
        (
            title,
            link,
            description,
            source,
            published
        )
        VALUES(?,?,?,?,?)
        """,
        (
            title,
            link,
            description,
            source,
            published
        ))

        conn.commit()

    except:

        pass

    conn.close()


if __name__ == "__main__":

    create_db()

    print("База создана")