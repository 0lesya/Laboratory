from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest


def wait_of_element(xpath, driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element


@pytest.fixture
def driver_init():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, executable_path=r'C:/Users/Олеся/Downloads/chromedriver_win32/chromedriver.exe')
    yield driver


def test_good_search(driver_init):
    driver_init.get('https://www.rsl.ru/')
    # поиск ячейки поиска
    el = wait_of_element(xpath='//*[@id="header"]/div[2]/div[2]/div[2]/div/input', driver=driver_init)
    el.send_keys("де Мопассан")
    el.send_keys(Keys.RETURN)
    time.sleep(2)
    try:
        driver_init.find_element(By.LINK_TEXT, 'имидж-каталогам')
        for_assert = ''
    except Exception as e:
        for_assert = 'Поиск автора проведен успешно'

    assert for_assert == 'Поиск автора проведен успешно'


def test_bad_search(driver_init):
    driver_init.get('https://www.rsl.ru/')
    el = wait_of_element(xpath='//*[@id="header"]/div[2]/div[2]/div[2]/div/input', driver=driver_init)
    el.send_keys("fhrtjnep[wf[w[et0vsdvmsb")
    el.send_keys(Keys.RETURN)
    time.sleep(3)


def test_vk(driver_init):
    try:
        driver_init.find_element(By.CLASS_NAME, "social-btn social-btn-vk")
    except Exception as e:
        print(e)


def test_authorization(driver_init):
    driver_init.get(
        "https://passport.rusneb.ru/auth/realms/RSL/protocol/openid-connect/auth?response_type=code&redirect_uri=https%3A%2F%2Fwww.rsl.ru%2Flogin&client_id=rsl.ru&scope=rsl_udb_profile+openid")

    # Поиск элементов и присваивание к переменным.
    input_email = wait_of_element(xpath='//*[@id="sign-in__form"]/div[1]/input', driver=driver_init)
    input_password = wait_of_element(xpath='//*[@id="sign-in__form"]/div[2]/input', driver=driver_init)
    login_button = wait_of_element(xpath='//*[@id="sign-in__form"]/div[6]/button', driver=driver_init)

    # Действия с формами
    input_email.send_keys("polesyka@gmail.com")
    input_password.send_keys("Marselyka1")
    login_button.click()

    # Поиск и проверка попадания на главную страницу

    title_text = wait_of_element(xpath='//*[@id="header"]/div[2]/div[1]/div[2]/div[1]/div[1]/span', driver=driver_init)
    assert title_text.text == "Олеся"


if __name__ == '__main__':
    driver = driver_init
    test_good_search(driver)
    test_bad_search(driver)
    test_authorization(driver)
    test_vk(driver)
