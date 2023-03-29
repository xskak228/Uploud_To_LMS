from requests import get, post, delete, put

# Good
print(put('http://localhost:8080/api/jobs',
          json={
              id
          }).json())
