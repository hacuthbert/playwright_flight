from pages.search import SearchPage
from pages.reserve import ReservePage
from pages.purchase import PurchasePage
from playwright.sync_api import Page


def test_book_flight(
    page: Page,
    search_page: SearchPage,
    reserve_page: ReservePage,
    purchase_page: PurchasePage,
) -> None:
    URL = "https://blazedemo.com/"
    search_page.load(URL)
    search_page.search("Boston", "London")
    reserve_page.reserve_flight()
    purchase_page.purchase_flight()
    assert page.get_by_role("heading", name="Thank you for your purchase").is_visible()
