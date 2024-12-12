# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

# Configure download preferences
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": "/Users/kushtartyn/Desktop/development/testing1/PythonTestDemo/test/testdata/gap_report_grocery_focal_superstore_101_2024-10-28_2024-10-28.pdf",  # Change to your download path
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True  # For PDF files
})

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://focal.systems/adaorder') # example

# Trigger download
download_button = driver.find_element_by_id("downloadReport")
download_button.click()

# Wait for download to complete (may require a more robust check)
time.sleep(5)
driver.quit()

download_path = "/PythonTestDemo/test/testdata"  # To be updated
expected_files = ["gap_report_grocery_focal_superstore_101_2024-10-28_2024-10-28.csv",
                  "gap_report_grocery_focal_superstore_101_2024-10-28_2024-10-28.pdf"]

for file_name in expected_files:
    file_path = os.path.join(download_path, file_name)
    assert os.path.isfile(file_path), f"{file_name} not found in download directory"

