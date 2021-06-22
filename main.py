from datetime import datetime
import requests

GENDER = "M"
WEIGHT_KG = "90"
HEIGHT_CM = "180"
AGE = "47"

APP_ID = "a62bb22a"
API_KEY = "8a0cfb1927e2b85bdd09d8f0ef76bf61"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/e02e90cc81d3e6b66814fe14bef27a3e/trainingWorkouts/workouts"
sheety_bearer_token = "sfsafsffsfwer234sdfe34tdfg34tsdfgs36rdhfdhsdfgJHGHJFGKJUY#KJFjgsdfjksdfhk"
exercise_text = input("Tell me which exercises you did: ")

bearer_headers = {
    "Authorization": f"Bearer {sheety_bearer_token}"
}

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

response = requests.post(url=exercise_endpoint,
                         headers=headers, json=parameters)
exercise_0 = response.json()["exercises"][0]

# print(exercise_0["user_input"])
# print(exercise_0["duration_min"])
# print(exercise_0["nf_calories"])

exercise = exercise_0["user_input"]
duration = exercise_0["duration_min"]
calories = exercise_0["nf_calories"]


today_date = datetime.today().strftime("%d/%m/%Y")
today_time = datetime.today().strftime("%H:%M:%S")


print(today_time)


sheety_parameters = {
    "workout":
    {"exercise": exercise,
     "duration": duration,
     "calories": calories,
     "date": today_date,
     "time": today_time, }
}


response = requests.post(
    url=sheety_endpoint, json=sheety_parameters, headers=bearer_headers)


response = requests.get(url=sheety_endpoint, headers=bearer_headers)
workouts = response.json()
print(workouts)
