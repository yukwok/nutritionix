import requests


GENDER = "M"
WEIGHT_KG = "90"
HEIGHT_CM = "180"
AGE = "45"

APP_ID = "a62bb22a"
API_KEY = "8a0cfb1927e2b85bdd09d8f0ef76bf61"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)12
