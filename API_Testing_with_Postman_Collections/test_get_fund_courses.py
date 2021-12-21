import requests
import logging
import config

def get_fund_courses():
    try:
        api_url = config.fund_courses_url
        response = requests.get(api_url)
                
        resp_text = response.text
        with open("fund_courses.txt", "w+") as file:
            file.write(resp_text)
                
        code = response.status_code
        print(code)
        
        assert int(code) == 200, "The code does NOT match!"
        logging.info("Fundamental courses are found!")

    except Exception as e:
        logging.exception(e)
        
get_fund_courses()
