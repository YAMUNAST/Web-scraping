import scrapy

class ESPNFootballSpider(scrapy.Spider):
    name = "espn_football"
    allowed_domains = ["espn.com"]
    start_urls = ["https://www.espn.com/soccer/scoreboard"]

    def parse(self, response):
        matches = response.css("section.Scoreboard")
        for match in matches:
            yield {
                "team1": match.css(".ScoreCell__TeamName::text").getall()[0],
                "team2": match.css(".ScoreCell__TeamName::text").getall()[1],
                "score": match.css(".ScoreCell__Score::text").getall(),
                "date": response.css(".Scoreboard__Date::text").get(),
            }
