import matplotlib.pyplot as plt
import pyro
import pyro.distributions as dist
from pyro.poutine import trace
import random

class User():
    def generate_pref_vec(self):
        pref_vec = tuple(random.sample([1,2,3], 2))
        return pref_vec