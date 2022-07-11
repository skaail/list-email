import http.client
import json

conn = http.client.HTTPSConnection("markflush.com")
payload = json.dumps({
  "EMAIL": "testestests@gmail.com"
})
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'XSRF-TOKEN=eyJpdiI6IlZselZvVmp3alNGV25mbWVTVVdWaFE9PSIsInZhbHVlIjoia3g0N25Gb2tseWV0OFlSeWN6bTNLNVhFYzRIL3lnSm1XQlRGcThwZUF4WmplNTNkQm8yTlM3NU9ycnZTNFJZakZHM3MvS0JEYWc5K2Y2ZlZIMk9DS1BwVE1lMTR4aStjdzFOVUhHYjFGUFNHNE5QMUhib2toei9JK08wa0NEOHkiLCJtYWMiOiJlZGNlYTliNzJhZmI0MzM3ZTcyNjIwYmFkNWFiYjA2OWI3YzdiNGFlNDlhY2ZkNzVmMTU1NGVkZmZlYjYzZjJiIiwidGFnIjoiIn0%3D; acelle_mail_session=eyJpdiI6IlYydzRVZXFMbGJ1UDZrWG5Hb0E3TVE9PSIsInZhbHVlIjoialFlaWFjTDNQNWtxbjVPaXBpSkwzeHFtdUhnc1BSU3k0bGdVUnUvOTVuTGFkRm40RmF6ZU5CTVpXNGxEMmFUdmlIdVp3dXJDdHRZNk9lVkhqSmMrU1Rlc21KUEFRWjJXUjlsajJVUHhEYmJwekVnVFRkWmpxT0ZZM0xYRVA0ekoiLCJtYWMiOiJjOWJhMGNkMzdiMDM5MDBlMWVlMDhiYTc3NzJhMTUwZDBkZmVhNzgzYWM5ZmU3MDlhNmU5YjQyMjI3ZjhiMWQxIiwidGFnIjoiIn0%3D'
}
conn.request("POST", "/secure/public/frontend/forms/62c3124c48423/save?=", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))