from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():

    search = request.args.get("search", "")
    category = request.args.get("category", "")

    conn = sqlite3.connect("news.db")
    cur = conn.cursor()

    query = """
    SELECT *
    FROM articles
    WHERE title LIKE ?
    """

    params = [f"%{search}%"]

    if category:
        query += " AND category = ?"
        params.append(category)

    query += """
    ORDER BY id DESC
    LIMIT 100
    """

    articles = cur.execute(
        query,
        params
    ).fetchall()

    trending = cur.execute("""
        SELECT *
        FROM articles
        ORDER BY id DESC
        LIMIT 5
    """).fetchall()

    total_news = cur.execute(
        "SELECT COUNT(*) FROM articles"
    ).fetchone()[0]

    sport = cur.execute(
        "SELECT COUNT(*) FROM articles WHERE category='sport'"
    ).fetchone()[0]

    politics = cur.execute(
        "SELECT COUNT(*) FROM articles WHERE category='politics'"
    ).fetchone()[0]

    technology = cur.execute(
        "SELECT COUNT(*) FROM articles WHERE category='technology'"
    ).fetchone()[0]

    gaming = cur.execute(
        "SELECT COUNT(*) FROM articles WHERE category='gaming'"
    ).fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        articles=articles,
        trending=trending,
        search=search,
        category=category,
        total_news=total_news,
        sport=sport,
        politics=politics,
        technology=technology,
        gaming=gaming
    )


@app.route("/api/news")
def api_news():

    conn = sqlite3.connect("news.db")
    cur = conn.cursor()

    rows = cur.execute("""
        SELECT
            title,
            link,
            source,
            published
        FROM articles
        ORDER BY id DESC
        LIMIT 20
    """).fetchall()

    conn.close()

    news = []

    for row in rows:

        news.append({
            "title": row[0],
            "link": row[1],
            "source": row[2],
            "published": row[3]
        })

    return {
        "status": "success",
        "count": len(news),
        "news": news
    }


@app.route("/stats")
def stats():

    conn = sqlite3.connect("news.db")
    cur = conn.cursor()

    total = cur.execute(
        "SELECT COUNT(*) FROM articles"
    ).fetchone()[0]

    sport = cur.execute(
        "SELECT COUNT(*) FROM articles WHERE category='sport'"
    ).fetchone()[0]

    politics = cur.execute(
        "SELECT COUNT(*) FROM articles WHERE category='politics'"
    ).fetchone()[0]

    technology = cur.execute(
        "SELECT COUNT(*) FROM articles WHERE category='technology'"
    ).fetchone()[0]

    gaming = cur.execute(
        "SELECT COUNT(*) FROM articles WHERE category='gaming'"
    ).fetchone()[0]

    conn.close()

    return {
        "total_news": total,
        "sport": sport,
        "politics": politics,
        "technology": technology,
        "gaming": gaming
    }


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )