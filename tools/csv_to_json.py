import codecs
import pandas as pd
import json
import os
import argparse


def main(source, destination):
    df = pd.read_csv(source, encoding='utf-8')

    dictionary = {
        k: f.groupby('term')['synonym'].apply(list).to_dict()
        for k, f in df.groupby('group')
    }

    json_object = json.dumps(dictionary, indent=4, ensure_ascii=False)
    with codecs.open(destination, "w", "utf-8") as outfile:
        outfile.write(json_object)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert CSV to JSON')
    parser.add_argument('source', type=str, help='Source CSV file')
    parser.add_argument('destination', type=str, help='Destination JSON file')
    args = parser.parse_args()
    main(args.source, args.destination)
    print('Done!')
    exit(0)
