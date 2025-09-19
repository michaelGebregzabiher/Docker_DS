import os
import requests
import sys

log_dir = '/log'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

api_address = os.getenv('API_ADDRESS', 'api')
api_port = os.getenv('API_PORT', 8000)

test_cases = [
    {'sentence': 'life is beautiful', 'expected_sign': 1},
    {'sentence': 'that sucks', 'expected_sign': -1}
]

endpoints = ['/v1/sentiment', '/v2/sentiment']
username = 'alice'
password = 'wonderland'

log_output = ''

for endpoint in endpoints:
    for i, case in enumerate(test_cases, 1):
        r = requests.get(
            url=f'http://{api_address}:{api_port}{endpoint}',
            params={
                'username': username,
                'password': password,
                'sentence': case['sentence']
            }
        )
        
        if r.status_code == 200:
            score = r.json().get('score', 0)
            test_status = 'SUCCESS' if (score * case['expected_sign']) > 0 else 'FAILURE'
        else:
            score = 'N/A'
            test_status = 'FAILURE'
        
        output = f'''
Test {i} - {endpoint}
============================
Content test
============================
request done at "{endpoint}"
| sentence="{case["sentence"]}"
expected score sign = {case["expected_sign"]}
actual score = {score}
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
