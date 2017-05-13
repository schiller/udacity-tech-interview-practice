# Question 1
# Given two strings s and t, determine whether some anagram of t is a substring of s. 
# For example: if s = "udacity" and t = "ad", then the function returns True. 
# Your function definition should look like: question1(s, t) and return a boolean True or False.

from collections import deque

def question1(s, t):
    if s is not None and t is not None:
        # empty string is substring to any string
        if t == "":
            return True

        t_count = get_letter_dict(t)
        # iterate through s taking len(t) steps
        for i in xrange(len(t) - 1, len(s), len(t)):
            if s[i] in t_count:
                if find_substring(s, i, t_count, len(t)):
                    return True
    return False

""" returns a dict with the letter count for the inputed word """
def get_letter_dict(t):
    t_count = {}
    for letter in t:
        if letter in t_count:
            t_count[letter] += 1
        else:
            t_count[letter] = 1
    return t_count

""" searches for the anagram on left and right of the initial position i """
def find_substring(s, i, t_count, len_t):
    q = deque()
    # walk left searching for anagram letters until one letter does not work
    # append letters on the left of the queue and decrement the letter count
    j = i
    while j >= 0 and j > i - len_t:
        if s[j] in t_count:
            if t_count[s[j]] > 0:
                q.appendleft(s[j])
                t_count[s[j]] -= 1
                j -= 1
            else:
                break
        else:
            break

    # check if anagram was found
    if len(q) == len_t:
        return True

    # now walk right from the initial letter
    # replace exceding left letters with right letters
    j = i + 1
    while j < len(s) and j < i + len_t and len(q) <= len_t:
        if s[j] in t_count:
            if t_count[s[j]] == 0:
                # if letter count is 0, dequeue on the left until we can use it
                k = j - len(q)
                while True:
                    popped = q.popleft()
                    t_count[popped] += 1
                    if popped == s[j]:
                        break
                    k += 1
                    # if we reach the initial letter without finding our letter, give up
                    if k == i:
                        return False
            q.append(s[j])
            t_count[s[j]] -= 1
            j += 1
        else:
            return False

    # check if anagram was found
    if len(q) == len_t:
        return True
        
    return False


print question1(None, None)
# False

print question1("", "")
# True

print question1("udacity", "ad")
# True

print question1("udacity", "ady")
# False