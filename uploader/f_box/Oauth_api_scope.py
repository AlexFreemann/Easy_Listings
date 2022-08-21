
from requests_oauthlib import OAuth1Session, OAuth1,OAuth2, OAuth2Session
from urllib.parse import urlencode


consumer_key = input("Input consumer key (long):")
oauth_consumer_secret = input("Input consumer secret (short):")


auth = OAuth2(consumer_key,oauth_consumer_secret)


 # Здесь нужно вписать параметр Permission Scope подробнеее тут https://www.etsy.com/developers/documentation/getting_started/oauth#perm_scope_listings_w
request_token_url = 'https://www.etsy.com/oauth/connect'
access_token_url = 'https://api.etsy.com/v3/public/oauth/token'

params={'response_type':'code','redirect_uri':'https://www.example.com/some/location','scope':'listing_w'}

oauth = OAuth2Session(consumer_key, client_secret=oauth_consumer_secret)

resp = etsy.fetch_request_token(request_token_url)


print('Click to this URL for allow access:')# тут мы получаем ссылку для получения когда временной авторизации
print(resp['login_url'])

verifier = input('Paste confirm code:') # тут печатаем код временнной авторизации

etsy = OAuth2Session(consumer_key, client_secret=oauth_consumer_secret, resource_owner_key=resp['oauth_token'], resource_owner_secret=resp['oauth_token_secret'])
acc_token = etsy.fetch_access_token(access_token_url, verifier=verifier)
print(acc_token) # и получаем словарь параметров авторизаци по выбранному Permission Scope (напр listings_w)
