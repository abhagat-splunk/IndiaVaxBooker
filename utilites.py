import json
import requests
import cowin_constants
def get_otp(phone_number):
    """
    curl -X POST "" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"mobile\":\"9876543210\"}"
    """
    url = "{}{}".format(cowin_constants.BASE_URL, cowin_constants.GENERATEOTP_EP)
    data = {"mobile": phone_number}
    print (url)
    headers = {"Content-Type": cowin_constants.APPJSON, "Accept": cowin_constants.APPJSON}
    print (headers)
    print (data)
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print ("{}\n{}\n{}".format(r.text, r.status_code, r))
    if r.status_code==200:
        return r.data['txnId']
    return ''    

#def confirm_otp(txn_id, otp):


