import http.client
import json

conn = http.client.HTTPSConnection("38rx1m.api.infobip.com")
payload = json.dumps({
    "phoneNumbers": [
        "998903225784"
    ]
})
headers = {
    'Authorization': 'App b628847d0b054667ee0e2a938e8e5293-35875ed1-ca47-4331-98e3-8488911b387c',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
conn.request("POST", "/signals/1/trusted-msisdns", payload, headers)
res = conn.getresponse()
data = res.read()
print(res.status)
print(data.decode("utf-8"))