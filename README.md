# PRODIGY_CS_02

Image Encryption/Decryption Tool
Overview:

This Python script demonstrates a simple image encryption and decryption tool using the Python Imaging Library (PIL) and numpy. It allows users to encrypt an image by swapping color channels and decrypt it back to the original format.
Features

    Encryption: Swaps red and blue channels of the image.
    Decryption: Reverses the channel swapping to restore the original image.
    Command-line interface for ease of use.

Requirements

    Python 3.x
    Pillow (pip install pillow)

Usage

    Clone the repository:

    bash

git clone https://github.com/yourusername/image-encryption-tool.git
cd image-encryption-tool

Install dependencies:

pip install -r requirements.txt

Run the script:

    python image_encrypt_decrypt.py

Instructions

    Choose E for encryption, D for decryption, or Q to quit.
    Provide paths for input and output images as prompted.
    Encrypted images will be saved with _encrypted appended to the filename.

Example

Encrypt an image:

Enter 'E' for encryption, 'D' for decryption, or 'Q' to quit: E
Enter the path of the image you want to encrypt: path/to/your/image.jpg
Enter the path where you want to save the encrypted image: path/to/save/encrypted_image.jpg
Image encrypted and saved as path/to/save/encrypted_image.jpg

Decrypt the encrypted image:

Enter 'E' for encryption, 'D' for decryption, or 'Q' to quit: D
Enter the path of the encrypted image you want to decrypt: path/to/encrypted_image.jpg
Enter the path where you want to save the decrypted image: path/to/save/decrypted_image.jpg
Image decrypted and saved as path/to/save/decrypted_image.jpg

License

This project is licensed under the  GNU GENERAL PUBLIC LICENSE- see the LICENSE file for details.
