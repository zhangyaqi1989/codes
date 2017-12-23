# import numpy as np
# import matplotlib.pyplot as plt
# import dis

if __name__ == "__main__":
    print("Hello World")
    s = open('test.py').read()
    c = compile(s, 'test.py', 'exec')
    print(list(c.co_code))

