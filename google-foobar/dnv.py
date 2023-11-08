
import numpy as np
# Returns indexes of active and the terminal states
def states(matrix):
    active, terminal = [], []
    for rowN, row in enumerate(matrix):
        (active if sum(row) else terminal).append(rowN)
    return(active,terminal)

# Convert elements of array in simplest form
def simplify_form(B):
    B = B.round().astype(int).A1                   #convert np.matrix to np.array
    gcd = np.gcd.reduce(B)
    B = np.append(B, B.sum())                     
    return (B / gcd).astype(int)
#Solution function
def solution(m):
    active, terminal = states(m)
    if 0 in terminal:                             
        return [1] + [0]*len(terminal[1:]) + [1]
    m = np.matrix(m, dtype=float)[active, :]       
    rowssum = np.prod(m.sum(1))                 
    P = m / m.sum(1)                               
    Q, R = P[:, active], P[:, terminal]           
    I = np.identity(len(Q))
    N = (I - Q) ** (-1)                            
    B = N[0] * R * rowssum / np.linalg.det(N)   
    return simplify_form(B)