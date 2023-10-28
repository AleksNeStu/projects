"""
TLS (Transport Layer Security), the successor to SSL (Secure Sockets Layer), is the supported way of providing authenticity and confidentiality for TCP streams in AnyIO.

TLS is typically established right after the connection has been made. The handshake involves the following steps:

Sending the certificate to the peer (usually just by the server)

Checking the peer certificate(s) against trusted CA certificates

Checking that the peer host name matches the certificate

Obtaining a server certificate
There are three principal ways you can get an X.509 certificate for your server:

Create a self signed certificate

Use certbot or a similar software to automatically obtain certificates from Let’s Encrypt

Buy one from a certificate vendor

The first option is probably the easiest, but this requires that the any client connecting to your server adds the self signed certificate to their list of trusted certificates. This is of course impractical outside of local development and is strongly discouraged in production use.

The second option is nowadays the recommended method, as long as you have an environment where running certbot or similar software can automatically replace the certificate with a newer one when necessary, and that you don’t need any extra features like class 2 validation.

The third option may be your only valid choice when you have special requirements for the certificate that only a certificate vendor can fulfill, or that automatically renewing the certificates is not possible or practical in your environment.

Using self signed certificates
To create a self signed certificate for localhost, you can use the openssl command line tool:

openssl req -x509 -newkey rsa:2048 -subj '/CN=localhost' -keyout key.pem -out cert.pem -nodes -days 365
This creates a (2048 bit) private RSA key (key.pem) and a certificate (cert.pem) matching the host name “localhost”. The certificate will be valid for one year with these settings.

To set up a server using this key-certificate pair:
"""
import os
import ssl

from anyio import connect_tcp, run
from anyio import create_tcp_listener
from anyio.streams.tls import TLSListener

from common.utils import get_dir

#1) self sertificate
"""
To create a self signed certificate for localhost, you can use the openssl command line tool:

This creates a (2048 bit) private RSA key (key.pem) and a certificate (cert.pem) matching the host name “localhost”. The certificate will be valid for one year with these settings.

To set up a server using this key-certificate pair:
"""
dir = get_dir()
key_path = dir / "key.pem"
cert_path = dir / "cert.pem"


def generate_ssl():
    openssl_params = f"req -x509 -newkey rsa:2048 -subj '/CN=localhost' -keyout {key_path} -out {cert_path} -nodes -days 365"
    os.system(f"openssl {openssl_params}")


#To set up a server using this key-certificate pair:

async def handle(client):
    async with client:
        name = await client.receive()
        await client.send(b'Hello, %s\n' % name)

async def main_server():
    # Create a context for the purpose of authenticating clients
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

    # Load the server certificate and private key
    context.load_cert_chain(certfile=cert_path, keyfile=key_path)

    # Create the listener and start serving connections
    """
    According to the TLS standard, encrypted connections should end with a closing handshake. This practice prevents so-called truncation attacks. However, broadly available implementations for protocols such as HTTP, widely ignore this requirement because the protocol level closing signal would make the shutdown handshake redundant.
    
    AnyIO follows the standard by default (unlike the Python standard library’s ssl module). The practical implication of this is that if you’re implementing a protocol that is expected to skip the TLS closing handshake, you need to pass the standard_compatible=False option to wrap() or TLSListener.
    """
    listener = TLSListener(await create_tcp_listener(local_port=5555), context)
    await listener.serve(handle)

run(main_server)


