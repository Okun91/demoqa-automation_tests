import os
from selenium.webdriver import Keys
from generator.generator import generator_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_form_field(self):
        person = next(generator_person())
        file_name, path = generated_file()
        self.remove_footer()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.firstname)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.lastname)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)
        self.element_is_visible(self.locators.SUBJECTS).send_keys('English')
        self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.RETURN)
        hobby = self.element_is_visible(self.locators.HOBBIES)
        self.go_to_element(hobby)
        hobby.click()
        self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        select_state = self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_SITY).click()
        self.element_is_visible(self.locators.SITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT).click()
        return person

    def form_result(self):
        result_list = self.elements_are_present(self.locators.TABLE)
        data = []
        for i in result_list:
            self.go_to_element(i)
            data.append(i.text)
        return data
