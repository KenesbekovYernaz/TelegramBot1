import qrcode

class QR_Code:
	def __init__(self, qr_info, qr_name):
		img = qrcode.make(qr_info)
		img.save(f"qr_codes\\{qr_name}")

