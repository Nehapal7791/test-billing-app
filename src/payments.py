"""Payment processing module."""

from src.invoice import generate_invoice


def process_payment(invoice: dict, payment_method: str) -> dict:
    """Process payment for an invoice."""
    if payment_method not in ("card", "bank_transfer", "direct_debit"):
        raise ValueError(f"Unknown payment method: {payment_method}")
    return {
        "invoice_id": invoice.get("customer_id"),
        "amount_charged": invoice["total"],
        "method": payment_method,
        "status": "success",
    }


def refund_payment(payment: dict, reason: str) -> dict:
    return {
        "original_payment": payment,
        "refund_amount": payment["amount_charged"],
        "reason": reason,
        "status": "refunded",
    }
