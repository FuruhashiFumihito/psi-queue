from user import User
from simulator import Simulate
import matplotlib.pyplot as plt

if __name__ == '__main__':
    step_num = 100
    queue_length_history, ports_state_history, sales_history = Simulate().simulate(step_num)
    steps = range(step_num)

    fig = plt.figure()
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax3 = ax1.twinx()

    ax1.plot(steps, queue_length_history, color='blue', label="queue")
    # ax2.plot(steps, [x[0] for x in ports_state_history], color='red',  label="port1_state")
    # ax3.plot(steps, sales_history, color='yellow', label="sales")

    plt.show()