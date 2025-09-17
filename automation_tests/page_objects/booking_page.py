class BookingPage:
    def __init__(self, page):
        self.page = page
        # Locators
        self.class_search_box = "input[placeholder='Search classes']"
        self.search_results = ".class-result"        # all results
        self.book_button = "button.book-class"       # inside a class card
        self.confirm_message = ".booking-confirmation"

        self.cancel_button = "button.cancel-booking"
        self.cancel_confirm_message = ".cancel-confirmation"

        self.booking_history_tab = "a[href='/booking-history']"
        self.booking_history_items = ".history-item"

    # ---------- Booking flow ----------
    def search_class(self, class_name: str):
        self.page.fill(self.class_search_box, class_name)
        self.page.press(self.class_search_box, "Enter")
        self.page.wait_for_selector(self.search_results)

    def book_class_by_index(self, index=0):
        results = self.page.query_selector_all(self.search_results)
        if len(results) > index:
            results[index].click()
            self.page.click(self.book_button)
            self.page.wait_for_selector(self.confirm_message)
        else:
            raise Exception("No class found to book.")

    def book_multiple_classes(self, class_names: list[str]):
        for class_name in class_names:
            self.search_class(class_name)
            self.book_class_by_index(0)

    def is_booking_successful(self) -> bool:
        return self.page.is_visible(self.confirm_message)

    # ---------- Cancel booking ----------
    def cancel_booking(self):
        self.page.click(self.cancel_button)
        self.page.wait_for_selector(self.cancel_confirm_message)

    def is_cancel_successful(self) -> bool:
        return self.page.is_visible(self.cancel_confirm_message)

    # ---------- Booking history ----------
    def open_booking_history(self):
        self.page.click(self.booking_history_tab)
        self.page.wait_for_selector(self.booking_history_items)

    def get_booking_history_items(self) -> list[str]:
        items = self.page.query_selector_all(self.booking_history_items)
        return [item.inner_text() for item in items]
