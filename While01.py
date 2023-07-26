def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    s='python1121'
    return s.count('0')+s.count('1')+s.count('2')+s.count('3')+s.count('4')+s.count('5')+s.count('6')+s.count('7')+s.count('8')+s.count('9')
print(main('python1121'))