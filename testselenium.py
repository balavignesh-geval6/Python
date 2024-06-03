from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

path = r'C:/Users/g6-te/Downloads/chromedriver-win64/chromedriver.exe'

service = Service(executable_path=path)

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=service)
# Open the webpage
website = "https://www.adamchoi.co.uk/overs/detailed"
driver.get(website)

# Add a delay to allow the page to load
time.sleep(5)  # Wait for 5 seconds

# Find the "All matches" button and click it
all_matches_button = driver.find_element(By.XPATH, "//label[@analytics-event='All matches']")
all_matches_button.click()

dropdown = Select(driver.find_element(By.ID, "country"))

dropdown.select_by_visible_text("Spain")

time.sleep(3)

# Add a delay to allow the page to load the new content
time.sleep(5)  # Wait for 5 seconds

# Find all match rows
matches = driver.find_elements(By.TAG_NAME, "tr")

# Initialize lists to store the data
date = []
home_team = []
score = []
away_team = []

# Loop through matches and extract data
for match in matches:
    try:
        date.append(match.find_element(By.XPATH, "./td[1]").text)
        home_team.append(match.find_element(By.XPATH, "./td[2]").text)
        score.append(match.find_element(By.XPATH, "./td[3]").text)
        away_team.append(match.find_element(By.XPATH, "./td[4]").text)
    except NoSuchElementException:
        print("A row did not contain the expected number of columns and was skipped.")

# Create a DataFrame from the extracted data
df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})

# Save the DataFrame to a CSV file
df.to_csv('football.csv', index=False)

print(df)

