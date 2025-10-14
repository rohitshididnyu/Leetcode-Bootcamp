from collections import Counter

def findAnagrams(s: str, p: str):
    res = []
    p_count = Counter(p)
    s_count = Counter()
    
    p_len = len(p)
    
    for i, ch in enumerate(s):
        s_count[ch] += 1  # add current char
        
        # shrink the window if it's too big
        if i >= p_len:
            left_char = s[i - p_len]
            s_count[left_char] -= 1
            if s_count[left_char] == 0:
                del s_count[left_char]
        
        # compare the two count maps
        if s_count == p_count:
            res.append(i - p_len + 1)
    
    return res
