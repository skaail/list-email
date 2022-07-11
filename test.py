import http.client
import json

conn = http.client.HTTPSConnection("markflush.com")
payload = json.dumps({
  "EMAIL": "skaailsspvp@gmail.com"
})
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'XSRF-TOKEN=eyJpdiI6InNBY2hLalY3b2QvRDBvdjhRazlCU2c9PSIsInZhbHVlIjoic0VpK0p1MTVrdXZMd0JneHh5UlF1M1hGYUovQU9wajZjaDhrc3hPbGVmM1FhNVhzSHhhck5sTTFWK1JUeTY4d240WGE1a1E2M0djc0RMTWpzNGxPM0xxN3BFN3dKNERDaGl0aUhRYkJTTURqQjZDaG15K0xvenoxOFRJNFp4RTEiLCJtYWMiOiI3YmViZWY5MzIyZDMzN2UzZTlkOTczMGI2Nzc5MmJjNjZmNDkzN2QwNWFmMmNmNTNiMjE4NjNhYTk5YTlmMjMxIiwidGFnIjoiIn0%3D; acelle_mail_session=eyJpdiI6IjNnUmd0MllEelJGZFA2YlA5dGtSMlE9PSIsInZhbHVlIjoiWGxRbXJibG1VazFSQ2pDZzJtNmRlak0zRGtBYVRXMFlPblVvQncyelJaT2J0aTRhM2FwcEZTNlRIVmJyMGFlRHJMdlJxb0FvM2ZheGhZUy9EK3dIUkNKS050eGtzZXgyQjV1OWt4KzZSeVNmeUxMM1pRVG1udXN2U3NmSExHRDYiLCJtYWMiOiJjMDgyODE2MzFkNjVkMWI5NmEyZWM3NWIwYTAyYmVhNzIzYzFkMjI2MWUxMTljYTAwMWU0YTM1MTFlN2Q5YTAxIiwidGFnIjoiIn0%3D'
}
conn.request("POST", "/secure/public/frontend/forms/62c3124c48423/save?=", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))