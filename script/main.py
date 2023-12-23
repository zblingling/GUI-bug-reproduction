import time
import subprocess as sp
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common import MobileEvent, EventFiringWebDriver
from datetime import datetime
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService

class AppiumListener(MobileEvent):
    def on_touch(self, event, driver):
        get_current_page_source(driver)

def start_appium_server():
    ip_address = '127.0.0.1'
    port = '4725'
    date = datetime.now().strftime("%Y%m%d%H%M")

    # Run Appium server, store logfile
    appium_service = AppiumService()
    appium_service.start(args=[
        '--address', ip_address,
        '-p', port,
        '--log-timestamp',
        '--log', './logs/{}.appium.log'.format(date),
    ], stdout=sp.DEVNULL)

    print("appium is running : ", appium_service.is_running)
    print("appium is listening : ", appium_service.is_listening)

    return ip_address, port

def initialize_driver(ip_address, port):
    options = UiAutomator2Options()
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "13",
        "deviceName": "Android Emulator",
        "appPackage": "com.google.android.calculator",
        "appActivity": "com.android.calculator2.Calculator"
    }
    options.set_capability('appium:chromeOptions', desired_caps)

    # appium 1-->2: no need to add /wd/hub to the end of the url
    # appium 2: no slash at the end of the url
    driver = EventFiringWebDriver(
        webdriver.Remote(
            command_executor='http://{}:{}'.format(ip_address, port),
            options=options
        ),
        AppiumListener()
    )

    print("appium is connected to the device")
    return driver

def get_current_page_source(driver):
    xml_string = driver.page_source
    xml_path = f'./xml/{time.time()}.appium.xml'
    with open(xml_path, 'w', encoding='utf-8') as xml_file:
        xml_file.write(xml_string)
    print(f'Page source saved to: {xml_path}')

def main():
    ip_address, port = start_appium_server()
    driver = initialize_driver(ip_address, port)

    try:
        while True:
            # 添加适当的延迟，等待用户操作触发事件
            time.sleep(1)
    except KeyboardInterrupt:
        # 捕获 Ctrl+C 信号，退出循环
        print("Exiting the loop.")
    finally:
        # 关闭 Appium 会话
        driver.quit()

if __name__ == "__main__":
    main()
