import pandas as pd
import re

def read_data():
    return pd.read_csv("./data/data.csv", sep="\n")

def parse_row(string):
    match_regex = r"([^.]*)\.(.*?)\,(\ .*?)\,( \d*)."
    title, authors, publisher, year= [str_.strip() for str_ in re.match(match_regex, string).groups()]
    return {'title':title, 'authors':authors, 'publisher':publisher, 'year':year}

def dict_list_to_csv(data, filekey):
    data = pd.DataFrame.from_dict(data)
    data.to_csv(f'{filekey}.csv')

def process_data():
    df = read_data()
    successful = []
    failed = []
    for _, row in df.iterrows():
        try:
            successful.append(parse_row(row.Name))
        except AttributeError:
            failed.append(row.Name)
    print("Printing to successful.csv")
    dict_list_to_csv(successful, 'successful')
    print("Printing to failed.csv")
    dict_list_to_csv(failed, 'failed')

