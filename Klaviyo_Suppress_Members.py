import requests

public_api_key = 'ABC'
private_api_key = 'XYZ'

"""
A segment was created manually in the Klaviyo UI.
It contains any email address that contains the trailing characters:
    "@friendbuy.com"
"""
segment_id = "WgaEjb"

segment_url = "https://a.klaviyo.com/api/v2/group/" + segment_id + "/members/all?api_key=" + private_api_key
# https://developers.klaviyo.com/en/reference/get-members

headers = {
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.request("GET", segment_url, headers=headers)
'''
If number of segment members > 1000, a marker to the next 
member pagination will be returned. This is not yet handled.
'''
records = []
if response.status_code == 200:
    response_data_dict = response.json()  # convert response to JSON
    records = response_data_dict.get('records', [])  # get list of dicts representing members
    #records = response_data_dict['records']  # get list of dicts representing members
    print("Received the desired segment!")
else:
    print("Error getting desired segment!")
    print(response.text)
    exit()


''' PART 2: once we get the desired segment emails, we then want to suppress it '''

suppress_seg_url = "https://a.klaviyo.com/api/v1/people/exclusions"
# https://developers.klaviyo.com/en/reference/exclude-globally

for rec in records:
    payload = {'api_key': private_api_key, 'email': rec['email']}
    response2 = requests.request("POST", suppress_seg_url, data=payload, headers=headers)

    if response2.status_code == 200:
        print("Suppressed " + rec['email'])
    else:
        print("Error suppressing " + rec['email'] + "!")
        print(response2.text)
        exit()

print("Segment Members Suppressed!")
