import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from trainData import UserData
# Function to add cookies
def add_cookies(driver, cookies):
    for cookie in cookies:
        driver.add_cookie(cookie)

# LinkedIn job application process
def apply_linkedin_jobs(driver):
    # Go to LinkedIn jobs page
    driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&origin=JOB_SEARCH_PAGE_JOB_FILTER")
    time.sleep(3)

    # Find job listing and apply (example class name, it may vary)
    jobs = driver.find_elements(By.CLASS_NAME, 'jobs-search-results__list-item')
    try:
        jobs[1].click()
        time.sleep(2)

        apply_button = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
        apply_button.click()
        time.sleep(2)
        submit_button = driver.find_element(By.CLASS_NAME, 'artdeco-button--primary')
        submit_button.click()
        submit_button.click()
        # "pl3 t-14 t-black--light"

        modelInfo = driver.find_element(By.CLASS_NAME, 't-16 t-bold').text
        print("modelInfo",modelInfo)
        # Work experience
        if(modelInfo=="Additional Questions"):
            infoList = UserData.keys()
            print("infoList",infoList)

            input_field  = driver.find_elements(By.CLASS_NAME, 'artdeco-text-input--input')
            input_field.send_keys("")

            dropdowns = driver.find_elements(By.TAG_NAME, 'select')
            for dropdown in dropdowns:
                select = Select(dropdown)
                options = select.options
                select.select_by_visible_text(options[1].text)
            

        time.sleep(5)
        submit_button = driver.find_element(By.CLASS_NAME, 'artdeco-button--primary')
        submit_button.click()
        time.sleep(2)
        submit_button = driver.find_element(By.CLASS_NAME, 'artdeco-button--primary')
        submit_button.click()
        time.sleep(10)
    except Exception as e:
        print(f"Error applying to job: {e}")
    return
    for job in jobs:
       
        try:
            job.click()
            time.sleep(2)

            # Click the Easy Apply button (example class name)
            apply_button = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
            apply_button.click()
            time.sleep(3)

            # Submit application (modify based on the LinkedIn flow)
            submit_button = driver.find_element(By.CLASS_NAME, 'artdeco-button--primary')
            submit_button.click()
            time.sleep(2)
        except Exception as e:
            print(f"Error applying to job: {e}")

def main():
    # Initialize Selenium WebDriver
    driver = webdriver.Chrome()
    
    # LinkedIn Cookies (sample structure)
    linkedin_cookies = [{"name":"","value":""}]

    # Apply for jobs on LinkedIn
    driver.get('https://www.linkedin.com/jobs/search')
    # time.sleep(2)
    add_cookies(driver, linkedin_cookies)
    driver.refresh()
    # time.sleep(5)
    apply_linkedin_jobs(driver)

    # Close browser
    driver.quit()

if __name__ == "__main__":
    main()
