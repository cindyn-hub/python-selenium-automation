from pages.cart_page import CartPage
from pages.header import Header
from pages.navigation_panel import NavigationPanel
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.search_results_page import SearchResultsPage
from pages.base_page import Page
from pages.main_page import MainPage
from pages.side_panel import SidePanel
from pages.signin_page import SigninPage
from pages.target_app_page import TargetAppPage
from pages.terms_conditions_page import TermsConditionsPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.side_panel = SidePanel(driver)
        self.signin_page = SigninPage(driver)
        self.navigation_panel = NavigationPanel(driver)
        self.terms_conditions_page = TermsConditionsPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.privacy_policy_page = PrivacyPolicyPage(driver)



