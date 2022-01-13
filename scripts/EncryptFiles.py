from os import path
from Crypto import Cipher
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from FileSystem import *

def generate_key():
    """
    Function responsible for generating an RSA key pair.
    """
    # add the directory where the public and private key will be saved.
    save_path = load_path()
    directory_private = os.path.join(save_path, 'private.pem')
    directory_public = os.path.join(save_path, 'public.pem')
    
    # Generate the public and private key.
    key = RSA.generate(2048)
      
    private_key = key.export_key()
    outfile = open(directory_private, "wb")
    outfile.write(private_key)
    outfile.close()

    public_key = key.publickey().export_key()
    outfile = open(directory_public, "wb")
    outfile.write(public_key)
    outfile.close()


def encryptTextFile(path_public_key, path_file):
    """
    Function responsible for encrypting text files.
    
    param path_public_key: public key directory.
    param path_file: directory of the file to be encrypted.
    """
    # Extract the contents of the file.
    data = (open(path_file).read()).encode("utf-8")
    # Generates a file that will be encrypted.
    file = open(fileName(path_file) + ".bin", 'wb')

    # Open the public key.
    recipient_key = RSA.import_key(open(path_public_key).read())
    # Generate an AES key.
    session_key = get_random_bytes(16)
    # Encrypt the session key with the public RSA key.
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)
    
    # Encrypt data with AES session key.
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    
    for i in (enc_session_key, cipher_aes.nonce, tag, ciphertext):
        file.write(i)
    file.close()


def decryptTextFile(path_private_key, path_file):
    """
    Function responsible for decrypting text files.

    param path_private_key: private key directory.
    param path_file: directory of the file to be decrypted.
    """
    file = open(path_file, "rb")
    private_key = RSA.import_key(open(path_private_key).read())

    enc_session_key, nonce, tag, ciphertext = \
        [file.read(i) for i in (private_key.size_in_bytes(), 16, 16, -1)]

    # Decrypt the session key with the private RSA key.
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    # Decrypt the data with the AES session key.
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)

    string = data.decode("utf-8")
    # Generates new decrypted text file.
    new_file = open(fileName(path_file) + '_decrypt.txt', "a")
    new_file.write(string)
    new_file.close()
    file.close()