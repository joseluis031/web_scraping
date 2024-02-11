from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

def encrypt(message, key):
    # Asegurarse de que la clave sea de 32 bytes para AES-256
    key = key.ljust(32, b'\0')[:32]

    # Generar un vector de inicialización (IV) aleatorio
    iv = b'\0' * 16  # Puedes generar uno aleatorio con os.urandom(16)

    # Crear un objeto AES con la clave y el modo CBC
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())

    # Crear un objeto de cifrado
    encryptor = cipher.encryptor()

    # Aplicar relleno PKCS7 al mensaje
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_message = padder.update(message) + padder.finalize()

    # Cifrar el mensaje
    ciphertext = encryptor.update(padded_message) + encryptor.finalize()

    return (iv, ciphertext)

def decrypt(ciphertext, key, iv):
    # Asegurarse de que la clave sea de 32 bytes para AES-256
    key = key.ljust(32, b'\0')[:32]

    # Crear un objeto AES con la clave y el modo CBC
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())

    # Crear un objeto de descifrado
    decryptor = cipher.decryptor()

    # Descifrar el mensaje
    decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()

    # Quitar el relleno PKCS7
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    original_message = unpadder.update(decrypted_message) + unpadder.finalize()

    return original_message

# Ejemplo de uso
mensaje_original = b"Hola, esto es un mensaje secreto."
clave = b"UnaClaveSecreta"

iv, mensaje_cifrado = encrypt(mensaje_original, clave)
mensaje_descifrado = decrypt(mensaje_cifrado, clave, iv)

print("Mensaje original:", mensaje_original)
print("Mensaje cifrado:", mensaje_cifrado)
print("Mensaje descifrado:", mensaje_descifrado.decode())
