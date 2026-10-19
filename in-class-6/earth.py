# In-class 6: NASA EPIC (photos of the whole Earth from space), with the key kept in .env
#
# 1. Load the key from .env (python-dotenv: load_dotenv(), then os.getenv("NASA_API_KEY"))
# 2. Call https://api.nasa.gov/EPIC/api/natural with your key as the api_key parameter,
#    and timeout=10 so it gives up instead of hanging if the server is slow
# 3. Check r.status_code before you use the data
# 4. The reply is a list of today's photos. Print the caption and the date of the first one

import os
import requests
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("NASA_API_KEY")
print(key is None)
url = "https://api.nasa.gov/EPIC/api/natural"
apiCall = requests.get(url, params={"timeout":10, "api_key":key})
print(apiCall.json()[0]["caption"], apiCall.json()[0]["date"])
# caption = apiCall["caption"]