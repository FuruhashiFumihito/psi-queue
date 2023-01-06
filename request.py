import requests
import json

# station: https://ckan.odpt.org/dataset/c_bikeshare_gbfs-d-bikeshare/resource/06ddbb21-be3d-4163-ac92-d90127e9bf90

if __name__ == '__main__':
    url = 'https://api-public.odpt.org/api/v4/gbfs/docomo-cycle-tokyo/station_status.json'
    r = requests.get(url)
    station_status_json = r.json()

    with open('dumps/station_status.json', 'w') as f:
      json.dump(station_status_json, f, indent=4)

    