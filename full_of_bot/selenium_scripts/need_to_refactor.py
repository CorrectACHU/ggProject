


# ************ ACTION IN TEST MODE(LOOKING FOR CLICK ON THE SEND NOW) **********

# IT'S our main weapon to find contacts
def connect_recruiter(x):
    # ENTER URL OF SEARCH WITH FILTERS, MOVE TO X - PAGE IN SEARCH
    driver.get(
        f'https://www.linkedin.com/search/results/people/?industry=%5B%22137%22%2C%22104%22%5D&origin=FACETED_SEARCH&page={x}&sid=Wo7'
    )
    time.sleep(2)

    # TAKES ALL SPANS ON A PAGE
    all_spans = driver.find_elements_by_tag_name("span")

    # FILTER ONLY ARIE-HIDDEN SPANS
    all_spans = [s for s in all_spans if s.get_attribute("aria-hidden") == "true"]

    # MAKE A LIST WITH NAMES ON THE PAGE
    try:
        list_of_names = make_list_of_names(all_spans)
    except NotEnoughItemsForListError:
        print('*' * 100, x, 'FIRST EXCEPTION')
        list_of_names = make_list_of_names(all_spans)
    except NotEnoughItemsForListError:
        print('*' * 150, x, 'MISS EXCEPTION')
        connect_recruiter(x + 1)

    # FINDING OUR BUTTONS
    all_buttons = driver.find_elements_by_tag_name("button")
    connect_buttons = [btn for btn in all_buttons if
                       btn.text == "Connect" or btn.text == "Pending" or btn.text == "Follow" or btn.text == "Following"]

    # VARIABLE FOR THE COUNTER
    counter_clicker = 0

    # LET'S START CLICKING
    for btn in connect_buttons:

        # SKIP FOLLOWING AND PENDING BUTTONS
        if btn.text in ['Following', 'Pending']:
            counter_clicker += 1
            continue
        # CLICK ON THE FOLLOW
        if btn.text in ['Follow']:
            driver.execute_script("arguments[0].click();", btn)
            counter_clicker += 1
            time.sleep(2)
            continue

        name = list_of_names[counter_clicker]
        message = f"Hello, {name}! {prepared_text}"

        # CLICK ON THE CONNECT
        click_of(btn)
        time.sleep(2)

        # CLICK ADD A NOTE
        add_a_note = driver.find_element_by_xpath("//button[@aria-label='Add a note']")
        click_of(add_a_note)
        time.sleep(2)

        # TO ENTER A MESSAGE
        input_message = driver.find_element_by_tag_name("textarea")
        input_message.send_keys(f"{message}")
        time.sleep(2)

        # CLICK ON THE SEND NOW(REPLACE CLOSE WITH SEND IN CLOSE FUNCTION IF YOU WANT TO EXIT THE TEST MODE)
        send = driver.find_element_by_xpath("//button[@arial-label='Send now']")
        close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
        click_of(close)
        time.sleep(2)

        # CHANGE THE COUNT
        print(message)
        print('-' * 20, counter_clicker)
        counter_clicker += 1
        time.sleep(2)
    print('*' * 50, x)
    connect_recruiter(x + 1)


def click_of(a):
    driver.execute_script("arguments[0].click();", a)
