import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time
import pathlib


def refresh_cookies(email, pw):
    url = f'https://kktix.com'
    options = uc.ChromeOptions()
    options.add_argument("--headless=new")
    driver = uc.Chrome(options=options)
    driver.get(url)
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li[class='not-signed-in']")))[1].click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='user_login']"))).send_keys(email)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='user_password']"))).send_keys(pw)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class='btn btn normal btn-login']"))).click()
    time.sleep(2)
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    driver.quit()
def remove_twd_comma(s):
    return int(s.replace("TWD$", "").replace(",", ""))


choose_by_ticket_price = True
choose_by_ticket_name = not choose_by_ticket_price
price_range = [3880, 6380, 3380, 800]
name_keyword = ["黃2D", "黃3I"]
ticket_quantity = 2
cutoff_price = 5000
cutoff_ticket_quantity = 1
with open("./cred.txt", "r") as f:
    card_no, month, year, val_code, id_no, email, name, mobile, pw = f.read().split("\n")
# refresh_cookies(email, pw)

events = {
    "10/4": "a8249618-00a1c",
    "10/5": "a8249618-01afw",
    "10/6": "a8249618-02bew",
}
event_id = events["10/4"]
url = f'https://kktix.com/events/{event_id}/registrations/new'
options = uc.ChromeOptions()
options.add_argument(f"--load-extension={pathlib.Path().absolute()}/CapSolver/")
driver = uc.Chrome(options=options)
driver.set_window_position(2000, 0)
driver.maximize_window()
driver.get(url)
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()


found_type = False
while(True):
    if(found_type):
        try:
            driver.switch_to.alert.accept()
            found_type = False
        except: continue
    try:
        ticket_type_collection = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class='ticket-unit ng-scope']")))
        if(choose_by_ticket_price):
            for price in price_range:
                print(f"Currently finding ${price} tickets: ", end='')
                for ticket_type in ticket_type_collection:
                    type_price = remove_twd_comma(ticket_type.find_element(By.CSS_SELECTOR, "[class='ng-binding ng-scope']").text)
                    if(type_price == price):
                        try:
                            print(ticket_type.find_element(By.CSS_SELECTOR, "[class='ticket-quantity ng-binding ng-scope']").text)
                            continue
                        except:
                            plus_button = ticket_type.find_element(By.CSS_SELECTOR, "button[class='btn-default plus']")
                            real_quantity = ticket_quantity if price < cutoff_price else cutoff_ticket_quantity
                            for i in range(real_quantity):
                                plus_button.click()

                            # effective_quantity = int(ticket_type.find_element(By.CSS_SELECTOR, "input[type='text']").get_attribute('value'))
                            # if(effective_quantity < real_quantity):
                            #     print("Not enough tickets, refreshing...")
                            #     driver.refresh()
                            #     continue
                            
                            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='person_agree_terms']"))).click()
                            WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[class*='btn btn-primary']")))[-1].click()
                            found_type = True
                            print(f"Found tickets available")
                            break
                if(found_type): break
            if(not found_type):
                print("Did not find any ticket type available, refreshing...")
                driver.refresh()
        elif(choose_by_ticket_name):
            for kw in name_keyword:
                print(f"Currently finding {kw} tickets: ", end='')
                for ticket_type in ticket_type_collection:
                    type_name = ticket_type.find_element(By.CLASS_NAME, "ticket-name").text
                    if(kw in type_name):
                        try:
                            print(ticket_type.find_element(By.CSS_SELECTOR, "[class='ticket-quantity ng-binding ng-scope']").text)
                            continue
                        except:
                            plus_button = ticket_type.find_element(By.CSS_SELECTOR, "button[class='btn-default plus']")
                            for i in range(ticket_quantity):
                                plus_button.click()
                            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='person_agree_terms']"))).click()
                            WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[class*='btn btn-primary']")))[-1].click()
                            found_type = True
                            print(f"Found tickets available")
                            break
                if(found_type): break
            if(not found_type):
                print("Did not find any ticket type available, refreshing...")
                driver.refresh()
    except Exception as e:
        print("Error occured: ", e)
        print("Tickets unavailable, refreshing...")
        driver.refresh()




