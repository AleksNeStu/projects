"""https://developer.allegro.pl/en/auth/"""

import requests
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from requests import auth
from requests import utils
from urllib.parse import urlparse, parse_qs

import constants
import settings


class OAUTHBearer(auth.AuthBase):
    """OAUTHBearer class."""

    def __init__(self, api_key, access_token):
        self._api_key = api_key
        self._access_token = access_token

    def __call__(self, req):
        req.headers['authorization'] = f"Bearer {self._access_token}"
        return req


class HTTPHandler(BaseHTTPRequestHandler):
    """HTTP Server callbacks to handle OAuth redirects."""

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        code_val = parse_qs(self.path).get('/?code')

        if code_val:
            msg = 'OAUTH is finished. Tab can be closed.'
            self.server.auth_code =  code_val[0]
        else:
            msg = ('Authorization code is not returned, PTAL: '
                   'https://developer.allegro.pl/en/auth/')

        self.wfile.write(
            bytes(f'<html>{msg}</html>', 'utf-8'))


class AuthHandler:
    """https://developer.allegro.pl/auth/"""

    def __init__(self, client_id, client_secret,
                 api_auth_url=constants.OAUTH_URL,
                 redirect_uri=constants.REDIRECT_URI, api_key=None,
                 access_token=None, refresh_token=None, token_expires_in=None):
        self._client_id = client_id
        self._client_secret = client_secret
        self._api_key = api_key
        # Remove suffix if necessary
        self._auth_url = api_auth_url[:-1] if api_auth_url.endswith(
            '/') else api_auth_url
        self._redirect_uri = redirect_uri

        self.access_token = access_token
        self.refresh_token = refresh_token
        self.token_expires_in = token_expires_in

    def get_oauth_url(self, silent):
        base_url = (
            "{auth_url}"
            "/authorize"
            "?response_type=code"
            "&client_id={client_id}"
            "&redirect_uri={redirect_uri}"
        )
        # '&prompt=confirm' is default
        # https://auth0.com/docs/authenticate/login/configure-silent-authentication
        if silent:
            base_url += '&prompt=none'
        url = base_url.format(auth_url=self._auth_url,
                              client_id=self._client_id,
                              redirect_uri=self._redirect_uri)

        return utils.requote_uri(url)

    def get_oauth_code(self, silent=False):
        """Gets auth code via browser."""
        red_uri = urlparse(self._redirect_uri)
        serv_name_port = red_uri.hostname, red_uri.port
        oauth_url = self.get_oauth_url(silent)

        httpd = HTTPServer(serv_name_port, HTTPHandler)
        # Consider using handles mode w/o opening of the browser
        # https://stackoverflow.com/questions/21777306/python-browser-emulator-with-js-support
        webbrowser.open(oauth_url)

        httpd.handle_request()
        httpd.server_close()

        # TODO: Add errors handling
        return httpd.auth_code

    def get_access_token(self, code=None, silent=False):
        access_code = self.get_oauth_code(silent) if code is None else code

        _url = self._auth_url + '/token'

        access_token_data = {'grant_type': 'authorization_code',
                             'code': access_code,
                             'redirect_uri': self._redirect_uri
                             }

        try:
            resp = requests.post(url=_url,
                              auth=auth.HTTPBasicAuth(
                                  self._client_id, self._client_secret),
                              data=access_token_data)
        except requests.exceptions.RequestException as e:
            raise e
        else:
            if resp.status_code >= 400:
                raise Exception(resp.json())

            response = resp.json()
            self.access_token = response['access_token']
            self.refresh_token = response['refresh_token']
            self.token_expires_in = response['expires_in']

            return response

    def refresh_access_token(self, refresh_token=None):
        _refresh_token = (
            self.refresh_token if refresh_token is None else refresh_token)

        _url = self._auth_url + '/token'

        refresh_token_data = {'grant_type': 'refresh_token',
                              'refresh_token': _refresh_token,
                              'redirect_uri': self._redirect_uri
                              }

        try:
            resp = requests.post(url=_url,
                              auth=auth.HTTPBasicAuth(
                                  self._client_id, self._client_secret),
                              data=refresh_token_data)
        except requests.exceptions.RequestException as e:
            raise e
        else:
            if resp.status_code >= 400:
                raise Exception(resp.json())

            response = resp.json()
            self.access_token = response['access_token']
            self.refresh_token = response['refresh_token']
            self.token_expires_in = response['expires_in']

            return response

    def apply_auth(self):
        return OAUTHBearer(self._api_key, self.access_token)


def get_access_code(silent):
    api_handler = AuthHandler(
        client_id=settings.CLIENT_ID, client_secret=settings.CLIENT_SECRET)
    access_code = api_handler.get_oauth_code(silent)
    return access_code

# access_code = get_access_code(silent=True)
