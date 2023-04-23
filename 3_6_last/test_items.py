from selenium.webdriver.common.by import By


def test_button_add_to_basket_is_on_page(browser):
    language = browser[1]
    link_part_one = "http://selenium1py.pythonanywhere.com/"
    link_part_two = language
    link_part_three = "/catalogue/coders-at-work_207/"
    link_full = f"{link_part_one}{link_part_two}{link_part_three}"

    browser[0].get(link_full)

    button_add_to_busket = browser[0].find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    button_on_page = len(button_add_to_busket) > 0

    assert not button_on_page, "Button 'Add to busket' is not on page."
