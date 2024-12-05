def is_safe(report):
    if len(report) < 2:
        return True  # Assuming single-level reports are safe

    differences = [report[i+1] - report[i] for i in range(len(report)-1)]

    if all(1 <= d <= 3 for d in differences):
        return True
    elif all(-3 <= d <= -1 for d in differences):
        return True
    else:
        return False

def count_safe_reports(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    safe_count = 0
    for line in lines:
        report = list(map(int, line.split()))
        if is_safe(report):
            safe_count += 1

    return safe_count

# Example usage
if __name__ == "__main__":
    filename = "input.txt"
    print(count_safe_reports(filename))