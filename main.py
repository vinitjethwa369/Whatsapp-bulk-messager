# Packages
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # Importing WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # Importing expected_conditions
import time

# Config
login_time = 30                  # Time for login (in seconds)
new_msg_time = 5                 # Time for a new message (in seconds)
send_msg_time = 5                # Time for sending a message (in seconds)
country_code = 91                # Set your country code
action_time = 2                  # Set time for button click action
image_path = "C:/Users/HP/Downloads/WhatsApp Image 2024-09-22 at 10.59.15 PM.jpeg"  # Absolute path to your image

# Create driver without service argument
driver = webdriver.Chrome(ChromeDriverManager().install())

# Encode Message Text
with open('whatsapp-bulk-messenger-main/message.txt', 'r') as file:
    msg = file.read()

# Open browser with default link
link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(login_time)

# Loop Through Numbers List
with open('whatsapp-bulk-messenger-main/numbers.txt', 'r') as file:
    for n in file.readlines():
        num = n.rstrip()
        link = f'https://web.whatsapp.com/send/?phone={country_code}{num}'
        driver.get(link)
        time.sleep(new_msg_time)

        # Click on button to load the input DOM using explicit wait
        if image_path:
            try:
                # Use the CSS selector based on the provided HTML
                attach_btn = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[data-icon="plus"]'))  # Updated selector
                )
                attach_btn.click()
                time.sleep(action_time)

                # Find and send image path to input
                msg_input = driver.find_elements(By.CSS_SELECTOR, 'input[type="file"]')[1]  # Adjusted for input type
                msg_input.send_keys(image_path)
                time.sleep(action_time)

            except TimeoutException:
                print("Timed out waiting for the attachment button to become clickable.")
                driver.save_screenshot("timeout_error.png")  # Save a screenshot for debugging

        # Start the action chain to write the message
        actions = ActionChains(driver)
        for line in msg.split('\n'):
            actions.send_keys(line)
            # SHIFT + ENTER to create next line
            actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(send_msg_time)

# Quit the driver
driver.quit()
