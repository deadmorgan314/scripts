import qrcode
def Qrcode_Maker(data):
    qr =qrcode.QRCode(version=1,box_size=10,border=5)
    qr.add_data(data)
    qr.make(fit=True)
    pic = qr.make_image()
    pic.save('myqrcode.png')

data = input()
Qrcode_Maker(data)