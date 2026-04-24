from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    #1: split the list in candindate lists
    #2: for each list in the candiate, rearrange the characters and check whether the ouput belogns to the initial list
    #3: if yes, then append it to the candiate list, else go to next list

    #candidate_lists = [[candidate]for candidate in strs] #instead of doing this, I can start with an empty list
    #and append the first element of the input list and then go from there.
    candidate_lists = []
    
    inputs = strs[:] #copy the list to avoid modifying the original list.
    for candidate in strs:
        if candidate not in inputs: # if it was removed in a previous iteration
            continue
        current_list = [candidate]
        words_to_remove = []
        candidate_lists.append(current_list)
        inputs.remove(candidate)
        for i, word in enumerate(inputs):
            if sorted(current_list[0]) == sorted(word): # is this the right way to check for anagrams? 
                current_list.append(word) #here we need to 
                words_to_remove.append(word) #remove for the duplicates
        for i in words_to_remove:
            inputs.remove(i)
    return candidate_lists
                
    
                
    