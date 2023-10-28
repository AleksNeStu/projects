import ssl

from anyio import connect_tcp, run
from anyio.abc import SocketAttribute

from common.utils import get_dir

# Connecting to this server can then be done as follows:

dir = get_dir()
key_path = dir / "key.pem"
cert_path = dir / "cert.pem"

async def main_client():
    # These two steps are only required for certificates that are not trusted by the
    # installed CA certificates on your machine, so you can skip this part if you
    # use Let's Encrypt or a commercial certificate vendor
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations(cafile=cert_path)

    async with await connect_tcp('localhost', 5555, ssl_context=context) as client:
        print('Connected to', client.extra(SocketAttribute.remote_address))

        await client.send(b'Client 888\n')
        response = await client.receive()
        print(response)

run(main_client)

