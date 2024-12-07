#user_login.py
from playwright.sync_api import Page

class RegistrationPage:
    def __init__(self,page: Page):
        self.page = page

        # Click the signup/signin menu button
    
        self.signup_button = page.locator("//*[@id='sideMenu']/ul[1]/li[1]")

        # click the phone number field
        self.phone_number = page.locator("//*[@id='wrapper']/div/div/div[2]/div/input")

        # Click the proceed to button
        self.proceed_button = page.locator("//*[@id='wrapper']/div/div/div[4]/button")
      
        # Enter the user_name
        self.user_name= page.locator("//*[@id='user-name']")
       
        # Save the user name
        self.save_user = page.locator("//button[@type='submit']")


        # Click the signup/signin menu button
    def signup_click(self):
       self.signup_button.click()
        
        # Enter the phone number
    def fill_phone_number(self, phonenumber : str):
        self.phone_number.fill(phonenumber)

        # Click the proceed to button
    def click_proceed_button(self):
        self.proceed_button.click()
       

        # Enter the sample OTP
    def enter_otp_values(self):
        otp_values =["1","2","3","4","5","6"]
        for i, value in enumerate(otp_values,start=1):
         self.page.locator(f"//*[@id='wrapper']/div[1]/div[1]/div[3]/input[{i}]").type(value)
      
        # Enter the user_name
        
    def fill_user_name(self, username : str):
        self.user_name.fill(username)

        # Save the user name
    def save_user_name(self):
       self.save_user.click()
        

        

