import os
import requests
import sys

log_dir = '/log'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

api_address = os.getenv('API_ADDRESS', 'api')
api_port = os.getenv('API_PORT', 8000)

test_cases = [
    {'user': 'bob', 'password': 'builder', 'endpoint': '/v1/sentiment', 'expected': 200},
    {'user': 'bob', 'password': 'builder', 'endpoint': '/v2/sentiment', 'expected': 403},
    {'user': 'alice', 'password': 'wonderland', 'endpoint': '/v1/sentiment', 'expected': 200},
    {'user': 'alice', 'password': 'wonderland', 'endpoint': '/v2/sentiment', 'expected': 200}
]

log_output = ''

for i, case in enumerate(test_cases, 1):
    r = requests.get(
        url=f'http://{api_address}:{api_port}{case["endpoint"]}',
        params={
            'username': case['user'],
            'password': case['password'],
            'sentence': 'test sentence'
        }
    )
    
    status_code = r.status_code
    test_status = 'SUCCESS' if status_code == case['expected'] else 'FAILURE'
    
    output = f'''
Test {i}
============================
Authorization test
============================
request done at "{case["endpoint"]}"
| username="{case["user"]}"
expected result = {case["expected"]}
actual result = {status_code}
==>  {test_status}
'''
    print(output)
    log_output += output

if os.environ.get('LOG') == '1':
    with open('/log/api_test.log', 'a') as file:
        file.write(log_output)
    # #force flush to ensure logs are written immediately
    # file.flush()
    # os.fsync(file.fileno())