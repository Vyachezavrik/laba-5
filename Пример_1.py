#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# Ввести список А из 10 элементов, найти сумму элементов, меньших по модулю 5, и вывести ее на экран.

if __name__ == '__main__':
    # Ввести список одной строкой.
    A = list(map(int, input("Ввести список одной строкой:").split()))
    # Проверить количество элементов списка.
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    # Найти искомую сумму.
    s = 0
    for item in A:
        if abs(item) < 5:
            s += item
    print(s)