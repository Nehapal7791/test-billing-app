"""Report export module."""

import csv
import io
import json

from src.invoice import generate_invoice


def export_report_csv(invoices: list[dict]) -> str:
    """Export a list of invoices as CSV."""
    out = io.StringIO()
    writer = csv.DictWriter(
        out, fieldnames=["customer_id", "subtotal", "tax", "total"]
    )
    writer.writeheader()
    for inv in invoices:
        writer.writerow({
            "customer_id": inv["customer_id"],
            "subtotal": inv["subtotal"],
            "tax": inv["tax"],
            "total": inv["total"],
        })
    return out.getvalue()


def export_report_json(invoices: list[dict]) -> str:
    return json.dumps(invoices, indent=2)


def build_monthly_report(customer_orders: dict[str, list]) -> dict:
    """Build a monthly report from a map of customer_id → order list."""
    invoices = [
        generate_invoice(cid, orders)
        for cid, orders in customer_orders.items()
    ]
    return {
        "invoices": invoices,
        "total_revenue": sum(i["total"] for i in invoices),
        "total_tax_collected": sum(i["tax"] for i in invoices),
    }


def export_report_pdf(invoices: list[dict]) -> bytes:
    # placeholder
    return b"%PDF stub"
