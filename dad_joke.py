import requests

joke_url="https://icanhazdadjoke.com"
my_header={
    'Accept':'application/json'
}
# api call
result = requests.get(joke_url,headers=my_header)
json_result=result.json()
print(json_result['joke'])
