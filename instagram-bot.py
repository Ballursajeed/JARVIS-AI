
#username = "_nerd_n_gga"
#password = "welcome7867"

'''from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By '''
import time

import json
import requests
#Welcome7867    fbpageID=294285857108535  ig_user_id = 17841458305592495

#accesss_token:EAAGkWZBMh3GUBO4dq6VZADIZApnedTxuiCA9NO9J4aHGsIEcrVmdyxxTJCP2cmp9lxUPTn7WqbikiT1E2YsPy1kTXt0wZAd3CcXklboeY6F0VnfB776E2AwX81NEeN4DNuZB3kTZBe3NcM1P0AK4zS2CETsexiJdajgzcmLZCvC3GDE3JmR0jU8ly8DSWkaYkFbFgD6lKpqNOrR1sOJZASLpm4pQOwZDZD
#accessToken: EAAGkWZBMh3GUBO3hNbV3uaKZAubdJd8jQf5dgGsGcpZB7RTkByCmxqlLhXDXEZBwOjjgCN733PJvlqC1ZB3VwNiQV3WgtsVZBdwVrk9Qq6XwO1bIzQ5i70b2ZACY30IISjb3pPV9DiMt6DxVZBmCh6mhf8F42UrPdxYR63Camz3iKY0aHBb1HqsDZCZCAG9sxNzjTf
'''def post_on_instagram(message, image_path):
    username, password = "zipbag_786", "jarvisai"

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
post_on_instagram("This is a test post!", "/path/to/your/image.jpg")'''

def post_image( imge_url):
    access_token = "EAAGkWZBMh3GUBO3hNbV3uaKZAubdJd8jQf5dgGsGcpZB7RTkByCmxqlLhXDXEZBwOjjgCN733PJvlqC1ZB3VwNiQV3WgtsVZBdwVrk9Qq6XwO1bIzQ5i70b2ZACY30IISjb3pPV9DiMt6DxVZBmCh6mhf8F42UrPdxYR63Camz3iKY0aHBb1HqsDZCZCAG9sxNzjTf"
    ig_user_id = "17841458305592495"
    
    post_url = 'https://graph.facebook.com/v20.0/{}/media'.format(ig_user_id)
    payload = {
        'image_url':imge_url,
        'caption':'a test posting',
        'access_token':access_token,
    }
    
    r = requests.post(post_url,data = payload)
    print(r.text)
    print("Media uploaded successfully!")
    
    result = json.loads(r.text)
    if 'id' in result:
        creation_id = result['id']
        second_url='https://graph.facebook.com/v20.0/{}/media_publish'.format(ig_user_id)
        second_payload = {
            'creation_id':creation_id,
            'access_token':access_token,
        }
        r = requests.post(second_url,data=second_payload)
        print(r.text)
        print("image publish to intagram")
    else:
        print("image posting is not possible!")
    
imge_url = "https://pbs.twimg.com/media/GKF1pPiXcAE_KOc?format=jpg&name=small"   
post_image(imge_url)
time.sleep(20)
