import qrcode




qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=0
    )#设置二维码的大小
qr.add_data("https://www.baidu.com")
qr.make(fit=True)
img = qr.make_image()

img.save("test.png")


            




    


