import sys

def main():
    left_list = []
    right_list = []

    for line in sys.stdin:
        a, b = map(int, line.strip().split())
        left_list.append(a)
        right_list.append(b)

    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    total_distance = sum(abs(a - b) for a, b in zip(left_sorted, right_sorted))
    print(total_distance)

if __name__ == "__main__":
    main()