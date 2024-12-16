from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

MOBILE_EMULATION = {"deviceName": "iPhone XR"}
DRIVER_PATH_EXISTED = "C:/Users/katya/.wdm/drivers/chromedriver/win64/131.0.6778.108/chromedriver-win32/chromedriver.exe"
BROWSER_PATH_EXISTED = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
URL = "https://www.google.com"
EXPECTED_TITLE = "Google"


def log_versions(driver):
    driver_version = driver.capabilities['chrome']['chromedriverVersion']
    browser_version = driver.capabilities['browserVersion']
    print(f"\nДрайвер: {driver_version}\nБраузер: {browser_version}")


def test_mobile_browser_with_service_path():
    """Запуск уже установленного драйвера по указанному пути (через сервис) с мобильным видом. """
    options = Options()
    options.add_experimental_option("mobileEmulation", MOBILE_EMULATION)
    #  только если браузер не в стандартной папке или переименован
    options.binary_location = BROWSER_PATH_EXISTED

    service = ChromeService(executable_path=DRIVER_PATH_EXISTED)
    driver = webdriver.Chrome(service=service, options=options)
    log_versions(driver)

    driver.get(URL)
    actual_title = driver.title
    driver.quit()

    assert EXPECTED_TITLE in actual_title


def test_mobile_browser_with_service_default():
    """Запуск уже установленного драйвера по пути из переменной окружения PATH (через сервис) с мобильным видом.

    PATH (Win):
    окно System Properties -> вкладка Advanced - Environments Variables...
    в нижнем разделе System variables отредактировать строку 'Path',
    добавив путь к ПАПКЕ хромдрайвера (F:\chromedriver), где должен быть ФАЙЛ chromedriver.exe

    Как найти окно System Properties:
    1. <Win> искать 'Envir...'
    2. или Пуск -> Правой кнопкой -> Setting -> Ищем 'Environment...'
    3. или Пуск -> Правой кнопкой -> System -> Advanced system settings
    """
    options = Options()
    options.add_experimental_option("mobileEmulation", MOBILE_EMULATION)

    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=options)
    log_versions(driver)

    driver.get(URL)
    actual_title = driver.title
    driver.quit()

    assert EXPECTED_TITLE in actual_title


def test_mobile_browser_with_service_install():
    """Скачивание и запуск драйвера (через сервис) с мобильным видом. """
    options = Options()
    options.add_experimental_option("mobileEmulation", MOBILE_EMULATION)

    path_installed = ChromeDriverManager().install()
    service = ChromeService(executable_path=path_installed)
    driver = webdriver.Chrome(service=service, options=options)
    log_versions(driver)

    driver.get(URL)
    actual_title = driver.title
    driver.quit()

    assert EXPECTED_TITLE in actual_title


def test_mobile_browser_default():
    """Запуск уже установленного драйвера с мобильным видом.
    Без сервиса можно запустить только уже установленный драйвер
    (из переменной окружения PATH или ранее скачанный в %USERPROFILE%\.wdm или из кэша и т.д.).
    """
    options = Options()
    options.add_experimental_option("mobileEmulation", MOBILE_EMULATION)

    driver = webdriver.Chrome(options=options)
    log_versions(driver)

    driver.get(URL)
    actual_title = driver.title
    driver.quit()

    assert EXPECTED_TITLE in actual_title
