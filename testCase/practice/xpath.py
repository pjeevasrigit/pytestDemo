from playwright.sync_api import Page, expect

def test_xpath(page: Page):

    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(3000)

    products = page.locator("//h2/a[contains(@href,'computer')]")

    print("Products count:", products.count())

    print("first product:", products.first.text_content())
    print("last product:", products.last.text_content())
    print("3rd product:", products.nth(2).text_content())

    product_title = products.all_text_contents()

    print("All titles", product_title)

    for i in product_title:
        print(i)



    ######### webpage handling

    page.goto("https://testautomationpractice.blogspot.com/")

    text_box = page.locator("#name")

    expect(text_box).to_be_visible()
    expect(text_box).to_be_enabled()

    expect(text_box).to_have_attribute("maxlength", "15")

    print("maxlength:", text_box.get_attribute("maxlength"))

    text_box.fill("testing web")

    enteredValue = text_box.input_value()

    print("Value entered:", enteredValue)

    male_radio = page.locator("#male")

    expect(male_radio).not_to_be_checked()

    male_radio.click()

    expect(male_radio).to_be_checked()

    days = ['Sunday','Monday','Tuesday','Wednesday',
            'Thursday','Friday','Saturday']

    checkboxes = []

    for day in days:
        checkbox = page.get_by_label(day)
        checkboxes.append(checkbox)

    allCheckboxes = [page.get_by_label(day) for day in days]

    print("total number of days", len(allCheckboxes))

    for checkbox in checkboxes:
        checkbox.check()
        expect(checkbox).to_be_checked()

    for checkbox in checkboxes[-3:]:
        checkbox.uncheck()
        expect(checkbox).not_to_be_checked()

    #####################################################

    page.locator("#country").select_option(label="India")

    dropdownOptions = page.locator("#country > option")

    expect(dropdownOptions).to_have_count(10)

    option_text = [
        text.strip()
        for text in dropdownOptions.all_text_contents()
    ]

    print(option_text)

    for country in option_text:
        print(country)

    #multiple dropdown
    page.locator("#colors").select_option(['Red','Blue','Green'])
    page.locator("#colors").select_option(label=['Red','Blue','Green'])
    page.locator("#colors").select_option(value=['Red','Blue','Green'])
    page.locator("#colors").select_option(index=[2,4])

    dropdown_multi = page.locator("#colors>options")
    expect(dropdown_multi).to_have_count(7)
