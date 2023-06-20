def main(a, b):
    
    '''Find the remainder when a is divided by b and return it.
    
    Args:
        a (int): a number
        b (int): a number
        
    Returns:
        int: the result.
    '''
    return a%b
a,b = int(input("a = ")),int(input("b = "))
print(main(a,b))