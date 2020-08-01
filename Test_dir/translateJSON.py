import json

INPUT_FILE = "../Resources/data.json"
OUTPUT_FILE = "../Resources/data_translated.json"

def main():
    i = 0
    min = 0
    max = 100
    with open(INPUT_FILE, "r", encoding="utf-8") as fd:
        data = json.load(fd)
    for info in data:
        i += 1
        if i == max:
            break
        if i < min:
            continue
        print(info['Review'])
        print('------------------------------------')
    # print(json.dumps(data, indent=4, ensure_ascii=False))
    # with open(OUTPUT_FILE, "w") as fd:
    #     fd.write(json.dumps(data, ensure_ascii=False, indent=4))

if __name__ == "__main__":
    main()
