from ticket import calculate_ticket_price


# --- Equivalence-class tests (Lab 2) ---
def test_child_ticket():
    assert calculate_ticket_price(8) == 500


def test_adult_ticket():
    assert calculate_ticket_price(30) == 1000


# --- Boundary-value tests (Lab 2) ---
def test_senior_lower_boundary():
    assert calculate_ticket_price(60) == 600


def test_child_upper_boundary():
    assert calculate_ticket_price(12) == 500


def test_age_above_maximum():
    assert calculate_ticket_price(121) == "Invalid"


def test_negative_age():
    assert calculate_ticket_price(-1) == "Invalid"


# --- Decision-table tests (Lab 4) ---
def test_weekend_surcharge():
    assert calculate_ticket_price(30, is_weekend=True) == 1200


def test_member_discount_on_weekend():
    assert calculate_ticket_price(30, is_weekend=True, is_member=True) == 1080