import urllib.request, json, urllib.error
try:
    req = urllib.request.Request(
        'http://localhost:3002/generate',
        data=b'{"name": "CalcIMC", "description": "Crie"}',
        headers={'Content-Type': 'application/json'}
    )
    res = urllib.request.urlopen(req)
    print(res.read().decode())
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code}")
    print(e.read().decode())
except Exception as e:
    print(e)
