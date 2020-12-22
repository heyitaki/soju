import scrapy


class ChampStatsSpider(scrapy.Spider):
    name = "champ_stats"
    custom_settings = {
        "FEEDS": {
            "../../data/10/25/champ-stats.json": {
                "format": "json",
                "encoding": "utf-8",
                "indent": 2,
                "overwrite": True,
            }
        }
    }
    urls = []

    def start_requests(self):
        start_url = "https://leagueoflegends.fandom.com/wiki/Category:TFT_Set_4"
        yield scrapy.Request(url=start_url, callback=self.parse_champ_names)

    def parse_champ_names(self, response):
        links = response.css('a.category-page__member-link[href*="/TFT"]')
        urls = [
            "https://leagueoflegends.fandom.com" + link.attrib["href"] for link in links
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_champ)

    def parse_champ(self, response):
        # Parse traits
        trait_container = response.xpath(
            '//tr[td[span[@data-type="trait" and @data-set="4"]]][1]'
        ).xpath('.//span[@data-type="trait"]')
        traits = [trait.attrib["data-param"] for trait in trait_container]

        # Parse stats
        stats = response.css("aside.pi-theme-teamfight-champion-bottom")[0]

        def getStat(x):
            sel = (
                stats.xpath(f'.//div[@data-source="{x}"][1]')
                .css("div.pi-data-value ::text")
                .getall()
            )
            text = "".join("".join(sel).split())

            if "/" in text:
                return [float(i) for i in text.split("/")][0]
            else:
                try:
                    return float(text)
                except:
                    return text

        yield {
            "name": response.url.split("/")[-2],
            "stats": {
                "armor": getStat("arm"),
                "attack_damage": getStat("ad"),
                "attack_speed": getStat("as"),
                "health": getStat("hp"),
                "magic_resist": getStat("mr"),
                "mana": getStat("mana"),
                "mana_start": getStat("startmana"),
                "range": getStat("range"),
            },
            "traits": traits,
        }
