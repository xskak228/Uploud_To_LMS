from requests import get, post, delete

# Good
print(delete('http://localhost:8080/api/jobs/2').json())
print(delete('http://localhost:8080/api/jobs/999').json())
print(delete('http://localhost:8080/api/jobs/q').json())