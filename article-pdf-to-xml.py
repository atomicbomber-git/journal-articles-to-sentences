#!/usr/bin/python

import os
import typing
import requests
import re
import dotenv

dotenv.load_dotenv()

articles_root_path = os.environ["ARTICLES_ROOT_PATH"]
processed_articles_root_path = os.environ["PROCESSED_ARTICLES_ROOT_PATH"]
grobid_endpoint = os.environ["GROBID_ENDPOINT"]

if (not os.path.isdir(processed_articles_root_path)):
    os.mkdir(processed_articles_root_path)

filepaths = []
for root, directory, files in os.walk(articles_root_path):
    files = [file for file in files if (os.path.splitext(file)[-1] == ".pdf")]

    for file in files:
        filepaths.append(os.path.join(root, file))
        
for index, filepath in enumerate(filepaths):
    filename = os.path.split(filepath)[-1] 
    basename = os.path.splitext(filename)[0]

    output_path = os.path.join(processed_articles_root_path, "{}.xml".format(basename))

    print("Processing {}...".format(filename))

    with open(filepath, "rb") as article_file:
        response = requests.post(
            "{}/api/processFulltextDocument".format(grobid_endpoint),
            data={
                "consolidateHeader": 1,
                "includeRawAffiliations": 1,
                "consolidateCitations": 1,
                "includeRawCitations": 1,
            },
            files={
                "input": (filename, open(filepath, 'rb'), 'application/pdf', {'Expires': '0'})
            }
        )

        if (response.status_code == 200):
            with open(output_path, "w") as output_file:
                output_file.write(response.text)
            print("SUCCESS")
        else:
            print("FAILURE")       
    pass