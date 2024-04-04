from selenium import webdriver
from selenium.webdriver.common.by import By

# keep tab open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/events/")

python_events = {}
event_name = driver.find_elements(By.CSS_SELECTOR, value=".most-recent-events a")
# for names in event_name:
#     print(names.text)

event_time = driver.find_elements(By.CSS_SELECTOR, value=".most-recent-events time")
# for time in event_time:
#     print(time.text)

for num in range(len(event_name)):
    python_events[num] = {
        "name": event_name[num].text,
        "date": event_time[num].text,
    }

print(python_events)

driver.quit()
