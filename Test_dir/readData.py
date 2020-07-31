import csv

PATH_TO_CSV = "../Resources/Отзывы/AppStore (за год).csv"

def main():
    i = 0
    # data = {}
    with open(PATH_TO_CSV, newline='', encoding='utf-8') as fd:
        reader = csv.reader(fd, delimiter=",")
        for row in reader:
            # data
            i += 1            
            if i > 5:
                break
            if i < 3:
                continue
            print(row)

if __name__ == "__main__":
    main()
