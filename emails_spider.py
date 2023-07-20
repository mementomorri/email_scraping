from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


class EMailsSpider(CrawlSpider):
    name = "emails"
    allowed_domains = ["scrapebay.com"]
    start_urls = ["https://www.scrapebay.com/"]

    rules = (
        Rule(LinkExtractor(), callback="parse_item",
             follow=False),
    )

    @staticmethod
    def parse_item(response):
        emails = re.findall(r'[\w.]+@[\w.]+\.[\w]+', response.text)

        for email in emails:
            if 'bootstrap' not in email:
                yield {response.url: email}
# scrapy runspider emails_spider.py -o scraped_emails.json -L WARN
