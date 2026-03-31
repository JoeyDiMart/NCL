from pyzbar.pyzbar import decode
from PIL import Image

# Load QR code image
qr_code = decode(Image.open("qr_code.png"))

# Extract and print metadata
for obj in qr_code:
    print("Decoded Data:", obj.data.decode("utf-8"))
    print("Type:", obj.type)
    print("QR Metadata:", obj)  # Inspect this for error correction level
