'''
Name: Jack Swelstad
Date: 10/17/23
Description: Find the mean of the numbers
'''

from typing import List


def findMean(listNums: List[int], num: int) -> int:
    total: int = 0
    for i in listNums:
        total += i

    return total // num


def main() -> None:

    strNumTemps = input()
    inputStr = input()

    intTemperatures = []
    strTemperatures = []
    intNumTemps = int(strNumTemps)

    strTemperatures = inputStr.split()

    for i in strTemperatures:
        intTemperatures.append(int(i))

    print(findMean(intTemperatures, intNumTemps))


if __name__ == "__main__":
    main()
