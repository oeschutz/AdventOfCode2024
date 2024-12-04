def part_one(filename):
    with open(filename) as f:
        first = []
        second = []
        for line in f:
            first.append(int(line.split()[0]))
            second.append(int(line.split()[1]))
        total_dist = 0
        while len(first) > 0:
            low_first = min(first)
            first.remove(low_first)
            low_second = min(second)
            second.remove(low_second)
            total_dist += abs(low_first - low_second)
        return total_dist

def part_two(filename):
    with open(filename) as f:
        first = []
        second = []
        for line in f:
            first.append(int(line.split()[0]))
            second.append(int(line.split()[1]))
        similarity = 0
        for num in first:
            similarity += (second.count(num) * num)
        return similarity

if __name__ == "__main__":
    print(part_one("aoc_day1_input.txt"))
    print(part_two("aoc_day1_input.txt"))