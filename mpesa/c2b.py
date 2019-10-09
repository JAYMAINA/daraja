import requests
import base64
from requests.auth import HTTPBasicAuth
import keys
from access_token import generate_access_token

def regurl():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % generate_access_token()}
    request = { 
        "ShortCode": keys.shortcode,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://githisiot.com/confirmation",
        "ValidationURL": "https://githisiot.com/validation_url"}

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

#regurl()

def simulatetransaction_c2b():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % generate_access_token()}
    request = { "ShortCode": keys.shortcode,
    "CommandID":"CustomerPayBillOnline",
    "Amount":"1",
    "Msisdn": keys.test_msisdn,
    "BillRefNumber":"cit2210182016" }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

simulatetransaction_c2b()