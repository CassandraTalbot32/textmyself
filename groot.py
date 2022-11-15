# python3
# textMyself.py - defines the textMyself function that sends a string passed to it as a msg

from twilio.rest import Client

# preset values
accountSID = 'AVXXXXXXXXXXXXXXXXXXXXXXXXXXX'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
myNumber = '+07777777777'
twilioNumber = '+1234568910'

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)

import textmyself
textmyself.textmyself('Side quest complete!')
