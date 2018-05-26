# coding:utf-8
import random
import math
import numpy as np

CHROMOSOME_SIZE = 15
def init():
    chromosome_state1 = ['000000100101001', '101010101010101']
    chromosome_state2 = ['011000100101100', '001100110011001']
    chromosome_state3 = ['001000100100101', '101010101010101']
    chromosome_state4 = ['000110100100100', '110011001100110']
    chromosome_state5 = ['100000100100101', '101010101010101']
    chromosome_state6 = ['101000100100100', '111100001111000']
    chromosome_state7 = ['101010100110100', '101010101010101']
    chromosome_state8 = ['100110101101000', '000011110000111']
    chromosome_states = [chromosome_state1,chromosome_state2,
                         chromosome_state3,chromosome_state4,
                         chromosome_state5,chromosome_state6,
                         chromosome_state7,chromosome_state8]
    return chromosome_states

def fitness(chromosome_states):
    fitnesses = []
    for chromosome_state in chromosome_states:

        if(chromosome_state[0][0] == '1'):
            x = 10 * (-float(int(chromosome_state[0][1:], 2) - 1) / 16384)
        else:
            x = 10 * (float(int(chromosome_state[0], 2) + 1) / 16384)
        if(chromosome_state[1][0] == '1'):
            y = 10 * (-float(int(chromosome_state[1][1:], 2) - 1) / 16384)
        else:
            y = 10 * (float(int(chromosome_state[1], 2) + 1) / 16384)
        z = y * math.sin(x) + x * math.cos(y)
        fitnesses.append(z)
    return fitnesses

def filter(chromosome_states, fitnesses):
    chromosome_states_new = []
    top1_fitness_index = 0
    for i in np.argsort(fitnesses)[::-1][:8].tolist():
        chromosome_states_new.append(chromosome_states[i])
        top1_fitness_index = i

    return chromosome_states, top1_fitness_index

def crossover(chromosome_states):
    chromosome_states_new = []
    while(chromosome_states):
        chromosome_state = chromosome_states.pop(0)
        for v in chromosome_states:
            pos = random.choice(range(8, CHROMOSOME_SIZE - 1))
            chromosome_states_new.append([1])




if __name__ == '__main__':
    chromosome_states = init()
    last_three = [0] * 3
    last_num = 0
    n = 100
    while n > 0:







