"""
OAuth plugin for HTTPie.

"""
from __future__ import print_function
from httpie.plugins import AuthPlugin
import os
import sys
import requests

__version__ = '1.0'
__author__ = 'Fabrice Aneche'
__licence__ = 'BSD'


class OAuth2DMPlugin(AuthPlugin):
    name = 'OAuth 2 DM'
    auth_type = 'oauth2DM'
    description = 'first export API_KEY, API_SECRET & AUTHORIZATION_URL'

    def get_auth(self, username, password):
        if not os.environ.get('API_KEY') or not os.environ.get('API_SECRET'):
            print('Set your API_KEY &API_SECRET in your environnement')
            sys.exit(2)

        payload = {
            'grant_type':'password',
            'client_id':os.environ.get('API_KEY'),
            'client_secret':os.environ.get('API_SECRET'),
            'username':username,
            'password':password,
        }

        r = requests.post("https://api.dailymotion.com/oauth/token", data=payload)
        if r.status_code != 200:
            print('oauth2DM: Invalid status code for token', r.status_code)

        res = r.json()
        if 'error' in res:
            print('oauth2DM:', res['error_description'])
            sys.exit(2)

        if 'access_token' not in res or 'uid' not in res:
            print('oauth2DM: Invalid token returned by DM')
            sys.exit(2)
        
        from requests_oauthlib import OAuth2 
        return OAuth2(client_id=res['uid'], token={'access_token':res['access_token'], 'token_type':'Bearer'})


