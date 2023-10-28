import shlex
from common.utils import get_dir
import pathlib
import os
from subprocess import call


d1 =pathlib.Path(__file__).resolve().parent
d2 = get_dir()

key_path = d2 / "key.pem"
cert_path = d2 / "cert.pem"
openssl_params = f"req -x509 -newkey rsa:2048 -subj '/CN=localhost' -keyout {key_path} -out {cert_path} -nodes -days 365"

os.system(f"openssl {openssl_params}")


# openssl_params_list = shlex.split(openssl_params)  # TO FIX
# call(["openssl", openssl_params_list])
