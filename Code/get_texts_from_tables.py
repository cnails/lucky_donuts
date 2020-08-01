import csv
import glob


texts = []

for glob_title, field_name, encoding in zip(
        ['google_play_csv/*.csv', 'app_store_csv/*.csv'], ['Review Text', 'Review'],
        ['utf-16', 'utf-8']):
    for file in glob.glob(glob_title):
        print(file)
        with open(file, encoding=encoding) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            header = next(reader)
            review_text_ix = header.index(field_name)
            i = 0
            for row in reader:
                if row[review_text_ix].strip():
                    texts.append(row[review_text_ix].replace('\n', ' ').strip())
                i += 1

with open('../Resources/texts.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(texts))
