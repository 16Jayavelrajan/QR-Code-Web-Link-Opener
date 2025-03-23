import qrcode
import webbrowser
from pyzbar.pyzbar import decode
from PIL import Image

def generate_qr(url, filename='Myqrcode.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f'QR Code saved as {filename}')

def scan_qr(image_path):
    img = Image.open(image_path)
    decoded_data = decode(img)
    if decoded_data:
        url = decoded_data[0].data.decode('utf-8')
        print(f'Opening URL: {url}')
        webbrowser.open(url)
    else:
        print('No QR code found in the image.')

if __name__ == "__main__":
    url = input("Enter the URL to generate QR code: ")
    generate_qr(url)
    print("Scan the QR code with your phone to open the website.")

