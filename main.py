from user import User
from simulator import Simulate
import matplotlib.pyplot as plt

if __name__ == '__main__':
    step_num = 1000
    queue_length_history, ports_state_history, sales_history = Simulate().simulate(step_num)
    steps = range(step_num)


    fig, ax = plt.subplots(2,3)

    ax[0,0].plot(steps, queue_length_history, color='blue', label="queue")
    ax[0,1].plot(steps, [x[0] for x in ports_state_history], color='red',  label="port1_state")
    ax[0,2].plot(steps, [x[1] for x in ports_state_history], color='red',  label="port2_state")
    ax[1,0].plot(steps, [x[2] for x in ports_state_history], color='red',  label="port3_state")
    ax[1,1].plot(steps, [x[3] for x in ports_state_history], color='red',  label="port4_state")
    ax[1,2].plot(steps, sales_history, color='yellow', label="sales")

    for i in range(2):
        for j in range(3):
            ax[i,j].legend()
    fig.subplots_adjust()
    plt.show()