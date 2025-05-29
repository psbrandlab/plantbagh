import feedparser
from markdownify import markdownify as md
import os
import hashlib

# RSS feed URL (update this!)
rss_url = "https://www.plantbagh.com/feeds/posts/default?alt=rss"

# Create folder
os.makedirs("rss-posts", exist_ok=True)

# Parse RSS
feed = feedparser.parse(rss_url)

for entry in feed.entries:
    title = entry.title
    link = entry.link
    published = entry.published
    content = entry.get("content", [{"value": ""}])[0]["value"]

    # Generate a unique filename based on the link
    filename = hashlib.md5(link.encode()).hexdigest()[:8]
    md_filename = f"rss-posts/{published[:10]}-{filename}.md"

    if not os.path.exists(md_filename):
        with open(md_filename, "w", encoding="utf-8") as f:
            f.write(f"# [{title}]({link})\n")
            f.write(f"**Published**: {published}\n\n")
            f.write(md(content))

print("RSS posts saved to 'rss-posts/' folder.")
