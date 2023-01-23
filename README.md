# TwitterScrapping
snscrape is a scraper for social networking services (SNS). It scrapes things like user profiles, hashtags, or searches and returns the discovered items, e.g. the relevant posts.

# snscrape
snscrape is a scraper for social networking services (SNS). It scrapes things like user profiles, hashtags, or searches and returns the discovered items, e.g. the relevant posts.

The following services are currently supported:

* Facebook: user profiles, groups, and communities (aka visitor posts)
* Instagram: user profiles, hashtags, and locations
* Mastodon: user profiles and toots (single or thread)
* Reddit: users, subreddits, and searches (via Pushshift)
* Telegram: channels
* Twitter: users, user profiles, hashtags, searches, tweets (single or surrounding thread), list posts, and trends
* VKontakte: user profiles
* Weibo (Sina Weibo): user profiles

## Requirements
snscrape requires Python 3.8 or higher. The Python package dependencies are installed automatically when you install snscrape.

Note that one of the dependencies, lxml, also requires libxml2 and libxslt to be installed.

## Installation
    pip3 install snscrape
    
 Using snscrape
After downloading snscrape, you’ll be able to utilize it in a couple of different ways. The most straightforward way is through its command-line interface (CLI) commands in the command prompt/terminal. If you are not comfortable with using a terminal, you can instead use Python to execute CLI commands.

Otherwise, snscrape does have an official Python wrapper. However, it is currently undocumented and lacks the simplicity of its CLI commands. The upside to using the Python wrapper is that you can easily interact with the data and tweet objects after scraping.

Regardless of what method you use, I cover them all below. In this tutorial, you’ll scrape a user's tweets and scrape historical tweets with a text search.

One last note: I’ve seen people using Tweepy with snscrape to access data from tweets. This is inefficient as you’re scraping twice. You should not use Tweepy unless you only have access to tweet IDs or URLs or you need the granularity. snscrape’s tweet object already has a lot of information available. The image below shows the data you can access with snscrape. The attributes in the image should map exactly to how they’re stored inside the actual object.

