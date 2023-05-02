from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


 class TestClaimAmount(unittest.TestCase):

    def setUp(self):
        
        driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("C://xampp//htdocs//testE//index.html")

    def tearDown(self):
        
        self.driver.quit()

    def test_case1(self):
        
        self.driver.find_element_by_id("f0").send_keys("15000")
        self.driver.find_element_by_id("f1").send_keys("12000")
        self.driver.find_element_by_xpath(‘/html/body/form/p[2]/input’).click()

       
        claim_amount = self.driver.find_element_by_id("s").text
        self.assertEqual(claim_amount, 27000, "Test Case#1 - Wrong")




    def test_case2(self):
      
        self.driver.find_element_by_id("f0").send_keys("50000")
        self.driver.find_element_by_id("f1").send_keys("25000")
        self.driver.find_element_by_xpath(‘/html/body/form/p[2]/input’).click()

        
        claim_amount = self.driver.find_element_by_id("s").text
        self.assertEqual(claim_amount, 75000,"Test Case#2 - Wrong")

    def test_case3(self):
     
        self.driver.find_element_by_id("f0").send_keys("50000")
        self.driver.find_element_by_id("f1").send_keys("12000")
        self.driver.find_element_by_xpath(‘/html/body/form/p[2]/input’).click()

       
        claim_amount = self.driver.find_element_by_id("s").text
        self.assertEqual(claim_amount, 62000 "Test Case#3 - Wrong")

    def test_case4(self):
       
        self.driver.find_element_by_id("f0").send_keys("15000")
        self.driver.find_element_by_id("f1").send_keys("7000")
       self.driver.find_element_by_xpath(‘/html/body/form/p[2]/input’).click()

        
        claim_amount = self.driver.find_element_by_id("s").text
        self.assertEqual(claim_amount,22000,  "Test Case#4 - Wrong")

    def test_case5(self):
       
        self.driver.find_element_by_id("f0").send_keys("12500")
        self.driver.find_element_by_id("f1").send_keys("11000")
        self.driver.find_element_by_xpath(‘/html/body/form/p[2]/input’).click()


        claim_amount = self.driver.find_element_by_id("s").text
        self.assertEqual(claim_amount,23500, "Test Case#5 - Wrong")