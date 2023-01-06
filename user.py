import matplotlib.pyplot as plt
import pyro
import pyro.distributions as dist
from pyro.poutine import trace
import random

class User():
    def generate_pref_vec(self):
        pref_vec = tuple(
                random.sample([1,2,3,4],
                 random.sample([1,2,3,4],1)[0]
                 ))
        return pref_vec