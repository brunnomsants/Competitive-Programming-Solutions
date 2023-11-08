import itertools


def solution(num_buns, num_required):
    result_list = [] #defines the list with the results
    all_combs = list(itertools.combinations(range(num_buns),num_required)) #list all the combinations in a range of num of buns and num of requireds
    total = len(all_combs)*num_required #set the total as a product of all combinations and num of requireds
    repeat_times = num_buns - num_required + 1 
    list_combs = list(itertools.combinations(range(num_buns),repeat_times)) #list all combination of num buns limited by repeat times
    for i in range(num_buns):
        result_list.append([])  

    #add the results to the result list

    for i in range(total/repeat_times):
        for j in list_combs[i]:
            result_list[j].append(i)

    return result_list    
