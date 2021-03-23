from typing import Any, Sequence

def seq_seach(a: Sequence, key: Any) -> int:
    i =0

    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1

if __name__ == '__main__':
    num = int(input('Enter the numbers'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

