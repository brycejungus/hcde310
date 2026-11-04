**What it is**
The Calorie Ninjas API is an API focused on nutrition. You can send it plain English text about food and it will 
give you structured nutrition data about that food. The API just takes a query parameter and returns information 
about each item. A designer might care for this API if they're looking for an API that's easy to use and gives
nutrition facts about thousands of foods. 

**Setup:**
pip install requests
Sign up for account and get API key from website

**Working Example**
URL = "https://api.calorieninjas.com/v1/nutrition"
params = {"query": "1lb brisket and potatoes"}
key = os.getenv("API_NINJAS_KEY")
headers = {"X-Api-Key": key}

response = requests.get(URL, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    food = data["items"][0]
    print(food)
else:
    print("Status Code: ", response.status_code)
**Output**
{'name': 'brisket', 'calories': 1312.3, 'serving_size_g': 453.592, 'fat_total_g': 82.9, 'fat_saturated_g': 33.2, 'protein_g': 132.0, 'sodium_mg': 217, 'potassium_mg': 781, 'cholesterol_mg': 487, 'carbohydrates_total_g': 0.0, 'fiber_g': 0.0, 'sugar_g': 0.0}

**Gotchas**
The original service is being shut down and moved over to APIninjas. On the new APINinjas, the free version hides the calories and protein. Missing data may emerge if it doesn't recognize a food, then it just disappears. The rate limits for calorie ninjas is 10,000 a month.

**Design Angle**
One project idea that it enables is a meal prep app for college students trying to keep track of their calorie count. The API returns numbers that are just estimates which is an ethical concern as some users might think it's exact numbers.


