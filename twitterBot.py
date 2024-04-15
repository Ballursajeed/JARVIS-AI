from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def account_info():
    with open('account_info.txt','r') as f:
        info = f.read().split()
        username = info[0]
        password = info[1]
    return username, password
def tweet(message):

   username = "SBallur59446"
   password = "Welcome7867"

   option = Options()
   option.add_argument("start-maximized")

   try:
       driver = webdriver.Chrome(options=option)
       driver.get("https://twitter.com/login")
       wait = WebDriverWait(driver, 10)

#for login
       username_field = wait.until(
       EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete=username]'))
       )
       username_field.send_keys(username)

       login_button = wait.until(
       EC.presence_of_element_located((By.CSS_SELECTOR, '[role=button].r-13qz1uu'))
       )
       login_button.click()

       password_field = wait.until(
       EC.presence_of_element_located((By.CSS_SELECTOR, '[type=password]'))
       )
       password_field.send_keys(password)

       login_button = wait.until(
       EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid*=Login_Button]'))
       )
       login_button.click()

 #for tweeting 
       tweet_button = wait.until(
             EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid=tweetButtonInline]'))
        )
       tweet_button.click()

       tweet_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid=tweetTextarea_0]'))
        )
       tweet_input.send_keys(message)

       tweet_button = wait.until(
       EC.element_to_be_clickable((By.XPATH, '//span[text()="Post"]'))
       )
       tweet_button.click()

    # Wait for a few seconds to observe the result
       time.sleep(5)
     
    # Add an input function to wait for user input before closing the browser
       input("Press Enter to close the browser window...")

       driver.quit()  # Close the browser window after user input

   except Exception as e:
       import traceback
       print("An error occurred:", e)
       traceback.print_exc()
       # Close the browser window if it's open
       if 'driver' in locals():
           driver.quit()

