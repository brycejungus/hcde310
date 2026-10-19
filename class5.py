import json
with open("aic_sample.json") as f:
    data = json.load(f)
results = data["data"]
print(results)
first = results[0]
print(first)

first_title = data["data"][0]["title"]
print(first_title)

total_results = len(results)

second_results = data["data"][1]["title"]
first_artst = data["data"][0]["artist"]
image_id = data["data"][2]["image_id"]
