import csv, json

PATH_TO_CSV = "../Resources/Отзывы/AppStore (за год).csv"

def main():
    with open("../Resources/data.json", "r") as fd:
        data = json.load(fd)
    for d in data:
        d['readed'] = 0
    with open("../Resources/data.json", "w") as fd:
        fd.write(json.dumps(data))
    # i = 0
    # # data = {}
    # with open(PATH_TO_CSV, newline='', encoding='utf-8') as fd:
    #     reader = csv.reader(fd, delimiter=",")
    #     for row in reader:
    #         # data
    #         i += 1            
    #         if i > 5:
    #             break
    #         if i < 3:
    #             continue
    #         print(row)

if __name__ == "__main__":
    main()
