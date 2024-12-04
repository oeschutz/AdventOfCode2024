import re

def part_one(filename):
    with open(filename) as f:
        line = "".join(f.read())
        all_calls = re.findall("(mul\(\d\d?\d?,\d\d?\d?\))", line)
        total = 0
        for call in all_calls:
            first = int(call[call.find("(")+1:call.find(",")])
            second = int(call[call.find(",")+1:call.find(")")])
            total += (first*second)
        return total

    

def part_two(filename):
    with open(filename) as f:
        line = "".join(f.read())
        all_calls = re.findall("mul\(\d\d?\d?,\d\d?\d?\)|do\(\)|don't\(\)", line)
        total = 0
        enabled = True
        for call in all_calls:
            if call == "do()":
                enabled = True
            elif call == "don't()":
                enabled = False
            elif enabled:
                first = int(call[call.find("(")+1:call.find(",")])
                second = int(call[call.find(",")+1:call.find(")")])
                total += (first*second)
        return total

if __name__ == "__main__":
    print(part_two("testinput3.txt"))
    print(part_two("input.txt"))