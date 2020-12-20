import scrapy


class ChampStatsSpider(scrapy.Spider):
  name = 'champ_stats'

  def start_requests(self):
    urls = [
      # 'https://leagueoflegends.fandom.com/wiki/Jhin/TFT',
      # 'https://leagueoflegends.fandom.com/wiki/Lillia/TFT',
      'https://leagueoflegends.fandom.com/wiki/Kalista/TFT'
    ]
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    # Parse traits
    trait_container = (response
      .xpath('//tr[td[span[@data-type="trait"]]][1]')
      .xpath('.//span[@data-type="trait"]'))
    traits = [trait.attrib['data-param'] for trait in trait_container]

    # Parse stats
    stats = response.css('aside.pi-theme-teamfight-champion-bottom')
    def getStat(x):
      sel = (stats
        .xpath(f'//div[@data-source="{x}"][1]')
        .css('div.pi-data-value ::text')
        .getall())
      text = ''.join(''.join(sel).split())

      if ('/' in text):
        return [float(i) for i in text.split('/')][0]
      else:
        try:
          return float(text)
        except:
          return text

    yield {
      'name': response.url.split('/')[-2],
      'stats': {
        'armor': getStat('arm'),
        'attack_damage': getStat('ad'),
        'attack_speed': getStat('as'),
        'health': getStat('hp'),
        'magic_resist': getStat('mr'),
        'mana': getStat('mana'),
        'mana_start': getStat('startmana'),
        'range': getStat('range'),
      },
      'traits': traits
    }
