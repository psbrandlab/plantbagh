import feedparser
from markdownify import markdownify as md
from datetime import datetime
import os
import hashlib

# 🔁 Replace with your actual RSS feed URL
FEED_URL = "https://plantbagh.blogspot.com/feeds/posts/default?alt=rss"
POST_DIR = "rss-posts"

feed = feedparser.parse(FEED_URL)

os.makedirs(POST_DIR, exist_ok=True)

for entry in feed.entries:
    title = entry.title
    link = entry.link
    published = entry.published
    content = entry.get("content", [{}])[0].get("value", entry.get("summary", ""))

    # Format filename like 2025-05-29-title.md
    date_obj = datetime.strptime(published, '%a, %d %b %Y %H:%M:%S %z')
    slug = "-".join(title.lower().split())[:50]
    filename = f"{POST_DIR}/{date_obj.strftime('%Y-%m-%d')}-{slug}.md"

    # Skip if file already exists
    if os.path.exists(filename):
        continue

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n")
        f.write(f"*Published on {date_obj.strftime('%Y-%m-%d')}*\n\n")
        f.write(md(content))
        f.write(f"\n\n[Read more]({link})")

print("✅ RSS fetch complete.")
