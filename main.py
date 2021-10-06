# Importing the required modules. Please pip install if not installed in your environment
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

with open("config.json") as file:
    data=json.load(file)

# Extracting Credentials and necessary details from the .JSON file. 
# Please Configure the .JSON file as per your requirements.
EmailID=data["Config"][0]["User_Email"]
pswd=data["Config"][0]["Password"]
Rcpt=data["Config"][1]["Recipient"]
MailSub=data["Config"][1]["Subject"]
MailBody=data["Config"][1]["Body"]
PATH=data["Config"][2]["DriverPath"]

# Intializing Google Chrome as our Web driver.
driver=webdriver.Chrome(PATH)

# Opening the Gmail login Page
driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

# Finding the username dialog box on the webpage & Entering the username
username=driver.find_element_by_id("identifierId")
username.send_keys(EmailID)
username.send_keys(Keys.RETURN)

# Finding the Password dialog box on the webpage & Entering the Password
try:
    password= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']")))
    password.send_keys(pswd)
    password.send_keys(Keys.RETURN)
except:
    driver.quit()

# Finding the Compose button and clicking it on the Gmail webpage
try:
    compose= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[text()='Compose']")))
    compose.click()
except:
    driver.quit()

# Filling in the Recipients, Email Subject and Mail Body and Sending.
try:
    to= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//textarea[@name='to']")))
    to.send_keys(Rcpt)
except:
    driver.quit()

time.sleep(2)
sub=driver.find_element_by_xpath("//input[@name='subjectbox']")
sub.send_keys(MailSub)

time.sleep(2)
body=driver.find_element_by_xpath("//div[@id=':qi']")
body.send_keys(MailBody)

time.sleep(2)
SEND=driver.find_element_by_xpath('//div[@id=":p3"]')
SEND.click()

# Waits for 10 seconds after Sending and we quit from the driver.
time.sleep(10)
driver.quit()

