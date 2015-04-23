"""
Demonstrate use of the TwoStateMarkovChain class.

Created Mar 20, 2015 by Tom Loredo
"""

import numpy as np
import scipy
import matplotlib as mpl
from matplotlib.pyplot import *
from scipy import *
from scipy import stats

# try:
#     import myplot
# except ImportError:
#     pass

from two_state_markov import TwoStateMarkovChain


ion()


def init_at_0():
    """
    Initial state sampler returning state 0.
    """
    return 0

# Distribution for a random initial state:
init_half = stats.binom(1, .5).rvs

tsmc = TwoStateMarkovChain(.07, .03)

# Simulate 1000 paths of length 30.
tsmc.sim_paths(1000, init_at_0, 30)
#tsmc.sim_paths(1000, init_half, 30)

tsmc.plot_evol()