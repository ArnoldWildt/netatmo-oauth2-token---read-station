from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session

auth_url = "https://api.netatmo.com/oauth2/token"

client_id = "c_id"
client_secret = "client_sec"
username = "usr"
password = "psw"
scope = "read_station"

oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))
token = oauth.fetch_token(token_url=auth_url, client_id=client_id,client_secret=client_secret,username=username,password=password,scope=scope)

print("####")
print(token)