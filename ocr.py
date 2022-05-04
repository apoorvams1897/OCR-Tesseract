from PIL import Image
import base64
import pytesseract
import io

async def image_to_string(file_obj):
  pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
  imgstring = base64.b64encode(file_obj.file.read())
  image_string = io.BytesIO(base64.b64decode(imgstring))
  image = Image.open(image_string)
  new_image = (pytesseract.image_to_string(image))
  return new_image
