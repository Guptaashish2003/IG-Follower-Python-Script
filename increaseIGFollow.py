from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from faker import Faker 
# Set up the driver (Make sure to replace 'path/to/your/chromedriver' with the actual path)

# Navigate to the URL containing the form
name = input("Enter the username for  the form: ")
for i in range(1, 100):
    try:
        driver = webdriver.Firefox()
        driver.get('https://smmpanel.com/signup')
        # Wait until the form is present
        form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'signup-frm'))
        )

        # Fill in the form fields
        driver.find_element(By.ID, 'login').send_keys(f'youbd{name}v{i}')
        driver.find_element(By.ID, 'email').send_keys(f'y{name}{i}il@kaku.com')
        driver.find_element(By.ID, 'first_name').send_keys('YourFirstNrame')
        driver.find_element(By.ID, 'last_name').send_keys('YourLastNamer')
        driver.find_element(By.ID, 'whatsapp').send_keys('1234567890')
        driver.find_element(By.ID, 'skype').send_keys('your_skype')
        driver.find_element(By.ID, 'telegram').send_keys('your_telegram')
        driver.find_element(By.ID, 'password').send_keys('your_password')
        driver.find_element(By.ID, 'password_again').send_keys('your_password')

        # Check the Terms of Service checkbox
        terms_checkbox = driver.find_element(By.NAME, 'RegistrationForm[termsofservice]')
        if not terms_checkbox.is_selected():
            terms_checkbox.click()

        # time.sleep(30)
        isCaptcha = True
        while isCaptcha:
            recaptcha_response = driver.find_element(By.ID, "g-recaptcha-response")
            print("please verify captcha",recaptcha_response.get_attribute("value"))
            if(recaptcha_response.get_attribute("value")):
                isCaptcha = False
                break

        # # Submit the form
        time.sleep(2)
        print("submitting form........")
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        time.sleep(4)
        dropdown = Select(driver.find_element(By.ID, "orderform-category"))

        # Select an option by its value
        dropdown.select_by_value("20379")
        driver.find_element(By.ID, 'field-orderform-fields-link').send_keys('https://www.instagram.com/itzsanjayraj.7224')
        driver.find_element(By.ID, 'field-orderform-fields-quantity').send_keys(49)
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        # # Optionally, wait for some response or element after submission
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, 'some-class-after-submit'))
        # )

    finally:
    # Close the driver
        driver.quit()
        print("Form submitted successfully")