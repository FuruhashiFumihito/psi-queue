import matplotlib.pyplot as plt
import json

if __name__ == '__main__':
    path = 'dumps/station_status-2.json'
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
      ax[0,0].plot(
        range(len(target_station)), ports_state_history,
        color='red',
        label='port_state')
      
    fig.subplots_adjust()
    plt.show()