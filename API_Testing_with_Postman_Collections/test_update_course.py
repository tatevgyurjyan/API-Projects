import requests
import logging
import test_data
import json
import test_add_new_course as add

course_id = add.post_new_Course()

def update_course():
    try:
        api_url = f"https://qwallity2.herokuapp.com/course/{course_id}/update"
        
        my_data = test_data.put_data
        response = requests.put(api_url, json=my_data)
        
        resp_text = response.text          
        code = response.status_code        
        
        assert int(code) == 200, "The code does NOT match!"
        logging.info("Course id is updated!")

    except Exception as e:
        logging.exception(e)
        
update_course()
