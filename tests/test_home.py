from playwright.sync_api import Page, expect
import os, json


pwdata = json.loads(os.environ['pwdata'])
homepage = pwdata['homepage']
user = pwdata['user']
passwd = pwdata['passwd']


def test_version(page: Page) -> None:  
    page.goto(homepage)
    version = page.locator('xpath=/html/body/footer/div/small')
    expect(version).to_contain_text("SCE 3.5.3.1:v175SALEM")
    signin = page.locator('#new_user > fieldset > legend')
    expect(signin).to_contain_text("Sign in")


def test_login(page: Page) -> None:
    page.goto(homepage)
    page.locator('id=user_email').fill(user)
    page.locator('id=user_password').fill(passwd)
    page.get_by_role("button", name="Sign in").click()
    dashboard = page.locator('xpath=/html/body/main/div[1]')
    expect(dashboard).to_contain_text("Dashboard")


def test_menu(page: Page) -> None:
    page.goto(homepage)
    page.locator('id=user_email').fill(user)
    page.locator('id=user_password').fill(passwd)
    page.get_by_role("button", name="Sign in").click()
    page.locator('body > header > nav > ul.toolbar.toolbar__search > li.toolbar__settings > a > i').click()


def test_myprofile(page: Page) -> None:
    page.goto(homepage)
    page.locator('id=user_email').fill(user)
    page.locator('id=user_password').fill(passwd)
    page.get_by_role("button", name="Sign in").click()
    page.locator('body > header > nav > ul.toolbar.toolbar__search > li.toolbar__settings > a > i').click()
    page.locator('body > header > nav > ul > li.toolbar__settings > ul > li:nth-child(2) > a').click()
    profileHeader = page.locator('#edit_user > h2')
    expect(profileHeader).to_contain_text("My Profile")


def test_promotesession(page: Page) -> None:
    page.goto(homepage)
    page.locator('id=user_email').fill(user)
    page.locator('id=user_password').fill(passwd)
    page.get_by_role("button", name="Sign in").click()
    page.locator('body > header > nav > ul.toolbar.toolbar__search > li.toolbar__settings > a > i').click()
    page.locator('body > header > nav > ul.toolbar.toolbar__search > li.toolbar__settings > ul > li:nth-child(3) > a').click()
    dashboard = page.locator('body > main > div.primary-heading')
    expect(dashboard).to_contain_text("Dashboard")

    


