from requests import get, post, delete

# Good
print(post('http://localhost:8080/api/jobs',
           json={'id': 9,
                 'team_leader': 2,
                 'job': 'TEST_API',
                 'work_size': 10,
                 "collaborators": "1, 3, 4",
                 "start_date": "19.03.2023",
                 'is_finished': False}).json())

# Worst ID
print(post('http://localhost:8080/api/jobs',
           json={'id': 4,
                 'team_leader': 2,
                 'job': 'TEST_API',
                 'work_size': 10,
                 "collaborators": "1, 3, 4",
                 "start_date": "19.03.2023",
                 'is_finished': False}).json())

# Нет параметров
print(post('http://localhost:8080/api/jobs',
           json={'id': 4,
                 'team_leader': 2,
                 'job': 'TEST_API',
                 'work_size': 10,
                 "start_date": "19.03.2023",
                 'is_finished': False}).json())



print(get('http://localhost:8080/api/jobs').json())