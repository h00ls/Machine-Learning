import qrcode

qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=0
    )#设置二维码的大小
qr.add_data("http://www.sec.gov/edgar.shtml")
qr.make(fit=True)
img = qr.make_image()

filename = "test.png"

print(filename)
img.save(filename)
