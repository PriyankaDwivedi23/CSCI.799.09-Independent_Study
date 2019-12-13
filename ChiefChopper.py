import math

def chiefHopper(arr):
    energyRequired = 0
    totalEnergy = 0
    for i in range(len(arr) - 1, -1, -1):
        currentEnergyNeeded = (energyRequired + arr[i]) / 2
        totalEnergy = math.ceil(currentEnergyNeeded )
        energyRequired = totalEnergy
    return totalEnergy


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = chiefHopper(arr)

    print(result)