# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
from twilio.twiml.messaging_response import MessagingResponse

# account_sid = 'AC923cebe1201f554ab5e35e36e7321cf3'
account_sid = 'ACde51c42e94f3414d11de10516f8ecefb'
# auth_token = 'de487555491df27b59f58745e37e2529'
auth_token = '07ded5c2a1f2be6e88cedafe12d0ca0d'
client = Client(account_sid, auth_token)

message = client.messages.create(
         body='This is the testing message Talha Junaid ;p ;p ;p !!!!',
         from_='+18504040675',
         media_url=['https://www.researchgate.net/profile/Visa_Tasic/publication/268802697/figure/fig2/AS:667837232316430@1536236212637/MMS-in-simple-control-system-block-schema.png'],
         to='+1 647 493 5996'
     )

print(message.sid)

def sms_reply():
    """Respond to incoming with a simple text message."""

    resp = MessagingResponse()
    print(resp)
