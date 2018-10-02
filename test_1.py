from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
chromedriver = "C:/Users/ITokkyZ/Desktop/autoimport/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
count =1
driver.get("https://data.go.th/Datasets.aspx")
list1 = []
for col in range(0,60,1):
    driver.get("https://data.go.th/Datasets.aspx") #main page
    time.sleep(1)
    page=driver.find_element_by_css_selector("#ctl00_MainContent_rptPaging_ctl"+str(col).zfill(2)+"_lbtnPageIndex").click() #redirect to n page
    time.sleep(2)
    # print(col)
    # list1.click()


    for row in range(2,22,1):
        
        driver.get("https://data.go.th/Datasets.aspx")
        time.sleep(1)
        page=driver.find_element_by_css_selector("#ctl00_MainContent_rptPaging_ctl"+str(col).zfill(2)+"_lbtnPageIndex").click() #back to current page
        time.sleep(2)
        content=driver.find_element_by_xpath('//*[@id="ctl00_MainContent_grdDataset"]/tbody/tr['+str(row)+']/td/li/div[2]/h2/a').click() #visit content
        time.sleep(2)

        file_element_list = driver.find_elements_by_xpath("//img[@src='Public/Images/File-Extension/csv-64.png' or @src='Public/Images/File-Extension/xls-64.png' or @src='Public/Images/File-Extension/xlsx-64.png']") #find CSV
        file_list = [tmp for tmp in file_element_list]
        # print(file_list)
        if(file_list):
            # for file_select in file_list:
            for index in range(0,len(file_list)):
                WebDriverWait(driver, 200).until(EC.visibility_of_element_located((By.XPATH, "//img[@src='Public/Images/File-Extension/csv-64.png' or @src='Public/Images/File-Extension/xls-64.png' or @src='Public/Images/File-Extension/xlsx-64.png']"))) #CSV select to dowload
                file_select = driver.find_elements_by_xpath("//img[@src='Public/Images/File-Extension/csv-64.png' or @src='Public/Images/File-Extension/xls-64.png' or @src='Public/Images/File-Extension/xlsx-64.png']")[index]
                file_select.click()
                
                print("found")
                WebDriverWait(driver, 200).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#ctl00_MainContent_btnDownloadResource")))
                download_buttom = driver.find_element_by_css_selector("#ctl00_MainContent_btnDownloadResource") #download csv
                download_buttom.click()
                time.sleep(3)

                WebDriverWait(driver, 200).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#ctl00_MainContent_btnBacktoResourceList")))
                back_buttom =driver.find_element_by_css_selector("#ctl00_MainContent_btnBacktoResourceList") #back to file select
                back_buttom.click()

                print("count:",count)
                count +=1


