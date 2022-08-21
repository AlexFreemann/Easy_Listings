import json
from requests import post,put,get
from json import loads,dumps




BASE_URL='https://openapi.etsy.com/v3/application/shops/'

def get_link_to_shop_connection():
    return

def auth():
    return

def post_listing(params,shop_id):
    listing_id=None

    url = BASE_URL+f'{shop_id}/listings'

    try:
        listing_id = loads(post(url, auth=auth, params=params).text)['listing_id']
        mes=f'Listing created! Listing id is {listing_id}'
    except Exception as e:
        mes=f'Listing is not created! Error: {e}'

    return listing_id, mes

def add_variation(models,listing_id):
    # r = put('{}/{}/inventory'.format(base_url,listing_id), auth=auth, data={'products': models,'price_on_property': ['514']})
    # print(f"Uploading models for listing {listing_id} {read_r(r)}")
    return


def add_img(img_path,place,listing_id,shop_id):

    url= BASE_URL+f'{shop_id}/listings/{listing_id}/images'
    img_name=img_path.split('/')[-1]
    params = {'rank': place}
    files = {'image': [img_name, open(img_path, 'rb'), 'image/jpeg']}
    respone = post(url, params=params, files=files, auth=auth)

    return respone.text


import requests


def get_access_token():
    url=BASE_URL+"public/oauth/connect"

    link=f"""https://www.etsy.com/oauth/connect?
      response_type=code
      &redirect_uri=https://www.example.com/some/location
      &scope=transactions_r%20transactions_w
      &client_id={KEYSTRING}&state=superstate
      &code_challenge=DSWlW2Abh-cf8CeLL8-g3hQ2WQyYdKyiu83u_s7nRhI
      &code_challenge_method=S256"""

    return response.json()["access_token"]


KEYSTRING='5y0skqx6dx8ljs94wremg35m'
SHARED SECRET='pn3yhrr0h1'