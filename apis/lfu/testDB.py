import sqlite3
import requests 
import json 
import uuid
from tabulate import tabulate


con = sqlite3.connect("../../db/lfu.db")
cur = con.cursor()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def test():
    cur.execute("SELECT * FROM groups")

    groups = cur.fetchall()
    for group in groups: 
        print(group[0], group[1], group[2])
        print(tabulate(json.loads(group[3])))
    # print(tabulate(json.loads(data[0][3])))

if __name__ == "__main__":
    test()
