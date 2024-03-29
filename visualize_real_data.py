import matplotlib.pyplot as plt
import json

def vs(path):
    with open(path) as f:
        station_status = json.load(f)

    target_id = [
      "00010882",
      "00010855",
      "00010976",
      "00010599"
    ]
    fig, ax = plt.subplots(2,2)
    for id in target_id:
      target_station = station_status[id]
      ports_state_history = []
      for log in target_station:
          num_bikes_available = log['num_bikes_available']
          ports_state_history.append(num_bikes_available)
      if target_id.index(id) == 0:
        i, j = 0, 0
      if target_id.index(id) == 1:
        i, j = 1, 0
      if target_id.index(id) == 2:
        i, j = 0, 1
      if target_id.index(id) == 3:
        i, j = 1, 1
      ax[i,j].plot(
        range(len(target_station)),
        ports_state_history,
        color='red',
        label='port_state of ' + id
        )
      ax[i,j].legend()
      
    fig.subplots_adjust()
    plt.show()

if __name__ == '__main__':
    path = 'dumps/station_status.json'
    vs(path)
    path = 'dumps/station_status-2.json'
    vs(path)
    path = 'dumps/station_status-3.json'
    vs(path)
