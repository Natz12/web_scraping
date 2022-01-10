import time
import numpy as np
import pandas as pd
from datetime import date

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class CocorahsScrap():
    def __init__(self):
        self.driver = None
        self.reports = None
        self.stations_list = None 
        self.stations_info = None
                 
    def setUp(self, url = "https://www.cocorahs.org/ViewData/ListHailReports.aspx"):
        # driver = webdriver.Firefox()
        driver = webdriver.Chrome("/Users/natalia/Documents/WebDriver/chromedriver")# Optional argument, if not specified will search path.
        driver.get(url)
        self.driver = driver
        # time.sleep(3) # Let the user actually see something!
        
    @staticmethod
    def clear_element(elem, count = 10):
        i = 0
        while i < 10:
            elem.send_keys(Keys.BACK_SPACE)
            i += 1      
    
    def get_hail_reports(self, date_ini, date_end, country = "C"):
        
        def get_column_names(grid):    
            grid_header = grid.find_element_by_xpath("//tr[@class='GridHeader']")
            grid_header = grid_header.find_elements_by_xpath('td')
            columns = [column.text for column in grid_header]
            return columns

        def get_rows(grid):
            rows = np.array([])
            for grid_item in ['GridItem', 'GridAltItem']:
                # grid_header = grid.find_element_by_xpath(f"//tr[@class='GridHeader']")
                grid_header = grid.find_elements_by_xpath(f"//tr[@class='{grid_item}']")
                elems = [column.text.strip() for elem in grid_header for column in elem.find_elements_by_xpath('td')]
                elems = np.array(elems)
                # elems = elems.reshape(int(elems.size/10),10)
                rows = np.append(rows,elems)
            # rows = np.array(rows)
            # rows = rows.reshape(int(rows.size/10),10)
            return rows  
        
        self.setUp()
        driver = self.driver
        driver.get("https://www.cocorahs.org/ViewData/ListHailReports.aspx")
        # time.sleep(1) # Let the user actually see something!
        assert "CoCoRaHS" in driver.title
        elem = driver.find_element_by_id("frmHailObsSearch_ucStateCountyFilter_ddlCountry")
        elem.send_keys(country)
        elem = driver.find_element_by_id("frmHailObsSearch_ucDateRangeFilter_dcStartDate_t")
        # time.sleep(1) # Let the user actually see something! #TODO https://selenium-python.readthedocs.io/waits.html
        self.clear_element(elem)
        elem.send_keys(date_ini)
        
        elem = driver.find_element_by_id("frmHailObsSearch_ucDateRangeFilter_dcEndDate_t")
        time.sleep(1) #TODO https://selenium-python.readthedocs.io/waits.html
        self.clear_element(elem)
        elem.send_keys(date_end)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(1) 

        grid = driver.find_element_by_xpath("//table[@class='Grid']")
        columns = get_column_names(grid)

        select_values = []

        drop_down = driver.find_element_by_id("ucReportList_wcDropDownListPager")
        all_options = drop_down.find_elements_by_tag_name("option")

        for option in all_options:
            print("Value is: %s" % option.get_attribute("value")) #Error. solution: get values and then reference them by value
            select_values.append(option.get_attribute("value"))
            # drop_down = driver.find_element_by_id("ucReportList_ReportGrid")
            # option.click()

        hail_events = np.array([])
        for value in select_values:
            s1= Select(driver.find_element_by_id('ucReportList_wcDropDownListPager'))
            # s1.select_by_index(2) 
            s1.select_by_value(value)   
            time.sleep(1)
            grid = driver.find_element_by_xpath("//table[@class='Grid']")
            rows = get_rows(grid)
            hail_events = np.append(hail_events, rows)
        hail_events = np.array(hail_events)
        hail_events = hail_events.reshape(int(hail_events.size/10),10)
        hail_df = pd.DataFrame(hail_events, columns = columns)
        
        self.reports = hail_df
        self.stations_list = np.unique(hail_df['Station Number'])

    def get_stations(self):
        print(1)

date_ini = "01/01/2012"
today = date.today()
date_end = today.strftime("%d/%m/%Y")


datascrap = CocorahsScrap()
datascrap.get_hail_reports(date_ini, date_end)


driver = datascrap.driver
driver.get("https://www.cocorahs.org/Stations/ListStations.aspx")
time.sleep(1) # Let the user actually see something!
assert "CoCoRaHS" in driver.title
# elem = driver.find_element_by_name("q")
elem = driver.find_element_by_id("frmStationSearch_ucStateCountyFilter_ddlCountry")
# elem.clear()
elem.send_keys("C")

# s1= Select(driver.find_element_by_id('frmStationSearch_ucStateCountyFilter_ddlCounty'))

# s1.select_by_value(value) 

elem = driver.find_element_by_id("frmStationSearch_ucStationTextFieldsFilter_tbTextFieldValue")
elem.send_keys("CAN-ON-202")

elem = driver.find_element_by_id("frmStationSearch_ucStationTextFieldsFilter_cblTextFieldsToSearch_0")
elem.click()
elem = driver.find_element_by_id("frmStationSearch_btnSearch")
elem.click()
driver.find_element_by_xpath("//table[@class='Grid']//a[contains(@title,'View')]").click()
time.sleep(1) # Let the user actually see something! #TODO https://selenium-python.readthedocs.io/waits.html


with open("elem_text.txt", "w") as text_file:
    print(f"{hail_events}", file=text_file)
    

 
s1.select_by_index(2)





print('end')
# while True:
#     try:
#         elem = driver.find_element_by_id("ucReportList_wcNextPager")
#     except selenium.common.exceptions.NoSuchElementException:
#         break
    # else:

elem = driver.find_element_by_id("ucReportList_wcDropDownListPager")

# grid = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[@id='tdMainBody']/table[@id='Table1']/tbody/tr[2]/td/table")
# grid = driver.find_element_by_xpath("//table[@id='Table1']/tbody/tr[2]/td/table")

rows = elem.text

with open("elem_text.txt", "w") as text_file:
    print(f"{hail_events}", file=text_file)

assert "No results found." not in driver.page_source
driver.close()