#!/usr/bin/env python
#-*-coding:utf-8-*-

## percentile.py


def main():

    list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

    print calc_percentile(list, 0.95)


def calc_percentile(list, p):
    list.sort(key = float)

    length = len(list)
    rank = ((length - 1) * p)
    d = rank - int(rank)

    result = float(list[int(rank)]) + (float(list[int(rank + 1)]) - float(list[int(rank)])) * d

    return result

if __name__ == "__main__":

    main()
