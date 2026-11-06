def calculate_total(items: list[dict]):
    subtotal = sum(item["price"]*item["quantity"] for item in items)
    tax = subtotal//10
    return {"subtotal": subtotal, "tax": tax, "total": subtotal+tax}
