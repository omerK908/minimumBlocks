"""
Omer Kalif
Dor Redlich
Daniel Twito
"""

import Minimun_Blocks


def run_minimum_blocks():

    s1 = "abaxxxababaxxxxab"
    s2 = "baxxxxababaxxxaba"
    # s1 = "abaxxxababaxxxxabtturffqsqq"
    # s2 = "baxxxxababaxxxabaurfqsqqftt"
    #
    s1 = "2121"
    s2 = "1212"
    mb = Minimun_Blocks.MinimumBlocks(s1, s2)
    print(mb.run())


if __name__ == '__main__':
    run_minimum_blocks()


