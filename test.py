import pyotp
import qrcode

uri = "otpauth://totp/ladibanks1?secret=MPNQ5BLRZ2YDQGIXUVK72BH25LADKGOA&issuer=Namecheap"
img = qrcode.make(uri)
img.save("namecheap.png")
