import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# ✅ Chrome Options Configure karo

options = uc.ChromeOptions()
options.add_argument("--remote-debugging-port=2007")
options.add_argument("--user-data-dir=D:/youtube_scraper/chrome_session")


# ✅ Preferences set karo
prefs = {
    "profile.default_content_setting_values.notifications": 1,  # Allows notifications
    "profile.default_content_setting_values.geolocation": 1,  # Disables geolocation
}
options.add_experimental_option("prefs", prefs)

# ✅ Chrome Driver Create karo
driver = uc.Chrome(options=options)

# ✅ YouTube Open karo
driver.get("https://www.youtube.com")
time.sleep(3)

# ✅ Search Bar Locate karo
search_box = driver.find_element(By.NAME, "search_query")

# ✅ "computer" likho aur Enter press karo
search_box.send_keys("computer")
search_box.send_keys(Keys.RETURN)
time.sleep(2)

# ✅ Pehli video locate karo aur click karo
first_video = driver.find_element(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')
video_title = first_video.text  # ✅ Video ka naam save karo
first_video.click()
time.sleep(5)  # Video load hone ka wait karo

# ✅ Views extract karna (Updated XPath)
try:
    like = driver.find_element(By.XPATH, '//*[@id="like-button"]/yt-button-shape/label/div/span').text  # ✅ Views locate karo
except:
    like = "Views not found"

# ✅ Output print karo
print(f"✅ Video Title: {video_title}")
print(f"✅ Video Views: {like}")

# ✅ Close Chrome
time.sleep(10)  # Video play hone do
driver.quit()

