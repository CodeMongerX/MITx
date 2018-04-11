'''Write a Python function that returns a list of keys in aDict that map 
to integer values that are unique (i.e. values appear exactly once in 
aDict). The list of keys you return should be sorted in increasing order.
(If aDict does not contain any unique values, you should return an 
empty list.)
This function takes in a dictionary and returns a list.
'''


def uniqueValues(val):
    '''
    aDict: a dictionary
    '''
    # Your code here
    list1 = []
    valkey = val.keys()
    valval = val.values()
    lkey = list(valkey)
    lval = list(valval)
    for i in range(len(lval)):
        if lval.count(lval[i]) == 1:
            list1.append(lkey[i])
    
    print(list1)
    
    return None

#testCases
uniqueValues({1: 1, 2: 2, 3: 3})     
uniqueValues({1: 1, 2: 2, 3: 3})   
uniqueValues({1: 1})
uniqueValues({1: 1, 2: 1, 3: 3})
uniqueValues({2: 2, 3: 3, 4: 4})
uniqueValues({})
uniqueValues({2: 0, 3: 3, 6: 1})
uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0})
uniqueValues({0: 9, 1: 1, 2: 7, 3: 3, 5: 2, 6: 5, 7: 8, 9: 10, 10: 0})
uniqueValues({8: 3, 1: 3, 2: 2})
uniqueValues({2: 2, 5: 0, 7: 3})
uniqueValues({5: 1, 7: 1})
uniqueValues({0: 3, 1: 2, 2: 3, 3: 1, 4: 0, 6: 0, 7: 4, 8: 2, 9: 7, 10: 0})
uniqueValues({0: 2, 1: 3, 2: 0, 3: 6, 7: 2, 9: 3})
uniqueValues({8: 1, 0: 4, 1: 1, 5: 2, 9: 4}) 