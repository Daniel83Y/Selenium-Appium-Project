from appium import webdriver as mobile
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Keys
from Tests.globals import capabilities_Pixel7, APP_GOOGLE_Maps,appium_server_url_local
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction


class MapAppPage:
    def __init__(self,driver):
        """Initialize the MapAppPage on Pixel7 with a WebDriver instance."""
        # Merge APP_Caller into capabilities_Pixel7 if APP_Caller contains additional capabilities
        capabilities = {**capabilities_Pixel7, **APP_GOOGLE_Maps}
        self.driver = mobile.Remote(appium_server_url_local, capabilities)
    def touch_skip_start(self):
        #click the skip button from x and y
        x=850
        y=210
        touch_action = TouchAction(self.driver)
        touch_action.tap(x=x, y=y).perform()
    def find_address(self):
        find = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID,'com.google.android.apps.maps:id/search_omnibox_text_box')))
        return find
    def click_address(self):
        self.find_address().click()

    def search_address(self):
        search = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'com.google.android.apps.maps:id/search_omnibox_edit_text')))
        return search

    def send_keys_search_address(self, address):
        self.search_address().send_keys(address)
    def located_address(self):
        located_address = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.LinearLayout[@resource-id="com.google.android.apps.maps:id/compass_container"]/android.widget.LinearLayout')))
        return located_address

    def checked_location(self):
        location2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH,
                                                "//android.widget.TextView[@content-desc='Dizengoff Center']"))
        )
        return location2.text
