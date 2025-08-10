from captcha.image import ImageCaptcha
import random, string


text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


ImageCaptcha().write(text, 'captcha.png')

print("CAPTCHA text:", text)
print("Saved as captcha.png")
