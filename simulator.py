import random
from user import User

class Simulate():
    def simulate(self, step_num):
        ports_setting_list = [ # supply_prob, capacity
          (0.6, 10),
          (0.2, 2),
          (0.2, 2)
        ]
        ports_now_device_num_list = [3,1,1]
        user_queue = [tuple(random.sample([1,2,3], 2))]
        sales = 0
        queue_length_history = []
        ports_state_history = []
        sales_history = []

        waiting_counter = 0

        for step in range(step_num):
            print('========================')
            print('START STEP')
            print('QUEUE LENGTH: ', len(user_queue))
            print('PORTS NOW... ', ports_now_device_num_list)

            prob_user_generate = 1 / (len(user_queue) + 1)

            print()
            print('GENERATING USER...')
            # userが生まれる
            if random.random() < prob_user_generate:
                print('USER GENERATED!!')
                user_pref_vec = User().generate_pref_vec()
                user_queue.append(user_pref_vec)
            else:
                print('USER DIDNOT GENERATE')
            
            print()
            print('GENERATING RIDE...')
            # ride
            if len(user_queue) > 0:
                user_pref_vec = user_queue[0]
                waiting_counter += 1
                for user_pref in user_pref_vec:
                    if 1 <= ports_now_device_num_list[user_pref-1]:
                        print('RIDE DONE!! PORT No.', user_pref)
                        ports_now_device_num_list[user_pref-1] -= 1
                        user_queue.pop()
                        sales += 100
                        waiting_counter = 0
                        break
                    else:
                        sales -= 50
                        print('NO BIKE')
                if  waiting_counter >= 5:
                    print('USER CANNOT WAIT MORE!!')
                    waiting_counter = 0
                    sales -= 100
                    user_queue.pop()

            else:
                print('NO USER WAIR NOW')
            
            # portのsupply追加
            print()
            print('GENERATING SUPPLY...')
            for i in range(len(ports_now_device_num_list)):
                ports_now_device_num = ports_now_device_num_list[i]
                prob_supply = ports_setting_list[i][0]
                capacity = ports_setting_list[i][1]
                if random.random() < prob_supply:
                    if ports_now_device_num < capacity:
                        print('SUPPLY DONE!!')
                        sales += 100
                        ports_now_device_num_list[i] += 1
                    else:
                        sales -= 100
                        print('OVER CAPACITY')

            print('')
            print('STEP DONE!!')
            print('QUEUE LENGTH: ', len(user_queue))
            print('PORTS NOW... ', ports_now_device_num_list)
            print('TOTAL SALES NOW...: ', sales)

            queue_length_history.append(len(user_queue))
            ports_state_history.append(ports_now_device_num_list)
            sales_history.append(sales)
            print('========================')
        return queue_length_history, ports_state_history, sales_history