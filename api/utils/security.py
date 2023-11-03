from cryptography.fernet import Fernet
from django.conf import settings


def encrypt_string(string_to_encrypt):
    """
    Encrypt String

    :param str string_to_encrypt: Unencrypted String

    :return: str
    """

    cipher = Fernet(settings.FERNET_KEY)

    if not isinstance(string_to_encrypt, bytes):
        string_to_encrypt = string_to_encrypt.encode('UTF-8')

    return cipher.encrypt(string_to_encrypt).decode('UTF-8')


def decrypt_string(string_to_decrypt):
    """
    Decrypt String

    :param str string_to_decrypt: Encrypted String

    :return: str
    """

    cipher = Fernet(settings.FERNET_KEY)

    if not isinstance(string_to_decrypt, bytes):
        string_to_decrypt = string_to_decrypt.encode('UTF-8')

    return cipher.decrypt(string_to_decrypt).decode('UTF-8')
