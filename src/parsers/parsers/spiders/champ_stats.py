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
    stats = response.css('aside.pi-theme-teamfight-champion-bottom')

    def get(x):
      sel = stats.xpath(f'//div[@data-source="{x}"][1]').css('div.pi-data-value ::text').getall()
      text = ''.join(''.join(sel).split())
      
      if ('/' in text):
        return [float(i) for i in text.split('/')]
      else:
        try:
          return float(text)
        except:
          return text

    yield {
      'name': response.url.split('/')[-2],
      'stats': {
        'armor': get('arm'),
        'attack_damage': get('ad'),
        'attack_speed': get('as'),
        'crit_chance': .25,
        'crit_modifier': 1.5,
        'health': get('hp'),
        'magic_resist': get('mr'),
        'mana': get('mana'),
        'mana_start': get('startmana'),
        'range': get('range'),
      }
    }
