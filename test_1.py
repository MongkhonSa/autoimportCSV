from selenium import webdriver
import time 
chromedriver = "C:/Users/ITokkyZ/Desktop/autoimport/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
count =1
driver.get("https://data.go.th/Datasets.aspx")
list1 = []
for col in range(0,60,1):
    driver.get("https://data.go.th/Datasets.aspx")
    page=driver.find_element_by_css_selector("#ctl00_MainContent_rptPaging_ctl"+str(col).zfill(2)+"_lbtnPageIndex").click()
    time.sleep(1)
    # print(col)
    # list1.click()


    for row in range(2,22,1):
        print("count:",count)
        count +=1
        driver.get("https://data.go.th/Datasets.aspx")
        time.sleep(1)
        list1=driver.find_element_by_css_selector("#ctl00_MainContent_rptPaging_ctl"+str(col).zfill(2)+"_lbtnPageIndex").click()
        time.sleep(1)
        content=driver.find_elements_by_xpath('//*[@id="ctl00_MainContent_grdDataset"]/tbody/tr['+str(row)+']/td/li/div[2]/h2/a')[0].click()
    # driver.get("https://data.go.th/Datasets.aspx")

