import qrcode

def generate_attendance_qr(url, filename="attendance_qr.png"):
    """
    Generate a QR code for the attendance web app
    url: The URL of your Flask app (e.g., 'http://192.168.1.100:5000')
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")
    print(f"Students can scan this to access: {url}")

# Replace with your computer's IP address and port
# To find your IP: Windows (ipconfig), Mac/Linux (ifconfig)
generate_attendance_qr("http://192.168.1.100:5000")