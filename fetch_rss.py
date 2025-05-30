import feedparser
import os
from datetime import datetime

rss_url = 'https://www.plantbagh.com/feeds/posts/default?alt=rss'
feed = feedparser.parse(rss_url)

for entry in feed.entries:
    title = entry.title.replace(" ", "-").replace("/", "-")
    pub_date = datetime(*entry.published_parsed[:6]).strftime("%Y-%m-%d")
    filename = f"rss-posts/{pub_date}-{title}.md"

    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# [{entry.title}]({entry.link})\n\n")
            f.write(f"_Published: {entry.published}_\n\n")
            f.write(f"{entry.summary}")
