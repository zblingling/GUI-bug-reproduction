from appium import webdriver
# from appium.options.android import UiAutomator2Options

import subprocess
import time

# Desired Capabilities
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'Android',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'automationName': 'UiAutomator2',
    # Add other capabilities as needed
}

# Appium Server URL
appium_server_url = 'http://localhost:4723'

# options = UiAutomator2Options()
# cloud_options = {}
# cloud_options['build'] = "build_1"
# cloud_options['name'] = "test_abc"
# options.set_capability('test:options', desired_caps)
# driver = webdriver.Remote(appium_server_url, options=options)

# print("appium connected to the device")

# Start Appium session
driver = webdriver.Remote(command_executor=appium_server_url, desired_capabilities=desired_caps)
print("appium connected to the device")

# Execute ADB command using subprocess
monkey_command = 'adb shell monkey -p com.android.settings --pct-touch 50 --pct-motion 50 -v 500'
subprocess.run(monkey_command, shell=True)

# Close the Appium session
driver.quit()
