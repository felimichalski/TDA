def equivalent(s1: str, s2: str) -> bool:
    # true if string are equals
    if(s1 == s2):
        return True

    # false if string size is odd
    if(len(s1) % 2 != 0):
        return False
    
    # floor division to get int instead of float
    half: int = len(s1) // 2

    # check if the strings are equivalent recursively
    return (equivalent(s1[:half], s2[half:]) and equivalent(s1[half:], s2[:half])) or (equivalent(s1[:half], s2[:half]) and equivalent(s1[half:], s2[half:]))

def solve() -> str:
    word1: str = input()
    word2: str = input()

    if(equivalent(word1, word2)):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    print(solve())