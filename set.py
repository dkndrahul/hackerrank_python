def average(array):
    average_heights = sum(set(array)) / len(set(array))
    return average_heights
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)