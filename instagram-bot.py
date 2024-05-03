
#username = "_nerd_n_gga"
#password = "welcome7867"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def post_on_instagram(message, image_path):
    username, password = "_nerd_n_gga", "welcome7867"

    option = Options()
    option.add_argument("start-maximized")

    try:
        driver = webdriver.Chrome(options=option)
        driver.get("https://www.instagram.com/")

        wait = WebDriverWait(driver, 20)

        # For login
        username_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        username_field.send_keys(username)

        password_field = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
        password_field.send_keys(password)

        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_button.click()

         # Handle "Save Info" popup
        try:
            not_now_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Not now')]")))
            not_now_button.click()
        except:
            pass

        # Handle "Turn On Notifications" popup
        try:
            not_now_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']")))
            not_now_button.click()
        except:
            pass

       # For posting
        create_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']//svg[@aria-label='New post']")))
        create_button.click()





        # Wait for the file upload input to be present
        file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))

        # Upload the image
        file_input.send_keys(image_path)

        # Wait for the next button to be clickable
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Next')]")))
        next_button.click()

        # Wait for the textarea for caption to be present
        caption_input = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@aria-label='Write a caption…']")))

        # Add caption
        caption_input.send_keys(message)

        # Click on the share button
        share_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Share')]")))
        share_button.click()

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

# Example usage
post_on_instagram("This is a test post!", "/path/to/your/image.jpg")
