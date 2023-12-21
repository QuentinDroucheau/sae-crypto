import cryptography
from cryptography.fernet import Fernet
from PIL import Image

def compare_images(image_path1, image_path2):
    img1 = Image.open(image_path1)
    img2 = Image.open(image_path2)

    if img1.size != img2.size or img1.mode != img2.mode:
        return "Les images sont de tailles ou de modes différents."

    diff_pixels = []
    width, height = img1.size
    cpt = 0

    for y in range(height):
        for x in range(width):
            pixel1 = img1.getpixel((x, y))
            pixel2 = img2.getpixel((x, y))

            if pixel1 != pixel2:
                if pixel1 - pixel2 > 0:
                    diff_pixels.append(1)
                else:
                    diff_pixels.append(0)
            cpt+=1

    return diff_pixels

def aes_encrypt(message, key):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

def aes_decrypt(encrypted_message, key):
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()



message = "Hello World !"
key = Fernet.generate_key()
encrypted_message = aes_encrypt(message, key)
decrypted_message = aes_decrypt(encrypted_message, key)

print("Message: ", message)
print("Key: ", key)
print("Encrypted message: ", encrypted_message)
print("Decrypted message: ", decrypted_message)
print("Message == Decrypted message: ", message == decrypted_message)


