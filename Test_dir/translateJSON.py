import json

INPUT_FILE = "../Resources/data.json"
OUTPUT_FILE = "../Resources/data_translated.json"

def main():
    with open(INPUT_FILE, "r") as fd:
        data = json.load(fd)
    with open(OUTPUT_FILE, "w") as fd:
        fd.write(json.dumps(data, ensure_ascii=True, indent=4))

if __name__ == "__main__":
    main()
