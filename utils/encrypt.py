import hashlib


def md5(str):
    hash_object = hashlib.md5()
    hash_object.update(str.encode())
    return hash_object.hexdigest()