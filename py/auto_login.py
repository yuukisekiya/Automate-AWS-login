from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# https://googlechromelabs.github.io/chrome-for-testing/

CHROME_DRIVER = "C:\\Users\\XXXXXXXX\\python\\drive\\chromedriver.exe"

# アカウント指定を動的に行えるようにUpdate予定

OPEN_AWS_URL = "https://console.aws.amazon.com"
AWS_ACCOUNT_ID = "XXXXXXXXXXXX"
AWS_IAM_ID = "XXXXXXXXXXXXXXXX"
AWS_IAM_PASSS = "XXXXXXXXX"

# ChromeDriverのサービスを設定
service = Service(CHROME_DRIVER)
chrome_options = Options()

# ドライバーを初期化
driver = webdriver.Chrome(service=service, options=chrome_options)

print("OPEN: " + OPEN_AWS_URL)
driver.get(OPEN_AWS_URL)

# ページが完全に読み込まれるまで待機（最大10秒）
wait = WebDriverWait(driver, 10)

# 要素が表示されるまで待機
input_signin_button = wait.until(EC.element_to_be_clickable((By.ID, "input_signin_button")))

print("ACCOUNT ID 入力")
input_account = wait.until(EC.presence_of_element_located((By.ID, "account")))
input_account.send_keys(AWS_ACCOUNT_ID)

print("USER NAME 入力")
username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
username_input.send_keys(AWS_IAM_ID)

print("PASSWORD 入力")
password_input = driver.find_element(By.ID, "password")
password_input.send_keys(AWS_IAM_PASSS)

signin_button = driver.find_element(By.ID, "signin_button")
signin_button.click()

# MFAの自動入力実装予定

# 手動で停止するための入力待機
input("Press Enter to close the browser and exit...")

# ブラウザを閉じる
driver.quit()
