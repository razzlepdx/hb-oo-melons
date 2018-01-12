"""Classes for melon orders."""


class AbstractMelonOrder(object):
    """A melon order from somewhere."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == "Christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price
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
