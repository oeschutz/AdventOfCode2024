from itertools import pairwise

def part_one(filename):
    with open(filename) as f:
        reports = [[int(i) for i in report.split()] for report in f]
        t = 0
        for r in reports:
            t += is_safe(r)
        return t

def part_two(filename):
    with open(filename) as f:
        reports = [[int(i) for i in report.split()] for report in f]
        t = 0
        for r in reports:
            s = is_safe(r)
            if not s:
                for i in range(len(r)):
                    r2 = r.copy()
                    r2.pop(i)
                    if is_safe(r2):
                        s = True
                    
            t += s
        return t

def is_safe(report):
    return (all(a < b for a,b in pairwise(report)) or all(a > b for a,b in pairwise(report))) and all(1<=abs(a-b)<=3 for a,b in pairwise(report))
    



if __name__ == "__main__":
    print(part_two("input.txt"))