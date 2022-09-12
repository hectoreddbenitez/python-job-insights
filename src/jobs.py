from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobs_list = []
    with open(path, encoding="utf8") as file:
        read_file = csv.DictReader(file, delimiter=",", quotechar='"')
        for row in read_file:
            jobs_list.append(row)
    return jobs_list
