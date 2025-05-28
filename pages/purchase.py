from playwright.sync_api import Page


class PurchasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.name_input = page.get_by_role("textbox", name="Name", exact=True)
        self.address_input = page.get_by_role("textbox", name="Address")
        self.city_input = page.get_by_role("textbox", name="City")
        self.state_input = page.get_by_role("textbox", name="State")
        self.zip_code_input = page.get_by_role("textbox", name="Zip Code")
        self.credit_card_number_input = page.get_by_role(
            "textbox", name="Credit Card Number"
        )
        self.month_input = page.get_by_role("textbox", name="Month")
        self.year_input = page.get_by_role("textbox", name="Year")
        self.name_on_card_input = page.get_by_role("textbox", name="Name on Card")
        self.purchase_button = page.get_by_role("button", name="Purchase Flight")

    def purchase_flight(self) -> None:
        self.name_input.fill("John Smith")
        self.address_input.fill("25 Fretz Road")
        self.city_input.fill("Souderton")
        self.state_input.fill("PA")
        self.zip_code_input.fill("18964")
        self.credit_card_number_input.fill("4000400040004000")
        self.month_input.fill("11")
        self.year_input.fill("2018")
        self.name_on_card_input.fill("John Smith")
        self.purchase_button.click()
