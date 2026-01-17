import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

from bs4 import BeautifulSoup

def scrape_website(website):
    print("launching the browser")

    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Website opened successfully")
        html = driver.page_source

        return html
    except Exception as e:
        print(f"Error opening website: {e}")
    finally:
        driver.quit()


def extract_body_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.find('body')
    if body:
        return str(body)
    else:
        return "Body not found"

def clean_body_content(body):
    soup = BeautifulSoup(body, 'html.parser')
    for script in soup(["script", "style"]):
        script.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content


def split_som_content(dom_content,max_length=6000):
    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)]
    