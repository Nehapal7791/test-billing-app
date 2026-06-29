"""Tax calculation module."""

TAX_RATES = {
    "standard": 0.20,
    "reduced": 0.05,
    "zero": 0.0,
}


def get_tax_rate(category: str) -> float:
    if not category or category == "none":
        category = "standard"
    return TAX_RATES.get(category, TAX_RATES["standard"])


def calculate_tax(amount: float, category: str = "standard", discount: float = 0.0) -> float:
    """Calculate tax for a given amount and category, after applying discount."""
    rate = get_tax_rate(category)
    taxable = max(0.0, amount - discount)
    return round(taxable * rate, 2)


def apply_tax_exemption(amount: float, is_exempt: bool) -> float:
    if is_exempt:
        return 0.0
    return calculate_tax(amount)


def validate_tax_number(vat_number: str) -> bool:
    return len(vat_number) >= 9 and vat_number[:2].isalpha()


def recalculate_tax_batch(amounts: list[float], category: str = "standard") -> list[float]:
    return [calculate_tax(a, category) for a in amounts]
