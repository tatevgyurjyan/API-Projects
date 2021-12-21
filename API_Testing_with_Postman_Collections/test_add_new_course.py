import requests
import json
import logging
import test_data
import config


def post_new_Course():
    try:           

        api_url = config.add_course_url        
        my_data = test_data.post_data        
        response = requests.post(api_url, json=my_data)                    
        code = response.status_code
     
        assert int(code) == 200, "The code does NOT match!"
        logging.info("New course is added!")
        
    except Exception as e:
        logging.exception(e)
        
    finally:
            json_response = json.loads(response.text)
            new_course_id = json_response['id']
            
    print("New course id is ", json_response['id'])   
    return new_course_id
    
post_new_Course()

