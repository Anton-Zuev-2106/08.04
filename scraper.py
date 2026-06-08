import feedparser

from database import (
    create_db,
    insert_article
)


RSS_FEEDS = {

    "BBC":
    "https://feeds.bbci.co.uk/news/rss.xml",

    "TechCrunch":
    "https://techcrunch.com/feed/",

    "Reuters":
    "https://www.reutersagency.com/feed/?best-topics=world&post_type=best"
}


def scrape():

    create_db()

    for source, url in RSS_FEEDS.items():

        print(f"\nИсточник: {source}")

        feed = feedparser.parse(url)

        for entry in feed.entries[:20]:

            title = entry.get(
                "title",
                ""
            )

            link = entry.get(
                "link",
                ""
            )

            description = entry.get(
                "summary",
                ""
            )

            published = entry.get(
                "published",
                ""
            )

            insert_article(
                title,
                link,
                description,
                source,
                published
            )

            print(title[:70])


if __name__ == "__main__":

    scrape()