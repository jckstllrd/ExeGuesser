from re import sub
from urllib.request import urlretrieve
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class RegistrationFormTest(LiveServerTestCase):

    def testform(self):
        selenium = webdriver.Chrome()

        selenium.get('http://127.0.0.1:8000/register/')

        user_name = selenium.find_element_by_id('username')
        p1 = selenium.find_element_by_id('password1')
        p2 = selenium.find_element_by_id('password2')

        submit = selenium.find_element_by_id('submit')

        user_name.send_keys('Test')
        p1.send_keys('password')
        p2.send_keys('password')

        submit.send_keys(Keys.RETURN)

        assert urlretrieve
