from collections import Counter

def solution(participant, completion):
    part_count = Counter(participant)
    dup_part = []
    for key, value in part_count.items():
        if value >= 2:
            dup_part.append(key)
    non_completion = list(set(participant) - set(completion))
    
    alls = dup_part + non_completion
    alls_count = Counter(alls)
    for key, value in alls_count.items():
        answer = key
    return answer