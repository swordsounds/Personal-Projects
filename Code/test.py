import easyocr

reader = easyocr.Reader(['en'])
reader.readtext('KGBIS New Logo.jpg', detail = 0)