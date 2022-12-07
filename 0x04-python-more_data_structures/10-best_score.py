#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxVal = 0
    maxKey = None
    for k, v in a_dictionary.items():
        if v > maxVal:
            maxVal = v
	    maxKey = k
    return maxKey
