import base64
import requests
import keys
from requests.auth import HTTPBasicAuth
from access_token import generate_access_token
from encoder import generate_password
from utils import get_timestamp
formatted_time = get_timestamp()
decoded_pwd = generate_password(formatted_time)

def lipa_na_mpesa():
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "BusinessShortCode": keys.business_shortCode,
        "Password": decoded_pwd,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": keys.phone_number,
        "PartyB": keys.business_shortCode,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://githisiot.com/lipanampesa/",
        "AccountReference": "cit2210182016",
        "TransactionDesc": "fees"
    }
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)

lipa_na_mpesa()
