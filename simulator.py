import random
from user import User

class Simulate():
    def simulate(self):
        steps = 10
        ports_setting_list = [ # supply_prob, capacity
          (0.7, 10),
          (0.3, 2),
          (0.2, 2)
        ]
        ports_now_device_num_list = [3,1,1]
        prob_user_generate = 0.4
        user_queue = [(1,2,3)]

        for step in range(steps):
            print('========================')
            print('QUEUE LENGTH: ', len(user_queue))
            print('PORTS NOW... ', ports_now_device_num_list)
            # userが生まれる
            if random.random() < prob_user_generate:
                print('USER GENERATED!!')
                user_pref_vec = User().generate_pref_vec()
                user_queue.append(user_pref_vec)
            
            # ride
            if len(user_queue) > 0:
              user_pref_vec = user_queue[0]
              for user_pref in user_pref_vec:
                  if 1 <= ports_now_device_num_list[user_pref-1]:
                      print('RIDE DONE!! PORT No.', user_pref)
                      ports_now_device_num_list[user_pref-1] -= 1
                      user_queue.pop()
                      break
                  else:
                    print('LESS CAPACITY')
            else:
              print('NO USER WAIR NOW')
            
            # portのsupply追加
            for i in range(len(ports_now_device_num_list)):
                ports_now_device_num = ports_now_device_num_list[i]
                prob_supply = ports_setting_list[i][0]
                capacity = ports_setting_list[i][1]
                if random.random() < prob_supply:
                    if ports_now_device_num < capacity:
                        print('SUPPLY DONE!!')
                        ports_now_device_num_list[i] += 1
                    else:
                        print('OVER CAPACITY')

            print('')
            print('STEP DONE!!')
            print('QUEUE LENGTH: ', len(user_queue))
            print('PORTS NOW... ', ports_now_device_num_list)
            print('========================')