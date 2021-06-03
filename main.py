import Minimun_Blocks


def run_minimum_blocks():
    s1 = "abcac"
    s2 = "bcaac"
    # s1 = "abaxxxababaxxxxab"
    # s2 = "baxxxxababaxxxaba"
    s1 = "abcaba"
    s2 = "ababca"
    mb = Minimun_Blocks.MinimumBlocks(s1, s2)


if __name__ == '__main__':
    run_minimum_blocks()


