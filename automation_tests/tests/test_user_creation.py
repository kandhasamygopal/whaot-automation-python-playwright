
# test_user_creation.py
import csv
from playwright.sync_api import sync_playwright
from automation_tests.page_objects.registration_page import RegistrationPage
import os
import webbrowser


def get_user_data():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'user_data.csv')
    print(f"Looking for file at: {os.path.abspath(file_path)}")
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

def test_user_creation():
    user_data = get_user_data()
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        for user in user_data:
            login_page = RegistrationPage (page)
            page.goto("https://staging.whaot.com/student",wait_until="load")
            
            login_page.signup_click()
            login_page.fill_phone_number(user['phonenumber'])
            login_page.click_proceed_button()
            login_page.enter_otp_values()
            login_page.fill_user_name(user['username'])
            login_page.save_user_name()

        browser.close()
