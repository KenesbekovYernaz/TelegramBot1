from pycoingecko import CoinGeckoAPI
import datetime
cg = CoinGeckoAPI()

# Bitcoin, Ethereum, Tether, Cardano, Binance coin

class Coin_Convert:
	def get_coins(self):
		info = cg.get_price(ids=["bitcoin", "ethereum", "tether", "cardano", "binancecoin"], vs_currencies='usd')

		data = f"""<b>🪙Coins {datetime.datetime.today()}</b>
		Bitcoin: <code>{info['bitcoin']['usd']}</code> USD
		Ethereum <code>{info['ethereum']['usd']}</code> USD
		Tether: <code>{info['tether']['usd']}</code> USD
		Cardano: <code>{info['cardano']['usd']}</code> USD
		Binance coin: <code>{info['binancecoin']['usd']}</code> USD
		"""

		return data