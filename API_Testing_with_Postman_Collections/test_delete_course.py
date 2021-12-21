import requests
import logging
import config
import test_add_new_course as add


new_course_id = add.post_new_Course() 

def delete_course():
    try:
        api_url = f"https://qwallity2.herokuapp.com/courses/course/{new_course_id}" 
                
        response = requests.delete(api_url)
        code = response.status_code
      
        assert int(code) == 200, "The code does NOT match!"
        logging.info("Course is deleted!")

    except Exception as e:
        logging.exception(e)

delete_course()        
