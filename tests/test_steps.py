import allure
from allure_commons.types import Severity

from model.pages.registration_page import RegistrationPage


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "rusak")
@allure.feature("Регистрация")
@allure.story("Пользователь может зарегистрироваться на DemoQA")
@allure.link("https://https://demoqa.com/", name="Testing")
@allure.title("new_user_registration")
@allure.description("some good description should be here")
def test_complete_todo():
    with allure.step("Открываем форму регистрации"):
        registration_page = RegistrationPage()
        registration_page.open()

    with allure.step("Заполняем форму"):
        registration_page.fill_first_name('John')
        registration_page.fill_last_name('Week')
        registration_page.fill_email('john.week@example.com')
        registration_page.select_gender("Male")
        registration_page.fill_mobile('9123456789')
        registration_page.fill_date_of_birth('2000', 'May', '4')
        registration_page.select_subjects('Math')
        registration_page.select_hobbies('Sports')
        registration_page.select_hobbies('Music')
        registration_page.select_picture('test01.png')
        registration_page.fill_curent_address('ул. Ленина 4')
        registration_page.fill_state('Haryana')
        registration_page.fill_city('Panipat')
        registration_page.submit_form()

    with allure.step("Проверяем результат"):
        registration_page.should_have_registered(
            'John Week',
            'john.week@example.com',
            'Male',
            '9123456789',
            '04 May,2000',
            'Maths',
            'Sports, Music',
            'test01.png',
            'ул. Ленина 4',
            'Haryana Panipat',
        )
