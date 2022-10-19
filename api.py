from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from functools import partial
from flask import *
import json
import time

app = Flask(__name__)


@app.route('/api/login', methods=['GET'])
def api():
    try:
        args = request.args
        username = args.get("username")
        password = args.get("password")
        options = Options()
        options.headless = True
        # driver = webdriver.Chrome(options=options)
        driver = webdriver.Chrome()
        driver.get("https://lms.uibk.ac.at/Shibboleth.sso/Login?SAMLDS=1&target=https://lms.uibk.ac.at/shib/&entityID=https%3A%2F%2Fidp.uibk.ac.at%2Fidp%2Fshibboleth")
        user = driver.find_element("name", "j_username")
        user.clear()
        user.send_keys(username)
        passwd = driver.find_element("name", "j_password")
        passwd.clear()
        passwd.send_keys(password)
        driver.find_element("name", "_eventId_proceed").click()
        driver.find_element(By.LINK_TEXT, "Kurse").click()
        tbody = driver.find_element(By.TAG_NAME, "tbody")
        row = tbody.text.split("\n")
        data = {"status": "success",
                "data": row,
                "time": time.time(),
                "code": 200,
                "cookies": driver.get_cookies()}
        driver.quit()
    except:
        return jsonify({"status": "error",})
    return data


if __name__ == '__main__':
    app.run(debug=True, port=3000)
