import requests

url = "https://price-history-charts.p.rapidapi.com/ProductHistory"

querystring = {
    "product_url": "https%3A%2F%2Fwww.flipkart.com%2Ff-d-f550x-56-w-bluetooth-home-theatre%2Fp%2Fitmbb277b11d5a94%3Fpid%3DACCEA2ASHNDGV4DP%26lid%3DLSTACCEA2ASHNDGV4DPE2GRYO%26marketplace%3DFLIPKART%26srno%3Ds_1_1%26otracker%3Dsearch%26fm%3DSEARCH%26iid%3Dbc4e7784-8f7a-48c6-b2f4-7991f15036db.ACCEA2ASHNDGV4DP.SEARCH%26ppt%3DSearch%2520Page%26ppn%3DSearch%26ssid%3Dskfmliat1s0000001533652515715%26qH%3Db15bdcf202f61a0d"}

payload = ""
headers = {
    'x-rapidapi-host': "price-history-charts.p.rapidapi.com",
    'x-rapidapi-key': "7bf12dce6fmsh43c7ce1499ba549p1ebd1ajsnbf675aa7cd5b",
    'content-type': "application/x-www-form-urlencoded"
}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)


import http.client

conn = http.client.HTTPSConnection("price-history-charts.p.rapidapi.com")

payload = ""

headers = {
    'x-rapidapi-host': "price-history-charts.p.rapidapi.com",
    'x-rapidapi-key': "7bf12dce6fmsh43c7ce1499ba549p1ebd1ajsnbf675aa7cd5b",
    'content-type': "application/x-www-form-urlencoded"
    }

conn.request("POST", "/ProductHistory?product_url=https%25253A%25252F%25252Fwww.flipkart.com%25252Ff-d-f550x-56-w-bluetooth-home-theatre%25252Fp%25252Fitmbb277b11d5a94%25253Fpid%25253DACCEA2ASHNDGV4DP%252526lid%25253DLSTACCEA2ASHNDGV4DPE2GRYO%252526marketplace%25253DFLIPKART%252526srno%25253Ds_1_1%252526otracker%25253Dsearch%252526fm%25253DSEARCH%252526iid%25253Dbc4e7784-8f7a-48c6-b2f4-7991f15036db.ACCEA2ASHNDGV4DP.SEARCH%252526ppt%25253DSearch%25252520Page%252526ppn%25253DSearch%252526ssid%25253Dskfmliat1s0000001533652515715%252526qH%25253Db15bdcf202f61a0d", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))