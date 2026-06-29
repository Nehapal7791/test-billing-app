"""web/views.py — user-facing page/view controllers (the UI layer).

Each function backs a screen the user actually sees. These are the entry points
QA cares about: "test the Invoice page", "test Checkout". They call down into the
backend (tax, invoice, report, payments).
"""

from src.invoice import format_invoice_summary, generate_invoice
from src.payments import process_payment, refund_payment
from src.report import build_monthly_report, export_report_csv
from src.tax import get_tax_rate


def tax_settings_page(category: str) -> dict:
    """Tax Settings screen — shows the rate applied for a category."""
    rate = get_tax_rate(category)
    return {"screen": "Tax Settings", "category": category, "rate": rate}


def invoice_detail_page(customer_id: str, items: list[dict]) -> dict:
    """Invoice Detail screen — renders a single customer's invoice."""
    invoice = generate_invoice(customer_id, items)
    return {"screen": "Invoice Detail", "summary": format_invoice_summary(invoice)}


def checkout_page(customer_id: str, items: list[dict], payment_method: str) -> dict:
    """Checkout screen — builds the invoice and charges the customer."""
    invoice = generate_invoice(customer_id, items)
    payment = process_payment(invoice, payment_method)
    return {"screen": "Checkout", "invoice": invoice, "payment": payment}


def monthly_report_page(customer_orders: dict) -> dict:
    """Monthly Report screen — revenue + tax summary, CSV export."""
    report = build_monthly_report(customer_orders)
    csv = export_report_csv(report["invoices"])
    return {"screen": "Monthly Report", "report": report, "csv": csv}


def refund_page(payment: dict, reason: str) -> dict:
    """Refund screen — issues a refund against a prior payment."""
    refund = refund_payment(payment, reason)
    return {"screen": "Refund", "refund": refund}
