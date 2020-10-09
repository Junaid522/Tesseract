client = EvernoteClient(
    consumer_key='YOUR CONSUMER KEY',
    consumer_secret='YOUR CONSUMER SECRET',
    sandbox=True # Default: True
)
request_token = client.get_request_token('YOUR CALLBACK URL')
client.get_authorize_url(request_token)