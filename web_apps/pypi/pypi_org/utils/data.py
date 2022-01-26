from passlib.handlers.sha2_crypt import sha512_crypt as crypto


def get_sql_lite_conn_str(db_file: str):
    db_file_stripped = db_file.strip()
    if not db_file or not db_file_stripped:
        # db_file = '../db/pypi_org.db'
        raise Exception("SQL lite DB file is not specified.")

    return 'sqlite:///' + db_file_stripped


def to_hash(txt: str) -> str:
    return crypto.encrypt(txt, rounds=177187)


def is_hash_correct(hash: str, txt: str) -> bool:
    return crypto.verify(txt, hash)