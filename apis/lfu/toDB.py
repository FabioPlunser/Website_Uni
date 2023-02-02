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
    MAGENTA = "\x1B[35m"
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

colors = [bcolors.OKBLUE, bcolors.OKCYAN, bcolors.OKGREEN, bcolors.WARNING, bcolors.MAGENTA, bcolors.FAIL]
def dropTables():
    cur.execute("DROP TABLE studies")
    cur.execute("DROP TABLE curriculum")
    cur.execute("DROP TABLE category")
    cur.execute("DROP TABLE course")
    cur.execute("DROP TABLE courseType")
    cur.execute("DROP TABLE groups")

def createTables():
    cur.execute("""CREATE TABLE IF NOT EXISTS studies (studies_id INTEGER PRIMARY KEY, name TEXT)""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS curriculum (studies_id INTEGER, curriculum_id INTEGER, name TEXT, PRIMARY KEY (studies_id, curriculum_id))""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS category (curriculum_id INTEGER, category_id, name TEXT, PRIMARY KEY (curriculum_id, category_id, name))""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS course (category_id, course_id INTEGER, name TEXT, PRIMARY KEY (category_id, course_id, name))""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS courseType (category_id, course_id INTEGER, name TEXT, lecturers TEXT, PRIMARY KEY (category_id, course_id))""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS groups (course_id INTEGER, group_id INTEGER, group_number, times TEXT, id UUID, PRIMARY KEY (course_id, group_id, group_number, times, id))""")

def studies():
    res = requests.get("http://127.0.0.1:3001/lfu")
    studies = json.loads(res.text)
    print(bcolors.OKGREEN + tabulate(studies["data"]) + bcolors.ENDC)
    for study in studies.get("data"): 
        print(bcolors.OKGREEN + json.dumps(study, indent=4) + bcolors.ENDC)
        cur.execute("INSERT INTO studies VALUES (?, ?)", (study.get("id"), study.get("name")))
        con.commit()
        curricula(study["id"])
    
def curricula(id):
    res = requests.get(f"http://127.0.0.1:3001/lfu/{id}")
    curricula = json.loads(res.text)
    print(bcolors.OKBLUE + tabulate(curricula["data"]) + bcolors.ENDC)
    for curriculum in curricula["data"]:
        try:
            cur.execute("INSERT INTO curriculum VALUES (?, ?, ?)", (id, curriculum.get("id"), curriculum.get("name")))
            con.commit()
        except Exception as e: 
            print(e)
            print(bcolors.FAIL + "curricula: \n" + json.dumps(curriculum, indent=4) + bcolors.ENDC)
        categories(curriculum["id"])

def categories(id):
    res = requests.get(f"http://127.0.0.1:3001/lfu/{id}")
    categories = json.loads(res.text)
    print(bcolors.OKCYAN + tabulate(categories["data"]) + bcolors.ENDC)
    if(categories["success"]):
        for category in categories["data"]:
            try:
                cur.execute("INSERT INTO category VALUES (?, ?, ?)", (id, category.get("id"), category.get("name")))
                con.commit()
            except Exception as e: 
                print(e)
                print(bcolors.FAIL + "categories: \n" + json.dumps(category, indent=4) + bcolors.ENDC)
            courses(category["id"])


def courses(id):
    res = requests.get(f"http://127.0.0.1:3001/lfu/{id}")
    courses = json.loads(res.text)
    # print(bcolors.MAGENTA + tabulate(courses["data"]) + bcolors.ENDC)
    if(courses["success"]):
        jsonType = courses["type"]
        for course in courses["data"]:
            try:
                cur.execute("INSERT INTO course VALUES (?, ?, ?)", (id, course.get("id"), course.get("name")))
                con.commit()
            except Exception as e: 
                print(e)
                print(bcolors.FAIL + "courses: \n" + json.dumps(course, indent=4) + bcolors.ENDC)
            if jsonType == "CourseDetails":
                groups(course["id"])
            else:
                courseTypes(course["id"])

def courseTypes(id):
    res = requests.get(f"http://127.0.0.1:3001/lfu/{id}")
    courseTypes = json.loads(res.text)
    # print(bcolors.WARNING + tabulate(courses["data"]) + bcolors.ENDC)
    if(courseTypes["success"]):
        for courseType in courseTypes["data"]:
            try:
                cur.execute("INSERT INTO courseType VALUES (?, ?, ?, ?)", (id, courseType.get("id"), courseType.get("name"), courseType.get("lectures")))
                con.commit()
            except Exception as e: 
                print(e)
                print(bcolors.FAIL + "courseTypes: \n" + json.dumps(courseType, indent=4) + bcolors.ENDC)

            groups(courseType["id"])

def groups(id):
    res = requests.get(f"http://127.0.0.1:3001/course/{id}")
    groups = json.loads(res.text)

    if(groups["success"]):
        for group in groups["groups"]:
            print(colors[id%5])
            print(id, groups["id"])
            print(tabulate(group["times"]))
            print(bcolors.ENDC)

            try:
                cur.execute("INSERT INTO groups VALUES (?, ?, ?, ?, ?)", (id, groups.get("id"), group.get("number"), json.dumps(group.get("times")), f"{uuid.uuid4()}"))
                con.commit()
            except Exception as e: 
                print(e)
                print(bcolors.FAIL + "groups: \n" + json.dumps(group, indent=4) + bcolors.ENDC)

def getLfuId(id):
    res = requests.get(f"http://127.0.0.1:3001/lfu/{id}")
    data = json.loads(res.text)
    return data

def getCourse(id):
    res = requests.get(f"http://127.0.0.1:3001/course/{id}")
    data = json.loads(res.text)
    return data


def test():
    cur.execute("SELECT * FROM groups")

    groups = cur.fetchall()
    for group in groups: 
        print(group[0], group[1], group[2])
        print(tabulate(json.loads(group[3])))


if __name__ == "__main__":
    try:
        dropTables()
    except Exception as e: 
        print(e)
        print("no tables to drop")
        exit
    
    try:
        createTables()
    except Exception as e: 
        print(e)
    
    studies()
