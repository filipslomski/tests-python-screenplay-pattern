from selenium import webdriver


class Browser(object):
    
    base_url = 'http://'
    driver = webdriver.Chrome('./chromedriver')
    driver.implicitly_wait(10)
    
    def close(self):
        self.driver.quit()

    def visit(self, location=''):
        url = self.base_url + location
        self.driver.get(url)

    def find_by_id(self, selector):
        return self.driver.find_element_by_id(selector)

    def find_by_xpath(self, selector):
        return self.driver.find_element_by_xpath(selector)