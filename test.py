from requests import get, post, delete, put

# Good
print(get('http://localhost:8081/api/users/3').json())
print(delete('http://localhost:8081/api/users/3').json())
print(get('http://localhost:8081/api/users/3').json())
