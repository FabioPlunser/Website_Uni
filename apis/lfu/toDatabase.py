import sqlite3
import requests 
import json 

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
    UNDERLINE = '\033[4m'

def parseLfu():
    res = requests.get("http://127.0.0.1:3001/lfu")
    data = json.loads(res.text)
    # cur.execute("DROP TABLE studies")
    # cur.execute("DROP TABLE curriculum")
    # cur.execute("DROP TABLE category")
    # cur.execute("DROP TABLE course")
    # cur.execute("DROP TABLE courseType")
    # cur.execute("DROP TABLE groups")

    cur.execute("""CREATE TABLE IF NOT EXISTS studies 
        (studies_id INTEGER PRIMARY KEY, name TEXT)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS curriculum 
        (studies_id INTEGER, curriculum_id INTEGER, name TEXT, PRIMARY KEY (studies_id, curriculum_id))""")
    cur.execute("""CREATE TABLE IF NOT EXISTS category 
        (studies_id INTEGER, curriculum_id INTEGER, category_id, name TEXT, PRIMARY KEY (studies_id, curriculum_id, category_id))""")
    cur.execute("""CREATE TABLE IF NOT EXISTS course 
        (studies_id INTEGER, curriculum_id INTEGER, category_id, course_id INTEGER, name TEXT, PRIMARY KEY (studies_id, curriculum_id, category_id, course_id))""")
    cur.execute("""CREATE TABLE IF NOT EXISTS courseType 
        (studies_id INTEGER, curriculum_id INTEGER, category_id, course_id INTEGER, lv_number INTEGER, name TEXT, lecturers TEXT, 
        PRIMARY KEY (studies_id, curriculum_id, category_id, course_id, lv_number))""")
    cur.execute('''CREATE TABLE IF NOT EXISTS groups 
        (studies_id INTEGER, curriculum_id INTEGER, category_id, course_id INTEGER, group_id INTEGER, group_number, comment TEXT, date TEXT, location TEXT, time TEXT, PRIMARY KEY (studies_id, curriculum_id, category_id, course_id, group_id))''')



    for studies in data["data"]:
        # print(bcolors.WARNING + json.dumps(obj=data2, indent=4, sort_keys=True) + bcolors.ENDC)
        try:
            cur.execute("INSERT INTO studies (studies_id, name) DISTINCT VALUES (?, ?)", (studies["id"], studies["name"]))
        except:
            cur.execute("UPDATE studies SET name = ? WHERE studies_id = ?", (studies["id"], studies["name"]))
        con.commit()
        curricula = getLfuId(stied["id"])
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
        for curriculum in curricula["data"]:
            # print(bcolors.FAIL + json.dumps(obj=curriculum, indent=4, sort_keys=True) + bcolors().ENDC)
            try:
                cur.execute("INSERT INTO curriculum (studies_id, curriculum_id, name) VALUES (?, ?, ?)", (studies["id"], curriculum["id"], curriculum["name"]))
            except:
                cur.execute("UPDATE curriculum SET name = ? WHERE studies_id = ? AND curriculum_id = ?", (studies["id"], curriculum["id"], curriculum["name"]))
            con.commit()
            category = getLfuId(curriculum.get("id"))
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------

            for cat in category["data"]:
                # print(bcolors.OKBLUE + json.dumps(obj=cat, indent=4, sort_keys=True) + bcolors.ENDC)
                try:
                    cur.execute("INSERT INTO category (studies_id, curriculum_id, category_id, name) VALUES (?, ?, ?, ?)", (studies["id"], curriculum["id"], cat.get("id"), cat.get("name")))
                except:
                    cur.execute("UPDATE category SET name = ? WHERE studies_id = ? AND curriculum_id = ? AND category_id = ?", (studies["id"], curriculum["id"], cat.get("id"), cat.get("name")))
                con.commit()
                courses = getLfuId(cat.get("id"))

        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------

                for course in courses["data"]:
                    # print(bcolors.OKCYAN + json.dumps(obj=course, indent=4, sort_keys=True) + bcolors.ENDC)
                    try:
                        cur.execute("INSERT INTO course (studies_id, curriculum_id, category_id, course_id, name) VALUES (?, ?, ?, ?, ?)", (studies["id"], curriculum["id"], cat.get("id"), course.get("id"), course.get("name")))
                    except:
                        cur.execute("UPDATE course SET name = ? WHERE studies_id = ? AND curriculum_id = ? AND category_id = ? AND course_id = ?", (studies["id"], curriculum["id"], cat.get("id"), course.get("id"), course.get("name")))
                    con.commit()
                    courseType = getLfuId(course.get("id"))
                    if(courseType["success"] == False):
                        continue
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
                    for types in courseType["data"]:
                        print(bcolors.OKGREEN + json.dumps(obj=types, indent=4, sort_keys=True) + bcolors.ENDC)
                        try:
                            cur.execute("INSERT INTO courseType (studies_id, curriculum_id, category_id, course_id, lv_number, name, lecturers) VALUES (?, ?, ?, ?, ?, ?, ?)", (studies["id"], curriculum["id"], cat.get("id"), course.get("id"), types.get("lv_number"), types.get("name"), types.get("lecturers")))
                        except:
                            cur.execute("UPDATE courseType SET name = ?, lecturers = ? WHERE studies_id = ? AND curriculum_id = ? AND category_id = ? AND course_id = ? AND lv_number = ?", (studies["id"], curriculum["id"], cat.get("id"), course.get("id"), types.get("lv_number"), types.get("name"), types.get("lecturers")))
                        con.commit()
                        groups = getCourse(types.get("id"))
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------

                        for group in groups["groups"]:
                            print(bcolors.WARNING + json.dumps(obj=group["times"], indent=4, sort_keys=True) + bcolors.ENDC)
                            for time in group["times"]:
                                try:
                                    cur.execute("INSERT INTO groups (studies_id, curriculum_id, category_id, course_id, group_id, group_number, comment, date, location, time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (studies["id"], curriculum["id"], cat.get("id"), course.get("id"), types["id"], group["number"], time["comment"], time["date"], time["location"], time["time"]))
                                except:
                                    cur.execute("UPDATE groups SET comment = ?, date = ?, location = ?, time = ? WHERE studies_id = ? AND curriculum_id = ? AND category_id = ? AND course_id = ? AND group_id = ? AND group_number = ?", (studies["id"], curriculum["id"], cat.get("id"), course.get("id"), types["id"], group["number"], time["comment"], time["date"], time["location"], time["time"]))
                                con.commit()
                                    
def getLfuId(id):
    res = requests.get(f"http://127.0.0.1:3001/lfu/{id}")
    data = json.loads(res.text)
    return data

def getCourse(id):
    res = requests.get(f"http://127.0.0.1:3001/course/{id}")
    data = json.loads(res.text)
    return data

if __name__ == "__main__":
    parseLfu()
