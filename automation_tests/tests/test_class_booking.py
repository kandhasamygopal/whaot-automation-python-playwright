class BookingPage:
    def __init__(self, page):
        self.page = page
        self.class_search_box = "input[placeholder='Master CBSE 8th Grade Physics: Force, Friction, Sound, Light & More Concepts']"
        self.search_result = ".class-result:first-child"
        self.book_button = "button.book-class"
        self.confirm_message = ".booking-confirmation"

    def search_class(self, class_name):
        self.page.fill(self.class_search_box, class_name)
        self.page.press(self.class_search_box, "Enter")

    def book_first_class(self):
        self.page.click(self.search_result)
        self.page.click(self.book_button)

    def is_booking_successful(self):
        return self.page.is_visible(self.confirm_message)
