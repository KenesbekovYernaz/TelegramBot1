from SimpleQIWI import *
from time import sleep
import config

class MY_QIWI:
	api = QApi(token=config.QIWI_TOKEN, phone=config.QIWI_PHONE)

	def get_balance_qiwi(self):
		balance = self.api.balance
		return f"🥝Balance QIWI: {balance}"

	def qiwi_pay(self, price, account_user, comment_pay=None):
		self.api.pay(account=account_user, amount=price, comment=comment_pay)

	def qiwi_create_key(self, price):
		api = self.api

		comment = api.bill(price)
		return comment

	def qiwi_bill(self):
		api = self.api

		api.start()

		while True:
			if api.check(comment):
				return "✅Платеж прашол!"
				break
			sleep(5)

		api.stop()



