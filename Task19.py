# Visit the Url & Get the Title & Content of the Webpage

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Access_Webpage:

    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    
    def acess(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(10)

# Acessing the webpage & enter the Login Credentials

    def login_credential(self,username,password):
        try:
            self.acess()
            self.driver.find_element(by=By.ID, value="user-name").send_keys(username)
            self.driver.find_element(by=By.ID, value="password").send_keys(password)
            sleep(5)
            self.driver.find_element(by=By.ID, value="login-button").click()
        except Exception as Error_found:
            print("Error_found:",Error_found)

# Get the title & current url of the Webpage

    def get_title_url(self):
        try:
            print("Title of the page: ",self.driver.title)
            print("The Current url of the webpage: ",self.driver.current_url)
        except Exception as Error:
            print("Error: ",Error)

# Extract the content of Webpage & save it into text file 
    def extract_save(self):
        try:
            data = self.driver.page_source
            with open("Webpage_task_11.txt",mode ="w") as file:
                file.write(data)
                print("The Page_source data is written on Webpage_task_11.txt file")
        except Exception as Data_error:
            print("Data_error: ",Data_error)
        finally:
            self.driver.quit()
            print("The process is done")


url ="https://www.saucedemo.com/"
a_wp =Access_Webpage(url)
a_wp.login_credential("standard_user","secret_sauce")
a_wp.get_title_url()
a_wp.extract_save()

