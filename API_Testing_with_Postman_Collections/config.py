import logging


logging.basicConfig(filename='test_log.log',
                    format='%(asctime)s: - %(levelname)s:%(message)s', 
                    level=logging.DEBUG)

add_course_url = "https://qwallity3.herokuapp.com/add_course/api"
delete_course_url = "https://qwallity2.herokuapp.com/courses/course/"
advanced_courses_url = "https://qwallity2.herokuapp.com/courses/advanced/api" 
fund_courses_url = "https://qwallity2.herokuapp.com/courses/fundamental/api"