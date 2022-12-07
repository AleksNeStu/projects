"""https://developer.allegro.pl/about/#rest-api"""
import logging
import requests
import sys

import constants
from oauth import AuthHandler

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class AllegroClient:
    def __init__(self, client_id, client_secret,
                 redirect_uri=constants.REDIRECT_URI, sandbox=True,
                 api_key=None,
                 timeout=None, request_headers=None, request_hooks=None,
                 access_token=None, refresh_token=None,
                 on_token_refresh_hook=None):
        if sandbox:
            self.base_url = constants.SANDBOX_API_URL
            self.auth_url = constants.SANDBOX_OAUTH_URL
        else:
            self.base_url = constants.API_URL
            self.auth_url = constants.OAUTH_URL

        self.auth_handler = AuthHandler(client_id=client_id,
                                        client_secret=client_secret,
                                        api_auth_url=self.auth_url,
                                        redirect_uri=redirect_uri,
                                        api_key=api_key,
                                        access_token=access_token,
                                        refresh_token=refresh_token)

        self.auth = self.auth_handler.apply_auth()

        self.timeout = timeout
        self.request_hooks = request_hooks

        self.request_headers = self._default_headers

        if isinstance(request_headers, dict):
            self.request_headers.update(request_headers)

        self._on_token_refresh_hook = on_token_refresh_hook

    def sign_in(self):
        """Use for 1st time login."""
        auth_response = self.auth_handler.get_access_token(silent=True)
        self.auth = self.auth_handler.apply_auth()

        return auth_response

    @property
    def _default_headers(self):
        headers = dict()
        headers['charset'] = 'utf-8'
        headers['content-type'] = 'application/vnd.allegro.public.v1+json'
        headers['accept'] = 'application/vnd.allegro.public.v1+json'

        return headers

    def _make_request(self, **kwargs):
        logging.info(u'{method} Request: {url}'.format(**kwargs))

        _tries = kwargs.pop('tries', 0) + 1

        if kwargs.get('json'):
            logging.info('PAYLOAD: {json}'.format(**kwargs))

        if kwargs.get('headers'):
            logging.info('PAYLOAD: {headers}'.format(**kwargs))

        try:
            response = requests.request(**kwargs)

            logging.info(u'{method} Response: {status} {text}'
                        .format(method=kwargs['method'],
                                 status=response.status_code,
                                 text=response.text))

        except requests.exceptions.RequestException as e:
            raise e
        else:
            if response.status_code == 401:
                if _tries > 10:
                    raise Exception(
                        "Could not refresh token! Please check credentials or connection!")

                logging.info(u'Response 401: Refreshing token....')
                self.auth_handler.refresh_access_token()
                self.auth = self.auth_handler.apply_auth()

                if self._on_token_refresh_hook:
                    self._on_token_refresh_hook(self.auth_handler.access_token,
                                                self.auth_handler.refresh_token)

                kwargs['auth'] = self.auth
                return self._make_request(tries=_tries, **kwargs)

            if response.status_code >= 400:
                if response.status_code == 404:
                    raise Exception("404 Not Found")
                else:
                    raise Exception(response.json())

            return response

    def _post(self, url, json=None, headers=None, data=None, files=None):
        url = requests.compat.urljoin(self.base_url, url)

        if isinstance(headers, dict):
            _headers = self.request_headers.copy()
            _headers.update(headers)
        else:
            _headers = self.request_headers

        req = self._make_request(**dict(
            method='POST',
            url=url,
            json=json,
            data=data,
            auth=self.auth,
            timeout=self.timeout,
            hooks=self.request_hooks,
            headers=_headers,
            files=files
        ))

        if req.status_code == 204:
            return None

        return req.json()

    def _get(self, url, params=None, headers=None):
        url = requests.compat.urljoin(self.base_url, url)

        if isinstance(headers, dict):
            _headers = self.request_headers.copy()
            _headers.update(headers)
        else:
            _headers = self.request_headers

        resp = self._make_request(**dict(
            method='GET',
            url=url,
            params=params,
            auth=self.auth,
            timeout=self.timeout,
            hooks=self.request_hooks,
            headers=_headers
        ))

        if resp.status_code == 204:
            return None

        return resp.json()

    def _delete(self, url, headers=None):
        url = requests.compat.urljoin(self.base_url, url)

        if isinstance(headers, dict):
            _headers = self.request_headers.copy()
            _headers.update(headers)
        else:
            _headers = self.request_headers

        req = self._make_request(**dict(
            method='DELETE',
            url=url,
            auth=self.auth,
            timeout=self.timeout,
            hooks=self.request_hooks,
            headers=_headers
        ))

        if req.status_code == 204:
            return None

        return req.json()

    def _patch(self, url, json=None, headers=None, data=None):
        url = requests.compat.urljoin(self.base_url, url)

        if isinstance(headers, dict):
            _headers = self.request_headers.copy()
            _headers.update(headers)
        else:
            _headers = self.request_headers

        req = self._make_request(**dict(
            method='PATCH',
            url=url,
            json=json,
            data=data,
            auth=self.auth,
            timeout=self.timeout,
            hooks=self.request_hooks,
            headers=_headers
        ))

        if req.status_code == 204:
            return None

        return req.json()

    def _put(self, url, json=None, headers=None, data=None):
        url = requests.compat.urljoin(self.base_url, url)

        if isinstance(headers, dict):
            _headers = self.request_headers.copy()
            _headers.update(headers)
        else:
            _headers = self.request_headers

        req = self._make_request(**dict(
            method='PUT',
            url=url,
            json=json,
            data=data,
            auth=self.auth,
            timeout=self.timeout,
            hooks=self.request_hooks,
            headers=_headers
        ))

        if req.status_code == 204:
            return

        return req.json()
