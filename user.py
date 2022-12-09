import matplotlib.pyplot as plt
import pyro
import pyro.distributions as dist
from pyro.poutine import trace

class User():
    def generate_pref_vec(self):
        pref_vec = (1,2,3)
        return pref_vec