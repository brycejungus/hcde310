import requests

base = "https://api.artic.edu/api/v1/artworks"

r = requests.get(base + "/search?query[match][title]=cats")
if r.status_code == 200:
    data = r.json()

    print(data)