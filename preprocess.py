#!/usr/bin/python

import dotenv
import os
import xml.etree.ElementTree as ElementTree
from bs4 import BeautifulSoup
import spacy


dotenv.load_dotenv()
processed_articles_root_path = os.environ["PROCESSED_ARTICLES_ROOT_PATH"]

nlp = spacy.load("en_core_web_sm")

frequency_map = {}



def get(target_list:list, index, default=None):
    max_index = len(target_list)

    if index not in range(0, max_index):
        return default
    else:
        return target_list[index]

def ngram(target:list, n: int) -> list:
    for i in range(0, len(target) + (n - 1)):
        yield [j for j in range(i, i + n)]


for root, directory, filenames in os.walk(processed_articles_root_path):
    xml_filenames = [filename for filename in filenames if os.path.splitext(filename)[-1] == ".xml"]

    test_list = [10, 11, 12]
    print([x for x in ngram(test_list, 3)])



    # for xml_filename in xml_filenames:
    #     # print("Processing {}...".format(xml_filename))

    #     full_xml_filepath = os.path.join(root, xml_filename)

    #     xml_tree = BeautifulSoup(        
    #         open(full_xml_filepath, "r").read(),
    #         "lxml"
    #     )

    #     for tag in xml_tree.find_all("p"):
    #         doc = nlp(tag.text)

    #         for sentence in doc.sents:
    #             tokens = [
    #                 token for token in sentence if 
    #                     (not token.is_punct) and
    #                     (not token.is_bracket) and
    #                     (not token.like_url)
    #             ]

    #             if (len(tokens) < 6):
    #                 continue

    #             for (i in range(0, len(tokens + 2))):
    #                 print("{}-{}-{}".format(


    #                 )))

    #             print(tokens)


