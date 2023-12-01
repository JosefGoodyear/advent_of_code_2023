

def main():
    total = 0
    with open("input.txt") as doc:
        calibrations = doc.read().splitlines()
    for calibration in calibrations:
        start = 0
        end = -1 
        while not calibration[start].isnumeric() or not calibration[end].isnumeric():
            if not calibration[start].isnumeric():
                start += 1
            if not calibration[end].isnumeric():
                end -= 1
        number = int(calibration[start] + calibration[end])
        total += number
    print(total)


if __name__ == "__main__":
    main()