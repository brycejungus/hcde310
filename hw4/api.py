import requests

FIELDS = "id,title,artist_title,artist_display,date_display"


url = "https://api.artic.edu/api/v1/artworks/search"     
  
headers = {"AIC-User-Agent": "HCDE 310 student project"}

# Search_art gets art from the API based on what the user inputs. It uses the users input to then call the API
# and returns what the API fetches. 
def search_art(term):
    params = {"q":term, "fields":FIELDS} 
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
    except requests.RequestException:
        print("API error: no answer") 
        return None
# This is what happens if there is an API error. If there is an error in fetching the response,
# then the message API error: no answer is printed. Same with the status code. If status code is not 200,
# then the status code is printed with the response reasoning.
    if (response.status_code != 200):
        print(response.status_code, response.reason)
        return None
    data = response.json()
    return data.get("data", [])




