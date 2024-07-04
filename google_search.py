from selene.support.shared import browser
from selene import  be, have


def test_google_search(browser_min):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_search_negative(browser_min):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web'))


def test_google_search_negative2(browser_min):
        #browser.config.browser_name = 'firefox'
        browser.open('https://google.com')
        browser.element('[name="q"]').should(be.blank).type('ghghghghfggg').press_enter()
        browser.config.hold_browser_open = True
        # browser.element('jsname="bVqjv"').click()
        browser.element('[id="botstuff"]').should(have.text('По запросу ghghghghfggg ничего не найдено.'))


def test_search_negative(browser_min):
    browser.element('[name="q"]').should(be.blank).type('gjklsfdhgjksdghdskj').press_enter()
    browser.element('.card-section').should(have.text('По запросу gjklsfdhgjksdghdskj ничего не найдено. '))
