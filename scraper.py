# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html


def release(html):
  return {
    'version': html.xpath('./span[@class="release-number"]/a/text()')[0],
    'download': 'https://www.python.org' + html.xpath('./span[@class="release-number"]/a/@href')[0],
    'date': html.xpath('./span[@class="release-date"]/text()')[0],
    'notes': html.xpath('./span[@class="release-enhancements"]/a/@href')[0]
  }


page = scraperwiki.scrape('http://python.org/downloads')
html = lxml.html.fromstring(page)
releases = list(map(release, html.cssselect('.download-list-widget li')))

for r in releases:
  scraperwiki.sqlite.save(unique_keys=['version'], data=r)

# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
