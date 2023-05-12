import random

from pages.elements_pages import TextBoxPages, CheckBoxPage, RadioButtonPage, WebTablePage
import time


class TestElements:
    class TestTextElements:

        def test_text_box(self, driver):
            text_box_page = TextBoxPages(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.scroll()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_address, output_per_address = text_box_page.check_fill_form()
            assert full_name == output_name, 'The full name does not match'
            assert email == output_email, 'The email does not match'
            assert current_address == output_cur_address, 'The current address does not match'
            assert permanent_address == output_per_address, 'The permanent address does not match'

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_results()
            assert input_checkbox == output_result

    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', 'radio button "Yes" have not been selected'
            assert output_impressive == 'Impressive', 'radio button "Impressive" have not been selected'
            assert output_no == 'NO', 'radio button "NO" have not been selected'

    class TestWebTables:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            result = web_table_page.check_new_person()
            assert new_person in result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result
