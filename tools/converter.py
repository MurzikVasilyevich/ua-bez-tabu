import argparse
import codecs
import json
import os
import shutil

import pandas as pd
from dict2xml import dict2xml


def main(source, destination):
    converter = Converter(source, destination)
    converter.create_json()
    converter.create_xml()


class Converter:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.dictionary = self.csv2dictionary()

    def csv2dictionary(self):
        os.makedirs(self.destination) if not os.path.exists(self.destination) else None
        shutil.copy(self.source, self.destination)
        df = pd.read_csv(self.source, encoding='utf-8')
        dictionary = {
            k: f.groupby('term')['synonym'].apply(list).to_dict()
            for k, f in df.groupby('group')
        }
        return dictionary

    def create_xml(self):
        xml = dict2xml(self.dictionary)
        with codecs.open(self.destination + "synonyms.xml", "w", "utf-8") as outfile:
            outfile.write(xml)

    def create_json(self):
        json_object = json.dumps(self.dictionary, indent=4, ensure_ascii=False)
        with codecs.open(self.destination + "synonyms.json", "w", "utf-8") as outfile:
            outfile.write(json_object)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert CSV to JSON')
    parser.add_argument('source', type=str, help='Source CSV file')
    parser.add_argument('destination', type=str, help='Destination JSON file')
    args = parser.parse_args()
    main(args.source, args.destination)
    print('Done!')
    exit(0)
