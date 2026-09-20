from pyscript import document, display

def sku_generation(e):
    document.getElementById('output').innerHTML = " "
    category = document.getElementById("categories").value.capitalize()
    product = document.getElementById("prod").value.upper()
    stock = document.getElementById("stock").value
    sku_key = category + "_" + product + "_" + stock
    display(sku_key, target='output')

def create_order(e):
    document.getElementById('output').innerHTML = " "
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")

    subtotal = (
        float(prod1.value) * prod1.checked +
        float(prod2.value) * prod2.checked +
        float(prod3.value) * prod3.checked +
        float(prod4.value) * prod4.checked +
        float(prod5.value) * prod5.checked
    )
    vat = subtotal * 0.12
    total_amount = subtotal + vat

    products = [
        ("Affogato", prod1),
        ("Cold Brew Malt", prod2),
        ("Spanish Latte", prod3),
        ("Americano", prod4),
        ("Caramel Macchiato", prod5),
    ]
    selected = [f"{name} ₱{p.value}" for name, p in products if p.checked]
    
    items_text = ", ".join(selected)
    summary = f"Subtotal = ₱{subtotal:.2f} | VAT = ₱{vat:.2f} | Total = ₱{total_amount:.2f}"

    display(items_text + "\n" + summary, target='output')
