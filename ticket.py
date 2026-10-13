def calculate_ticket_price(age, is_weekend=False, is_member=False):
    """Movie Ticket Price Calculator (PKR).

    Specification
    - age must be an integer between 0 and 120 (inclusive), otherwise "Invalid"
    - Base price: age 0-12 -> 500, age 13-59 -> 1000, age 60-120 -> 600
    - Weekend surcharge: +200
    - Members receive 10% off the price after the surcharge
    """
    # Reject non-integers (bool is a subclass of int, so exclude it explicitly)
    if isinstance(age, bool) or not isinstance(age, int):
        return "Invalid"

    # Check the permitted range
    if age < 0 or age > 120:
        return "Invalid"

    # Base price by age band
    if age <= 12:
        price = 500
    elif age <= 59:
        price = 1000
    else:
        price = 600

    if is_weekend:
        price += 200
    if is_member:
        price = price * 0.90

    return round(price, 2)