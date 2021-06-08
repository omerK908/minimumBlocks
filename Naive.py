"""
Omer Kalif
Dor Redlich
Daniel Twito
"""
import json


def minimum_blocks(str_1, str_2):
    ans = []
    all_same_partitions = []
    ans.append(split(str_1))
    count = len(str_1)

    for tmp1 in all_partitions(str_1):
        for tmp2 in all_partitions(str_2):
            if one_valued(tmp1, tmp2):
                all_same_partitions.append(tmp1)
                if len(tmp1) <= count:  # are One-valued and on
                    if len(tmp1) < count:
                        ans.clear()
                        # for n in ans:
                        #     if len(n) == count:
                        #         ans.remove(n)
                    count = len(tmp1)
                    ans.append(tmp1)

    with open('all_same_partitions1.txt', 'w') as f:
        f.write(json.dumps(all_same_partitions))

    return ans


def one_valued(tmp1, tmp2):
    if len(tmp1) != len(tmp2):
        return False
    list1 = list(tmp1)
    list2 = list(tmp2)
    for s in list1:
        if s not in list2:
            return False
    return True


def split(word):
    return [char for char in word]


def all_partitions(string):
    for cutpoints in range(1 << (len(string)-1)):
        result = []
        lastcut = 0
        for i in range(len(string)-1):
            if (1<<i) & cutpoints != 0:
                result.append(string[lastcut:(i+1)])
                lastcut = i+1
        result.append(string[lastcut:])
        yield result


s1 = "abaxxxababaxxxxab"
s2 = "baxxxxababaxxxaba"


print("Minimum Blocks: ", minimum_blocks(s1, s2))