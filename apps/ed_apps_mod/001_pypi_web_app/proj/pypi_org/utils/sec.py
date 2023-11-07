import hashlib

from passlib.handlers.sha2_crypt import sha512_crypt as crypto


def pass_to_hash(txt: str) -> str:
    # res will be diff every calc
    return crypto.encrypt(txt, rounds=177187)


def is_pass_hash_correct(hash: str, txt: str) -> bool:
    return crypto.verify(txt, hash)


def txt_to_hash(txt: str) -> str:
    txt = 'py__{}__pi'.format(txt)
    # res will be the same every calc
    return hashlib.sha512(txt.encode('utf-8')).hexdigest()