Application URL to work with: http://qwallity3.herokuapp.com/

Test Scenario:
                        Get fundamental courses
                        Get advanced courses
                        Add new course with data
                        Update already existing course with new data
                        Delete course

TODO:                   pip install selenium requests

Impotred Libraries:     logging, requests, json

Tests to be run -->

                        test_get_fund_courses.py -  retrieves fundamental courses 
                        test_get_adv_courses.py  -  retrieves advanced courses 
                        test_add_new_course.py   -  adds a new course in advanced courses
                        test_update_course.py    -  updates course data 
                        test_delete_course.py    -  delets an existing course

test_data.py:           includes test data for 'post' and 'put' requests 

config.py:              includes configuration data for logging and requests

Run result files:       test_log.txt
                        advanced_courses.txt (stores advanced courses)
                        fund_courses.txt (stores fundamental courses)

Other files in package:

            Heroku.app.postman_collection.json  -  same tests written and executed in Postman
            Heroku.app.postman_test_run.json    -  tests collection run result 

Tests should be run in Python. 
