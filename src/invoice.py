"""Invoice generation module."""

from src.tax import calculate_tax


def generate_line_item(description: str, quantity: int, unit_price: float) -> dict:
    subtotal = quantity * unit_price
    tax = calculate_tax(subtotal)
    return {
        "description": description,
        "quantity": quantity,
        "unit_price": unit_price,
        "subtotal": subtotal,
        "tax": tax,
        "total": subtotal + tax,
    }


def generate_invoice(customer_id: str, items: list[dict]) -> dict:
    """Build a full invoice dict for a customer."""
    line_items = [generate_line_item(**item) for item in items]
    subtotal = sum(i["subtotal"] for i in line_items)
    total_tax = sum(i["tax"] for i in line_items)
    return {
        "customer_id": customer_id,
        "line_items": line_items,
        "subtotal": subtotal,
        "tax": total_tax,
        "total": subtotal + total_tax,
    }


def format_invoice_summary(invoice: dict) -> str:
    lines = [f"Customer: {invoice['customer_id']}"]
    for item in invoice["line_items"]:
        lines.append(f"  {item['description']}: £{item['total']:.2f}")
    lines.append(f"Total: £{invoice['total']:.2f}")
    return "\n".join(lines)
