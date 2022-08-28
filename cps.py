# Baby regex matching. Matches a regex
# that contains letters and Kleene-star (e.g. “ab*c” matches
# “abbbbbc” and “ac”)
def matches(string, pattern):
    if len(pattern) < 2:
        return pattern == string
    elif pattern[1] != '*':
        return string[0] == pattern[0] and matches(string[1:], pattern[1:])
    else:
        for i in range(len(string) + 1):
            if (all([string[j] == pattern[0] for j in range(i)]) \
                and matches(string[i:], pattern[2:])):
                import pdb; pdb.set_trace()
                print("made it!")
                return True

    return False



def matches_cps(string, pattern, kont):
    if len(pattern) < 2:
        kont(pattern == string)

    elif pattern[1] != '*':
        if string[0] == pattern[0]:
            matches_cps(string[1:], pattern[1:], kont)
        else:
            kont(False)
    else:
        it = iter(range(len(string) + 1))

        def rec():
            try:
                i = next(it)
                if all([string[j] == pattern[0] for j in range(i)]):
                        matches_cps(string[i:], pattern[2:], lambda b: kont(True) if b else rec())
                else:
                    kont(False)
            except StopIteration:
                kont(False)

        rec()
