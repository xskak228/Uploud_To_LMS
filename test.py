from requests import get

print(get('http://localhost:8081/api/users_city/1').json())
