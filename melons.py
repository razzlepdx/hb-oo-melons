import random
import datetime
"""Classes for melon orders."""


class AbstractMelonOrder(object):
    """A melon order from somewhere."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):
        """Returns the base price, which varies randomly and conditionally."""

        surcharge = 0
        now = datetime.datetime.now()

        rush_hour_days = range(5)
        rush_hour_hours = [8, 9, 10]

        if now.hours in rush_hour_hours and now.date().weekday() in rush_hour_days:
            surcharge += 4

        return random.randint(5, 9) + surcharge

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        total = (1 + self.tax) * self.qty * base_price

        if self.species == "Christmas":
            base_price *= 1.5

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super(DomesticMelonOrder, self).__init__(species, qty)
        self.tax = 0.08


# GovernmentMelonOrder could instead be a child of DomesticMelonOrder.
# That would be helpful if DomesticMelonOrder had more methods to inherit.
# class GovernmentMelonOrder(DomesticMelonOrder):
class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order within the USA from the US Government"""

    order_type = "domestic"

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.passed_inspection = False
        self.tax = 0

    def mark_inspection(self, passed):
        """Takes a boolean to update whether melon order has passed inspection"""
        if passed:
            self.passed_inspection = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
