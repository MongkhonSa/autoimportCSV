from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time 
log_row = open('log_row.txt', 'r') 
# log_row.read() 
log_col = open('log_col.txt', 'r') 
# log_col.read() 
i=int(log_col.read())
j=int(log_row.read())
print(i,j)
chromedriver = "chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("https://data.go.th/Datasets.aspx")
for tmp in range(i):
    try:
        WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#ctl00_MainContent_imbtnNextPage")))
        driver.find_element_by_css_selector("#ctl00_MainContent_imbtnNextPage").click() #redirect to n page
        time.sleep(0.5)
    except NoSuchElementException:
        driver.quit()
    # print(tmp)
for col in range(i,60,1):
    write_col = open('log_col.txt', 'w') 
    write_col.write(str(col)) 
    write_col.close()
    time.sleep(2)

    for row in range(j,22,1):
        try:
            main_window = driver.current_window_handle
            actions = ActionChains(driver)
            time.sleep(1)
            newtab =driver.find_element_by_xpath('//*[@id="ctl00_MainContent_grdDataset"]/tbody/tr['+str(row)+']/td/li/div[2]/h2/a') #visit content
            actions.key_down(Keys.CONTROL).click(newtab).key_up(Keys.CONTROL).perform()
            driver.switch_to.window(driver.window_handles[-1])
        except NoSuchElementException:
            driver.quit()

        file_element_list = driver.find_elements_by_xpath("//img[@src='Public/Images/File-Extension/csv-64.png' or @src='Public/Images/File-Extension/xls-64.png' or @src='Public/Images/File-Extension/xlsx-64.png']") #find CSV
        file_list = [tmp for tmp in file_element_list]

        if(file_list):
            for index in range(0,len(file_list)):
                WebDriverWait(driver, 200).until(EC.visibility_of_element_located((By.XPATH, "//img[@src='Public/Images/File-Extension/csv-64.png' or @src='Public/Images/File-Extension/xls-64.png' or @src='Public/Images/File-Extension/xlsx-64.png']"))) #CSV select to dowload
                file_select = driver.find_elements_by_xpath("//img[@src='Public/Images/File-Extension/csv-64.png' or @src='Public/Images/File-Extension/xls-64.png' or @src='Public/Images/File-Extension/xlsx-64.png']")[index]
                file_select.click()
                
                print("found")
                WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#ctl00_MainContent_btnDownloadResource")))
                download_buttom = driver.find_element_by_css_selector("#ctl00_MainContent_btnDownloadResource") #download csv
                download_buttom.click()
                time.sleep(3)
                try:
                    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#ctl00_MainContent_btnBacktoResourceList")))
                    back_buttom =driver.find_element_by_css_selector("#ctl00_MainContent_btnBacktoResourceList") #back to file select
                    back_buttom.click()
                    time.sleep(2)
                except TimeoutException:
                    driver.close()
                    # main_window = driver.current_window_handle
                    driver.switch_to_window(main_window)
                    time.sleep(1)
                    newtab =driver.find_element_by_xpath('//*[@id="ctl00_MainContent_grdDataset"]/tbody/tr['+str(row)+']/td/li/div[2]/h2/a') #visit content
                    actions.key_down(Keys.CONTROL).click(newtab).key_up(Keys.CONTROL).perform()
                    driver.switch_to.window(driver.window_handles[-1])
                    # content=driver.find_element_by_xpath('//*[@id="ctl00_MainContent_grdDataset"]/tbody/tr['+str(row)+']/td/li/div[2]/h2/a').click() #visit content
                    # time.sleep(2)
        write_row = open('log_row.txt', 'w') 
        write_row.write(str(row)) 
        write_row.close()
        driver.close()
        driver.switch_to_window(main_window)
    write_row = open('log_row.txt', 'w') 
    write_row.write(str(2)) 
    write_row.close()
    j=2
    
    driver.find_element_by_css_selector("#ctl00_MainContent_imbtnNextPage").click() #redirect to n page
