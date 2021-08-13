"""
Omer Kalif
Dor Redlich
Daniel Twito
"""

import Minimun_Blocks


def run_minimum_blocks():

    s1 = "abaxxxababaxxxxab"
    s2 = "baxxxxababaxxxaba"

    # s1 = "abaxxxababaxxxxabaxxxababaxxxxab"
    # s2 = "baxxxxababaxxxabaaxxxababaxxxxab"

    # "ab axxxababaxxxxab axxxaba baxxxxab"
    # "baxxxxab ab axxxaba axxxababaxxxxab"

    # s1 = "xxabbacbccbxxxa"
    # s2 = "bbacxxaxxxabccb"

    mb = Minimun_Blocks.MinimumBlocks(s1, s2)
    print(mb.run())


if __name__ == '__main__':
    run_minimum_blocks()


