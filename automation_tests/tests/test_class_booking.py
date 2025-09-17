from pages.login_page import LoginPage
from pages.booking_page import BookingPage

def test_single_class_booking(page):
    login = LoginPage(page)
    login.navigate()
    login.login("testuser", "secret123")

    booking = BookingPage(page)
    booking.search_class("Yoga")
    booking.book_class_by_index(0)

    assert booking.is_booking_successful()

def test_cancel_booking(page):
    login = LoginPage(page)
    login.navigate()
    login.login("testuser", "secret123")

    booking = BookingPage(page)
    booking.search_class("Pilates")
    booking.book_class_by_index(0)
    booking.cancel_booking()

    assert booking.is_cancel_successful()

def test_booking_history(page):
    login = LoginPage(page)
    login.navigate()
    login.login("testuser", "secret123")

    booking = BookingPage(page)
    booking.search_class("Zumba")
    booking.book_class_by_index(0)

    booking.open_booking_history()
    history = booking.get_booking_history_items()

    assert any("Zumba" in item for item in history)

def test_multiple_class_bookings(page):
    login = LoginPage(page)
    login.navigate()
    login.login("testuser", "secret123")

    booking = BookingPage(page)
    booking.book_multiple_classes(["Yoga", "Pilates", "Zumba"])

    booking.open_booking_history()
    history = booking.get_booking_history_items()

    for cls in ["Yoga", "Pilates", "Zumba"]:
        assert any(cls in item for item in history)

