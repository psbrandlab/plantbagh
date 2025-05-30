import feedparser
import os
import hashlib
from datetime import datetime

# CHANGE THIS TO YOUR BLOGGER RSS FEED
RSS_FEED_URL = 'https://plantbagh.blogspot.com/feeds/posts/default?alt=rss'
OUTPUT_DIR = 'rss-posts'
MAX_POSTS = 20  # change as needed

feed = feedparser.parse(RSS_FEED_URL)

def slugify(title):
    return ''.join(c if c.isalnum() or c in [' ', '-', '_'] else '-' for c in title).strip().replace(' ', '-')

for entry in feed.entries[:MAX_POSTS]:
    title = entry.title
    published = entry.published
    date = datetime.strptime(published, '%a, %d %b %Y %H:%M:%S %z').strftime('%Y-%m-%d')
    slug = slugify(title)
    filename = f"{date}-{slug}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    if not os.path.exists(filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write(f"*Published on {published}*\n\n")
            f.write(entry.summary)

print("RSS posts saved to:", OUTPUT_DIR)
