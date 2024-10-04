import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def add_cookies(driver, cookies):
    for cookie in cookies:
        driver.add_cookie(cookie)
        

mySkills=["javascript","node","react","angular","front end",'css','html','web development','python']

onsiteCompanies=['ibm', 'e2open', 'accenture', 'rapyd', 'snow planet', 'factset', 'avalara', 'deltacubes technologies', 'tibarumal gems jewels', 'insightsoftware', 'freshprints', 'planful', 'experian', 'reuters news agency', 'sutherland global services inc', 'siddhartha degree college', 'sanofi', 'ss&c technologies', 'dazn', 'webflow', 'mwb technologies', 'unfold solution', 'hexawiz', 'sprious']

def apply_naukri_jobs(driver,pageNo):
    print("🚀 ~ onsiteCompanies:", onsiteCompanies)
    if pageNo==10:
        return
    
    experence="3"
    citytype="17"
    # 17
    lastDate="2"
    remote=False
        
    url='https://www.naukri.com/javascript-jobs-'+str(pageNo)+'?k=javascript&nignbevent_src=jobsearchDeskGNB'
    if experence!="0":
        url +="&experience="+experence
    if citytype !="0":
        url +="&cityTypeGid="+citytype
    if lastDate:
        url +="&jobAge="+lastDate
    if remote:
        url +="&wfhType=2"

    print("🚀 ~ url:", url)
    driver.get(url)
    time.sleep(2)
    
    try:
        # filter = driver.find_element(By.ID, 'filter-sort')
        # pageNext=driver.find_elements(By.CLASS_NAME,'styles_btn-secondary__2AsIP')
        # print("🚀 ~ pageNext:", pageNext)
        # filter.click()
        # filterDate = driver.find_elements(By.CLASS_NAME, 'styles_ss__menu-item__T4rgB')[7]
        # filterDate.click()
        # time.sleep(3)

        jobs = driver.find_elements(By.CLASS_NAME,'srp-jobtuple-wrapper')
       
        jobs_Links=[]
        for job in jobs:
            companyName=job.find_element(By.CLASS_NAME,"comp-name").text.lower()
            if companyName in onsiteCompanies:
                continue
            requiredSkills = job.find_element(By.CLASS_NAME,'tags-gt').text.lower()
            skip=True
            for skill in mySkills:
                if skill in requiredSkills:
                    print("skill",skill)
                    skip=False
                    break
            if skip:
                continue
            row1_element= job.find_element(By.CLASS_NAME,"row1")
            anchor_tag = row1_element.find_element(By.TAG_NAME, 'a')
            job_href = anchor_tag.get_attribute('href')
            jobs_Links.append(job_href)
            # break
            
        for link in jobs_Links:
            driver.get(link)
            time.sleep(2)
            apply_button = driver.find_elements(By.ID,'apply-button')
            companyElement = driver.find_element(By.CLASS_NAME,'styles_jd-header-comp-name__MvqAI')
            companyName = companyElement.find_element(By.TAG_NAME, 'a').text.lower()
            if companyName in onsiteCompanies:
                continue
            
            if(len(apply_button)):
                # apply_button[0].click()
                print("apply",link)
                input("enter any to continue:")
                # time.sleep(30)
            else:
                onsiteCompanies.append(companyName)
        apply_naukri_jobs(driver,pageNo+1)
        
    except Exception as e:
        print(f"Error applying to job: {e}")

    return


def main():
    driver = webdriver.Chrome()
    
    naukri_cookies = []

    driver.get('https://www.naukri.com/mnjuser/homepage')
    time.sleep(2)
    add_cookies(driver, naukri_cookies)
    driver.refresh()
    apply_naukri_jobs(driver,1)
    time.sleep(10)

    driver.quit()

if __name__ == "__main__":
    main()
