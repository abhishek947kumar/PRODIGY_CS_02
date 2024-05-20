from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j] # type: ignore

            # swapping red and blue channels
            encrypted_pixel = (b, g, r)

            pixels[i, j] = encrypted_pixel # type: ignore

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j] # type: ignore

            # swapping red and blue channels back
            decrypted_pixel = (b, g, r)

            pixels[i, j] = decrypted_pixel # type: ignore

    img.save(output_path)
    print("Image decrypted successfully!")

 # image path
input_image = r"C:\Users\Abhishek Kumar\OneDrive\Desktop\images.jpeg"
encrypted_image = r"C:\Users\Abhishek Kumar\OneDrive\Desktop\decrypted_image.jpeg"
decrypted_image = r"C:\Users\Abhishek Kumar\OneDrive\Desktop\encrypted_image.jpeg"


# Encrypt the image
encrypt_image(input_image, encrypted_image, key=None)

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image, key=None)
