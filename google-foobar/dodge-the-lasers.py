import math

def solvenum(num):
    if (num == 0):
      return 0
    squarerootm = "414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641572735013846230912297024924836055850737212644121497099935831"
    n_p = str(int(squarerootm) * num)[:-156]
    if len(n_p) == 0:
      n_p = 0
    else:
      n_p = int(n_p)
    return (n_p + num)*(n_p + num + 1) / 2 - (n_p*(n_p + 1))-solvenum(n_p)

def solution(s):
    return str(int(solvenum(int(s))))