import pytest

from pages.search import SearchPage
from pages.reserve import ReservePage
from pages.purchase import PurchasePage
from playwright.sync_api import Page


@pytest.fixture
def search_page(page: Page) -> SearchPage:
    return SearchPage(page)


@pytest.fixture
def reserve_page(page: Page) -> ReservePage:
    return ReservePage(page)


@pytest.fixture
def purchase_page(page: Page) -> PurchasePage:
    return PurchasePage(page)
