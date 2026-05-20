from playwright.sync_api import Page

from elements.label import Label
from pages.base_page import BasePage
from elements.input import Input
from elements.button import Button
from core.logger import Logger


class LoginPage(BasePage):
    UNIQUE_ELEMENT_LOC = "form:has(#email)"
    EMAIL_LOC = "#email"
    PASSWORD_LOC = "#password"
    SUBMIT_LOC = "form:has(#email) [type='submit']"
    ERROR_BLOCK_LOC = ".bg-destructive\\/10"

    def __init__(self, page: Page):
        super().__init__(page)

        self.unique_element = Label(
            page,
            self.UNIQUE_ELEMENT_LOC,
            description="Login page -> Login form"
        )
        self.email_input = Input(
            page,
            self.EMAIL_LOC,
            description="Login page -> Email input"
        )
        self.password_input = Input(
            page,
            self.PASSWORD_LOC,
            description="Login page -> Password input"
        )
        self.submit_button = Button(
            page,
            self.SUBMIT_LOC,
            description="Login page -> Submit button"
        )
        self.error_block = Label(
            page,
            self.ERROR_BLOCK_LOC,
            description="Login page -> Error block"
        )

    def is_open(self) -> bool:
        return self.unique_element.is_visible()

    def open(self) -> "LoginPage":
        self.navigate()
        Logger.info("LoginPage: opened")
        return self

    def login(self, email: str, password: str) -> None:
        Logger.info(f"LoginPage: login as '{email}'")
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()

    def is_error_visible(self) -> bool:
        return self.error_block.is_visible()