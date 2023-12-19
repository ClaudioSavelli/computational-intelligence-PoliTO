from itertools import combinations
from collections import namedtuple, defaultdict
from random import choice
from copy import deepcopy

from tqdm.auto import tqdm
import numpy as np

MAGIC = [2, 7, 6, 9, 5, 1, 4, 3, 8]

State = namedtuple('State', ['x', 'o'])

def print_board(pos):
    """Nicely prints the board"""
    for r in range(3):
        for c in range(3):
            i = r * 3 + c
            if MAGIC[i] in pos.x:
                print('X', end='')
            elif MAGIC[i] in pos.o:
                print('O', end='')
            else:
                print('.', end='')
        print()
    print()

def win(elements):
    """Checks is elements is winning"""
    return any(sum(c) == 15 for c in combinations(elements, 3))

def state_value(pos: State):
    """Evaluate state: +1 first player wins"""
    if win(pos.x):
        return 1
    elif win(pos.o):
        return -1
    else:
        return 0
    
def random_game():
    """Plays a random game"""
    trajectory = list()
    state = State(set(), set())
    available = set(range(1, 9+1))
    while available:
        x = choice(list(available))
        state.x.add(x)
        trajectory.append(deepcopy(state))
        available.remove(x)
        if win(state.x) or not available:
            break

        o = choice(list(available))
        state.o.add(o)
        trajectory.append(deepcopy(state))
        available.remove(o)
        if win(state.o):
            break
    return trajectory

# moves that can be made by the agent, the human and the random player

def agent_move(state: State, value_dictionary, player='x', trick=False):
    """Agent move"""
    legal_moves = set(range(1, 9+1)) - state.x - state.o
    best_move = None 
    if player == 'x' or player == 'o' and not trick:
        best_value = -np.inf
    elif player == 'o' and trick:
        best_value = np.inf 
    for move in legal_moves:
        next_state = State(state.x | {move} if player == 'x' else state.x, state.o | {move} if player == 'o' else state.o)
        next_hashable_state = (frozenset(next_state.x), frozenset(next_state.o))
        if value_dictionary[next_hashable_state] > best_value or (value_dictionary[next_hashable_state] < best_value and player == 'o' and trick):
            best_move = move
            best_value = value_dictionary[next_hashable_state]
        
    if best_move is None:
        print('No best move')
        return choice(list(set(range(1, 9+1)) - state.x - state.o))
    return best_move

def random_move(state: State):
    """Random move"""
    return choice(list(set(range(1, 9+1)) - state.x - state.o))

# Basic agent methods, where the agent has complete knowledge of the game and can play only as X

def play_game(first_player_move, second_player_move, value_dictionary, agent_player = -1, trick=False):
    """Plays a game"""
    state = State(set(), set())
    while True: 
        if agent_player == 1:
            state.x.add(agent_move(state, value_dictionary, 'x', trick))
        else:
            state.x.add(first_player_move(state))
        if win(state.x):
            #print('X wins')
            return "Player 1"
        elif not set(range(1, 9+1)) - state.x - state.o:
            #print('Draw')
            return 'Draw'
        if agent_player == 2:
            state.o.add(agent_move(state, value_dictionary, 'o', trick))
        else:
            state.o.add(second_player_move(state))
        if win(state.o):
            #print('O wins')
            return "Player 2"
        
def evaluate(player1, player2, value_dictionary, agent_player=-1, games=10_000, trick = False):
    """Evaluate the agent"""
    results = np.array([])
    for _ in tqdm(range(games)):
        res = play_game(player1, player2, value_dictionary, agent_player, trick)
        results = np.append(results, res)
    return results

def print_results(results): 
    """Prints the results of the evaluation"""
    value, counts = np.unique(results, return_counts=True)

    if 'Player 2' not in value:
        value = np.append(value, 'Player 2')
        counts = np.append(counts, 0)
    if 'Draw' not in value:
        value = np.append(value, 'Draw')
        counts = np.append(counts, 0)
    if 'Player 1' not in value:
        value = np.append(value, 'Player 1')
        counts = np.append(counts, 0)

    print(value, counts / counts.sum())

# Train Loop for basic agent
    
def train_loop(epsilon, training_steps):
    value_dictionary = defaultdict(float)
    hit_state = defaultdict(int)
    for steps in tqdm(range(training_steps)):
        trajectory = random_game()
        final_reward = state_value(trajectory[-1])
        for state in trajectory:
            hashable_state = (frozenset(state.x), frozenset(state.o))
            hit_state[hashable_state] += 1
            value_dictionary[hashable_state] = value_dictionary[
                hashable_state
            ] + epsilon * (final_reward - value_dictionary[hashable_state])
    return value_dictionary, hit_state

# Complete agent methods, where the agent has complete knowledge of the game and can play both as X and O

def complete_train_loop(epsilon, training_steps):
    value_dictionary_X = defaultdict(float)
    value_dictionary_O = defaultdict(float)
    hit_state = defaultdict(int)

    for steps in tqdm(range(training_steps)):
        trajectory = random_game()
        final_reward = state_value(trajectory[-1])
        for state in trajectory:
            hashable_state = (frozenset(state.x), frozenset(state.o))
            hit_state[hashable_state] += 1

            # X
            value_dictionary_X[hashable_state] = value_dictionary_X[
                hashable_state
            ] + epsilon * (final_reward - value_dictionary_X[hashable_state])

            # O
            value_dictionary_O[hashable_state] = value_dictionary_O[
                hashable_state
            ] + epsilon * (-final_reward - value_dictionary_O[hashable_state])

    complete_value_dictionary = {"x": value_dictionary_X, "o": value_dictionary_O}
    return complete_value_dictionary, hit_state

def complete_play_game(first_player_move, second_player_move, complete_value_dictionary, agent_player = -1):
    """Plays a game"""
    state = State(set(), set())
    while True:
        if agent_player == 1:
            state.x.add(complete_agent_move(state, complete_value_dictionary, 'x'))
        else:
            state.x.add(first_player_move(state))
        if win(state.x):
            #print('X wins')
            return "Player 1"
        elif not set(range(1, 9+1)) - state.x - state.o:
            #print('Draw')
            return 'Draw'
        if agent_player == 2:
            state.o.add(complete_agent_move(state, complete_value_dictionary, 'o'))
        else:
            state.o.add(second_player_move(state))
        if win(state.o):
            #print('O wins')
            return "Player 2"

def complete_evaluate(player1, player2, complete_value_dictionary, agent_player = -1, games=10_000):
    """Evaluate the agent"""
    if agent_player == -1:
        results = np.array([])
        for _ in tqdm(range(games)):
            res = play_game(player1, player2)
            results = np.append(results, res)
    elif agent_player == 1 or agent_player == 2:
        results = np.array([])
        for _ in tqdm(range(games)):
            res = complete_play_game(first_player_move=player1, 
                                     second_player_move=player2,
                                     complete_value_dictionary=complete_value_dictionary,
                                     agent_player = agent_player)
            results = np.append(results, res)
    else:
        print("Invalid agent player")
        return None
    
    return results

def complete_agent_move(state: State, complete_value_dictionary, player = 'x'):
    """Agent move"""
    value_dictionary = complete_value_dictionary[player]
    legal_moves = set(range(1, 9+1)) - state.x - state.o
    best_move = None 
    best_value = -np.inf
    for move in legal_moves:
        next_state = State(state.x | {move} if player == 'x' else state.x, state.o | {move} if player == 'o' else state.o)
        next_hashable_state = (frozenset(next_state.x), frozenset(next_state.o))
        if value_dictionary[next_hashable_state] > best_value:
            best_move = move
            best_value = value_dictionary[next_hashable_state]
        
    if best_move is None:
        print('No best move')
        return choice(list(set(range(1, 9+1)) - state.x - state.o))
    return best_move