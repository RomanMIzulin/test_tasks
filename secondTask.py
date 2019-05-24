import requests
rs = requests.get('https://reqres.in/api/users/2')
assert rs.status_code == 200, 'status code is not 200'

n = 1
assert requests.get('https://reqres.in/api/users/2').elapsed.total_seconds()<n, 'time of response more than 1 second'

drs = rs.json()['data']
assert (drs['id'] ==2) and (drs['email'] == 'janet.weaver@reqres.in') and (drs['first_name'] =='Janet') and (drs['last_name'] == 'Weaver') and (drs['avatar']=='https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg'), 'Body of responce is not supposed'


