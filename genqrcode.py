import qrcode


#สร้่าง QRCode
qr = qrcode.QRCode()
qr.add_data('https://www.google.com')
qr.make()


#บันทึก qrcode เก็บลงโปรเจคต์
img = qr.make_image()
img.save('demo_qrcode.png')
