def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    x=len(s)
    i=0
    sum=0
    while x>0:
        x-=1
        if s[i].islower():
            sum+=1
        i+=1
    return sum
print(main('Python'))