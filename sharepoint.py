import requests
import uuid
import json

from urllib.parse import quote, urlencode
import requests
import time

# Client ID and secret

# client_id = settings.ONEDRIVE_CLIENT_ID
# client_secret = settings.ONEDRIVE_SECRET_ID

# Constant strings for OAuth2 flow
# The OAuth authority
authority = 'https://login.microsoftonline.com'

# GET https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=ce9a9b0e-6de2-4ba1-bcfa-1352be652529&scope=openid offline_access User.Read files.read files.read.all files.readwrite files.readwrite.all&response_type=token&redirect_uri=https://www.google.com


# The authorize URL that initiates the OAuth2 client credential flow for admin consent
# authorize_url = '{0}{1}'.format(authority, '/nomadz.onmicrosoft.com/oauth2/v2.0/authorize?{0}')
authorize_url = '{0}{1}'.format(authority, '/common/oauth2/v2.0/authorize?{0}')

# The token issuing endpoint
# token_url = '{0}{1}'.format(authority, '/nomadz.onmicrosoft.com/oauth2/v2.0/token')
token_url = '{0}{1}'.format(authority, '/common/oauth2/v2.0/token')

# The scopes required by the app
scopes = ['openid',
          'offline_access',
          'User.Read',
          'files.read',
          'files.read.all',
          'files.readwrite',
          'files.readwrite.all',
          'Sites.Read.All',
          'Sites.ReadWrite.All',
          'Sites.Manage.All',
          'Sites.FullControl.All',
          # 'Sites.Search.All',
          # 'TermStore.Read.All',
          # 'TermStore.ReadWrite.All',
          # 'User.Read.All',
          # 'User.ReadWrite.All'
          ]


def get_signin_url(redirect_uri):
    # Build the query parameters for the signin url
    params = {'client_id': client_id,
              'redirect_uri': redirect_uri,
              'response_type': 'code',
              'scope': ' '.join(str(i) for i in scopes)
              }

    signin_url = authorize_url.format(urlencode(params))
    return signin_url


def get_token_from_code(auth_code, redirect_uri):
    # Build the post form for the token request
    post_data = {'grant_type': 'authorization_code',
                 'code': auth_code,
                 'redirect_uri': redirect_uri,
                 'scope': ' '.join(str(i) for i in scopes),
                 'client_id': client_id,
                 'client_secret': client_secret
                 }

    r = requests.post(token_url, data=post_data)

    try:
        return r.json()
    except:
        return 'Error retrieving token: {0} - {1}'.format(r.status_code, r.text)


def get_code_from_code(auth_code, redirect_uri):
    # Build the post form for the token request
    post_data = {'grant_type': 'authorization_code',
                 'code': auth_code,
                 'redirect_uri': redirect_uri,
                 'scope': ' '.join(str(i) for i in scopes),
                 'client_id': client_id,
                 'client_secret': client_secret
                 }

    r = requests.post(token_url, data=post_data)
    print(r.json())
    try:
        return r.json()
    except:
        return 'Error retrieving token: {0} - {1}'.format(r.status_code, r.text)


def get_token_from_refresh_token(refresh_token, redirect_uri):
    # Build the post form for the token request
    post_data = {'grant_type': 'refresh_token',
                 'refresh_token': refresh_token,
                 'redirect_uri': redirect_uri,
                 'scope': ' '.join(str(i) for i in scopes),
                 'client_id': client_id,
                 'client_secret': client_secret
                 }

    r = requests.post(token_url, data=post_data)
    print(r.json())

    try:
        return r.json()
    except:
        return 'Error retrieving token: {0} - {1}'.format(r.status_code, r.text)


def get_access_token(request, redirect_uri):
    current_token = request.session.get('access_token')
    expiration = request.session.get('token_expires')
    now = int(time.time())
    if current_token and now < expiration:
        # Token still valid
        return current_token
    else:
        # Token expired
        refresh_token = request.session.get('refresh_token')
        new_tokens = get_token_from_refresh_token(refresh_token, redirect_uri)

        # Update session
        # expires_in is in seconds
        # Get current timestamp (seconds since Unix Epoch) and
        # add expires_in to get expiration time
        # Subtract 5 minutes to allow for clock differences
        expiration = int(time.time()) + 3600 - 300

        # Save the token in the session
        request.session['access_token'] = new_tokens['access_token']
        request.session['refresh_token'] = new_tokens['refresh_token']
        request.session['token_expires'] = expiration

        return new_tokens['access_token']


graph_endpoint = 'https://graph.microsoft.com/v1.0{0}'


# Generic API Sending
def make_api_call(method, url, token, payload=None, parameters=None):
    # Send these headers with all API calls
    headers = {'User-Agent': 'django_onedrive/1.0',
               'Authorization': 'Bearer {}'.format(token),
               'Accept': 'application/json',
               "Content-Type": "application/x-www-form-urlencoded"}

    # Use these headers to instrument calls. Makes it easier
    # to correlate requests and responses in case of problems
    # and is a recommended best practice.
    request_id = str(uuid.uuid4())
    instrumentation = {'client-request-id': request_id,
                       'return-client-request-id': 'true'}

    headers.update(instrumentation)

    response = None

    if (method.upper() == 'GET'):
        response = requests.get(url, headers=headers, params=parameters)
    elif (method.upper() == 'DELETE'):
        response = requests.delete(url, headers=headers, params=parameters)
    elif (method.upper() == 'PATCH'):
        headers.update({'Content-Type': 'application/json'})
        response = requests.patch(url, headers=headers, data=json.dumps(payload), params=parameters)
    elif (method.upper() == 'POST'):
        headers.update({'Content-Type': 'application/json'})
        response = requests.post(url, headers=headers, data=json.dumps(payload), params=parameters)

    return response


def get_me(access_token):
    get_me_url = graph_endpoint.format('/me')

    # Use OData query parameters to control the results
    #  - Only return the displayName and mail fields
    query_parameters = {'$select': 'displayName,files'}

    r = make_api_call('GET', get_me_url, access_token, "", parameters=query_parameters)

    if (r.status_code == requests.codes.ok):
        return r.json()
    else:
        return "{0}: {1}".format(r.status_code, r.text)


def get_sharepoint_site_id(access_token):
    # get_me_url = graph_endpoint.format('/sites/netorg225728.sharepoint.com,e93cb13b-eda5-4fdd-8905-52d579965644,cc542cd1-b287-45fe-9048-4b8e2e6c5bbe')
    # get_me_url = graph_endpoint.format('/sites/root/lists')
    get_me_url = graph_endpoint.format('/sites/root/lists')
    # get_me_url = graph_endpoint.format('/sites/netorg225728.sharepoint.com,e93cb13b-eda5-4fdd-8905-52d579965644,cc542cd1-b287-45fe-9048-4b8e2e6c5bbe/drives/b!O7E86aXt3U-JBVLVeZZWRNEsVMyHsv5FkEhLji5sW76toYeV8uUqRKEwRYeRIVHy/root/children')

    # Use OData query parameters to control the results
    #  - Only return the displayName and mail fields
    query_parameters = {}

    r = make_api_call('GET', get_me_url, access_token, "", parameters=query_parameters)

    if (r.status_code == requests.codes.ok):
        return r.json()
    else:
        return "{0}: {1}".format(r.status_code, r.text)


def get_sharepoint_drive_id(access_token, site_id):
    get_me_url = graph_endpoint.format('/sites/'+site_id+'/drives')
    # get_me_url = graph_endpoint.format('/sites/root/lists')
    # get_me_url = graph_endpoint.format('/sites/root/lists')
    # get_me_url = graph_endpoint.format('/sites/netorg225728.sharepoint.com,e93cb13b-eda5-4fdd-8905-52d579965644,cc542cd1-b287-45fe-9048-4b8e2e6c5bbe/drives/b!O7E86aXt3U-JBVLVeZZWRNEsVMyHsv5FkEhLji5sW76toYeV8uUqRKEwRYeRIVHy/root/children')

    # Use OData query parameters to control the results
    #  - Only return the displayName and mail fields
    query_parameters = {}

    r = make_api_call('GET', get_me_url, access_token, "", parameters=query_parameters)

    if (r.status_code == requests.codes.ok):
        return r.json()
    else:
        return "{0}: {1}".format(r.status_code, r.text)


def get_sharepoint(access_token, site_id, drive_id):
    get_me_url = graph_endpoint.format('/sites/'+site_id+'/drives/'+drive_id+'/root/children')

    # Use OData query parameters to control the results
    #  - Only return the displayName and mail fields
    query_parameters = {}

    r = make_api_call('GET', get_me_url, access_token, "", parameters=query_parameters)

    if (r.status_code == requests.codes.ok):
        return r.json()
    else:
        return "{0}: {1}".format(r.status_code, r.text)


# def main():
#     auth_code = request.GET['code']
#     redirect_uri = 'https://27e84f99.ngrok.io/gettoken/'
#     token = get_token_from_code(auth_code, redirect_uri)
#     # token = get_code_from_code(auth_code, redirect_uri)
#     access_token = token['access_token']
#     data = get_drive(access_token)
#     sharepoint = get_sharepoint_site_id(access_token)
#     site_id = sharepoint['value'][0]['parentReference']['siteId']
#     sharepoint = get_sharepoint_drive_id(access_token, site_id)
#     drive_id = sharepoint['value'][0]['id']
#     sharepoint = get_sharepoint(access_token, site_id, drive_id)