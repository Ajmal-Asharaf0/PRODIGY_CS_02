from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path):
    try:
        # Open the image file
        img = Image.open(image_path)
        # Convert image to RGB mode if it's not
        img = img.convert('RGB')

        # Get image data as a numpy array
        img_array = np.array(img)

        # Perform encryption operation on pixel values
        # Example: Swapping red and blue channels
        encrypted_img_array = img_array[:, :, [2, 1, 0]]

        # Create a new image from the encrypted numpy array
        encrypted_img = Image.fromarray(encrypted_img_array)

        # Save encrypted image
        encrypted_img.save(output_path)
        print(f"Image encrypted and saved as {output_path}")
    except IOError:
        print(f"Unable to load image {image_path}")

def decrypt_image(encrypted_path, output_path):
    try:
        # Open the encrypted image file
        encrypted_img = Image.open(encrypted_path)

        # Convert image to RGB mode if it's not
        encrypted_img = encrypted_img.convert('RGB')

        # Get image data as a numpy array
        encrypted_img_array = np.array(encrypted_img)

        # Perform decryption operation (reverse of encryption)
        # Example: Swapping back red and blue channels
        decrypted_img_array = encrypted_img_array[:, :, [2, 1, 0]]

        # Create a new image from the decrypted numpy array
        decrypted_img = Image.fromarray(decrypted_img_array)

        # Save decrypted image
        decrypted_img.save(output_path)
        print(f"Image decrypted and saved as {output_path}")
    except IOError:
        print(f"Unable to load image {encrypted_path}")

# Main program
if __name__ == "__main__":
    print("Welcome to the Image Encryption/Decryption Tool!")

    while True:
        choice = input("Enter 'E' for encryption, 'D' for decryption, or 'Q' to quit: ").upper()

        if choice == 'E':
            original_image_path = input("Enter the path of the image you want to encrypt: ")
            output_encrypted_path = input("Enter the path where you want to save the encrypted image: ")
            encrypt_image(original_image_path, output_encrypted_path)

        elif choice == 'D':
            encrypted_image_path = input("Enter the path of the encrypted image you want to decrypt: ")
            output_decrypted_path = input("Enter the path where you want to save the decrypted image: ")
            decrypt_image(encrypted_image_path, output_decrypted_path)

        elif choice == 'Q':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 'E', 'D', or 'Q'.")
