import qrcode

# Function to generate QR code
def generate_qr_code(data, filename):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # size of each box in pixels
        border=4,  # width of the border (minimum is 4)
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image
    img.save(filename)

# Example usage
data = "https://www.linkedin.com/in/deepankar-nankani-05577654/"
filename = "linkedin_qr_code.png"
generate_qr_code(data, filename)
print(f"QR code saved as {filename}")


