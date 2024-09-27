import random
import time
# naive search: scanning through an entire list and ask if it's equal to the target
# if yes, return the index. if no, return -1.

# define naive search
def naive_search(l, target):
    # example, l = [1, 3, 10, 12], if 10 is our target. search through list, return 2
    for i in range(len(l)): # for every single index, if "l" at that index is the target, return that index
        if l[i] == target: 
            return i
    return -1 # if not, return -1

# define binary search
# leverage the fact that the list is SORTED.

def binary_search(l, target, low = None, high = None): # lowest indices, highest indices
    if low is None:
         low = 0 # lowest possible index we can check
    if high is None:
         high = len(l) - 1 # length of list minus 1, since it starts at 0
    # if the high bound is ever less than the low bound, that should never happen.
    if high < low: # the case that the element isn't in the list
         return -1
    # example l = [1, 3, 5, 10, 12], if 10 is our target, it should return 3.
    # define the midpoint (length of the list, divided by 2, rounded down.)
    midpoint  = (low + high) // 2 # 2
    if l[midpoint] == target:
        return midpoint # if the midpoint is our target value, return the midpoint
    elif target < l[midpoint]:
            return binary_search(l, target, low, midpoint - 1)
        # use recursion
    else: 
        # target > l[midpoint]
        return binary_search(l, target, midpoint + 1, high)
    
if __name__ == '__main__':
    l = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(l, target))
    print(binary_search(l, target))

# now, let's do some timing analysis. 
    length = 10000 # build a sorted list of 10000
    sorted_list = set()
    while len(sorted_list) < length:
         sorted_list.add(random.randint(-3 * length, 3*length)) # add some upper and lower bounds
         # gives us a range of -30000 to 30000
    sorted_list = sorted(list(sorted_list)) # make the list sorted

    # add time component
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target) # iterate through every item in the list
    end = time.time()
    print("Naive Search time: ", (end - start)/length, "seconds")

# 0.00024052760601043702 seconds (NAIVE)

    # do the same for binary search
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target) # iterate through every item in the list
    end = time.time()
    print("Binary Search time: ", (end - start)/length, "seconds")

#  3.847312927246094e-06 seconds (BINARY)
