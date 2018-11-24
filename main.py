from urllib import request, parse
import requests
import json
import sys
EVM_IP = 'http://127.0.0.1:8080'
ADDR = ['0x8d42377708663c904Bd9CA0D34970f3a7e265981', '0xEd2106819C0416b6CE86d70c9B6d7F3e9DdbC530', '0x5C683797Ac65ED780067391Adff2b586370B0849', '0xf1c9f7ac7b09b3380885831a2c2e4c00f97057e2', '0xefad7a4c52cb8e0d4af4b803e679c95e4d729d62']

def sendTransaction(from_adr, to_adr, msg_data, value):
    base_url = EVM_IP
    url = base_url + '/tx'
    data = {
        'from': '{}'.format(from_adr),
        'to': '{}'.format(to_adr),
        'value': value,
        'gas': 4000000,
        'data': msg_data
    }
    if to_adr == '':
        data.pop('to')

    data_arr = [data, data]
    if msg_data == '':
        data.pop('data')
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    req =  requests.post(url, data=json.dumps(data_arr), headers=headers)
    return req

def sendBundleTransaction(to_adr, msg_data, value):
    base_url = EVM_IP
    url = base_url + '/tx'

    data_arr = []
    for adr in ADDR:
        data = {
            'from': '{}'.format(adr),
            'to': '{}'.format(to_adr),
            'value': value,
            'gas': 4000000,
            'data': msg_data
        }
        if msg_data == '':
            data.pop('data')

        if to_adr == '':
            data.pop('to')

        data_arr.append(data)

    for i in range(5):
        data_arr.append(data_arr[i])
    #print('sending : ', len(data_arr))
        
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    req =  requests.post(url, data=json.dumps(data_arr), headers=headers)
    return req


rq = []
#print('sending %d package each of the package contains 10 tx'%(int(sys.argv[1])))
for i in range(int(sys.argv[1])):
    rq = sendBundleTransaction('0x70AEc4B9CFFA7b55C0711b82DD719049d615E21d', '', 100)
    #rq = (sendTransaction('0xEd2106819C0416b6CE86d70c9B6d7F3e9DdbC530', '0x70AEc4B9CFFA7b55C0711b82DD719049d615E21d', '', 100))

#print(rq)
