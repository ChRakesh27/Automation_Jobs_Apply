from bs4 import BeautifulSoup
import requests

def appying_Jobs_linkedIn(Headers):
    request= requests.get("https://www.linkedin.com/jobs/search/", headers=Headers)
    soup = BeautifulSoup(request.text, 'html.parser')
    jobs = soup.find_all("li", {'class' : 'jobs-search-results__list-item'})
    print("🚀 ~ jobs:", jobs)

    return


def main():
    Headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        'Cookie':'li_at-AQEDAURp1WUEl0WfAAABj_Zw9wUAAAGSZXxZbU0AA8uWZybpgYeIMVCfM9VG5Ok0TRy2y_hsX2DHhkBItx133-fETnU_N0D7sIRJoVvXnXVcwqf61bfrXSKgYsrWUp0FNXc396xFtjmdSD_T38owkqB9'}
    
    appying_Jobs_linkedIn(Headers)

if __name__ == "__main__":
    main()
