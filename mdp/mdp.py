"""3D MDP implementation based on examples from "Artificial Intelligence: A Modern Approach"
(Third edition) by Stuart Russell and Peter Norvig.

This is a script library intended to be used with iPython
"""
from utils import *
import sim_init

class MDP:

    def __init__(self, init, actlist, gamma=.9):
        update(self, init=init, actlist=actlist, gamma=gamma, states=set(), reward={})

    def R(self, state):
        "Return a numerical reward for this state."
        return self.reward[state]

    def T(state, action):
        """Transition model returns a list of resulting(state, probability) pairs.
        from the given state and action"""
        abstract

    def actions(self, state):
        return self.actlist

class GridMDP(MDP):
    """A three-dimensional grided MDP. A grid listing rewards must be specified
    Actions are (x, y, z) unit vectors"""
    def __init__(self, grid, init=(0, 0), gamma=.9):
        #grid.reverse()
        MDP.__init__(self, init, actlist=orientations, gamma=gamma)
        update(self, grid=grid, zlen=len(grid[1]), ylen=len(grid), xlen=len(grid[0]),)
        for x in range(self.xlen):
            for y in range(self.ylen):
                for z in range(self.zlen):
                    self.reward[x, y] = grid[z][y][x]
                    self.states.add((x, y, z))

    def T(self, state, action):
        return [(1.0, self.sim(state, action))]

    def sim(self, state, direction):
        "Poor programming and rough approximations abound - this section needs to be revisited"
        "This will return the state which results from applying thrust in the given direction for 60s."
        f_wind=[x * (0.5 * 0.5 * 1.2754 * (np.sqrt(np.sum(np.square(state[0] - state[1]))))) for x in (state[0] - state[1])
        f_prop=[x * 5. for x in direction]"5N thrust"
        f_tot=f_wind + f_prop
        dv=(f_tot / 2.) * 60. "2kg balloon, updated every minute. Rough discrete approximation"
        dx=[x + (dv * 30.) for x in state[2]]
        state1 = list(state)
        state1[0]= state1[0] + dv
        state1[2]= state1[0] + dx
        return if_(state1 in self.states, state1, state)

def value_iteration(mdp, epsilon=0.001):
    U1 = dict([(s, 0) for s in mdp.states])
    R, T, gamma = mdp.R, mdp.T, mdp.gamma
    while True:
        U = U1.copy()
        delta = 0
        for s in mdp.states:
            U1[s] = R(s) + gamma * max([sum([p * U[s1] for (p, s1) in T(s, a)])
                                        for a in mdp.actions(s)])
            delta = max(delta, abs(U1[s] - U[s]))
        if delta < epsilon * (1 - gamma) / gamma:
             return U

def best_policy(mdp, U):
    pi = {}
    for s in mdp.states:
        pi[s] = argmax(mdp.actions(s), lambda a:expected_utility(a, s, U, mdp))
    return pi

def expected_utility(a, s, U, mdp):
    return sum([p * U[s1] for (p, s1) in mdp.T(s, a)])


def policy_iteration(mdp):
    U = dict([(s, 0) for s in mdp.states])
    pi = dict([(s, random.choice(mdp.actions(s))) for s in mdp.states])
    while True:
        U = policy_evaluation(pi, U, mdp)
        unchanged = True
        for s in mdp.states:
            a = argmax(mdp.actions(s), lambda a: expected_utility(a,s,U,mdp))
            if a != pi[s]:
                pi[s] = a
                unchanged = False
        if unchanged:
            return pi

def policy_evaluation(pi, U, mdp, k=20):
    """Returns an updated utility which maps U from each state in the MDP to it's
    utility. This uses an approximation (modified policy iteration)."""
    R, T, gamma = mdp.R, mdp.T, mdp.gamma
    for i in range(k):
        for s in mdp.states:
            U[s] = R(s) + gamma * sum([p * U[s] for (p, s1) in T(s, pi[s])])
    return U