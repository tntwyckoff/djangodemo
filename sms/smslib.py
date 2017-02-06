from twilio.rest import TwilioRestClient


smsEp = "http://bugs.python.org"
fromPhone = "+18317131581"

account_sid = "ACbc91aab5fc28da67a610d8d55d80c317"
auth_token = "580faaa47b2a7d1cb7b9c1f83974f524"

test_account_sid = "AC29f5232040b0a6d9c0bbbd02c0616159"
test_auth_token = "a37416d5363bdad2880a675d6728d193"
test_from = "15005550006"

def sendSms (number, message):
    toPhone = formatPhone (number)

    # client = TwilioRestClient(test_account_sid, test_auth_token)
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(to=toPhone, from_=fromPhone, body=message)
   
    return True

def sendSmsApi (number, message):
    toPhone = formatPhone (number)

    return True

def formatPhone (number):
    return "+1{0}".format (number)