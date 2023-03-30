import logging

logging.basicConfig(
    filename='meu_log.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.info('Teste iniciado')

from appium import webdriver

desired_caps = {'platformName': 'Android', 'deviceName': 'Android Emulator', 'app': '/path/to/app.apk',
                'automationName': 'UiAutomator2', 'appium:logLevel': 'debug', 'appium:chromeOptions': {'w3c': False}}

# habilitando o logging do Appium Server

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

from loguru import logger

logger.add("meu_log.log")

logger.info('Teste iniciado')
