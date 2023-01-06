import requests
import json
import time
import datetime
# station: https://ckan.odpt.org/dataset/c_bikeshare_gbfs-d-bikeshare/resource/06ddbb21-be3d-4163-ac92-d90127e9bf90

def get_station_info():
    url = 'https://api-public.odpt.org/api/v4/gbfs/docomo-cycle-tokyo/station_information.json'
    r = requests.get(url)
    station_status_json = r.json()

    with open('dumps/station_info.json', 'w') as f:
      json.dump(station_status_json, f, indent=4)

def get_staion_status():
    url = 'https://api-public.odpt.org/api/v4/gbfs/docomo-cycle-tokyo/station_status.json'
    target_id = [
      "00010882",
      "00010855",
      "00010976",
      "00010599"
    ]
    outputs = {
      "00010882" : [],
      "00010855" : [],
      "00010976" : [],
      "00010599" : []
    }
    for i in range(100000):
        r = requests.get(url)
        station_status = r.json()['data']['stations']
        for station in station_status:
            if station['station_id'] in target_id:
                outputs[station['station_id']].append(station)
        with open('dumps/station_status.json', 'w') as f:
            json.dump(outputs, f, indent=4)
        print('[LOG]:DATE ADD:', datetime.datetime.now())
        time.sleep(180)

if __name__ == '__main__':
    get_staion_status()
    