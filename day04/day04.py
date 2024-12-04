def part_one(filename):
    with open(filename) as f:
        array = [line.strip() for line in f]
        h = len(array)
        w = len(array[0])
        total = 0
        for i in range(h):
            for j in range(w):
                if array[i][j] == 'X':
                    # check for surrounding m
                    if i-3 >= 0 and j-3 >= 0 and array[i-1][j-1] == "M" and array[i-2][j-2] == "A" and array[i-3][j-3] == "S":
                        total += 1
                    if i-3 >= 0 and array[i-1][j] == "M" and array[i-2][j] == "A" and array[i-3][j] == "S":
                        total += 1
                    if i-3 >=0 and j+3 < w and array[i-1][j+1] == "M" and array[i-2][j+2] == "A" and array[i-3][j+3] == "S":
                        total += 1
                    if j+3 < w and array[i][j+1] == "M" and array[i][j+2] == "A" and array[i][j+3] == "S":
                        total += 1
                    if i+3 < h and j+3 < w and array[i+1][j+1] == "M" and array[i+2][j+2] == "A" and array[i+3][j+3] == "S":
                        total += 1
                    if i+3 < h and array[i+1][j] == "M" and array[i+2][j] == "A" and array[i+3][j] == "S":
                        total += 1
                    if i+3 < h and j-3 >= 0 and array[i+1][j-1] == "M" and array[i+2][j-2] == "A" and array[i+3][j-3] == "S":
                        total += 1
                    if j-3 >=0 and array[i][j-1] == "M" and array[i][j-2] == "A" and array[i][j-3] == "S":
                        total += 1
        return total

def part_two(filename):
    with open(filename) as f:
        array = [line.strip() for line in f]
        h = len(array)
        w = len(array[0])
        total = 0
        for i in range(1, h-1):
            for j in range(1, w-1):
                if array[i][j] == "A":
                    if (array[i-1][j-1] == "M" and array[i+1][j+1] == "S") or (array[i-1][j-1] == "S" and array[i+1][j+1] == "M"):
                        if (array[i-1][j+1] == "M" and array[i+1][j-1] == "S") or (array[i-1][j+1] == "S" and array[i+1][j-1] == "M"):
                            total += 1
        return total
                    


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))