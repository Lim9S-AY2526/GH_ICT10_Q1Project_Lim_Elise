from pyscript import document, display

# SKU Generator Function
def sku_generation(e):
    # Clear previous output area
    document.getElementById('output').innerHTML = " "

    # Get category input and capitalize first letter
    category = document.getElementById("categories").value.capitalize()

    # Get product name input and convert to uppercase
    product = document.getElementById("prod").value.upper()

    # Get stock quantity input
    stock = document.getElementById("stock").value

    # SKU code
    sku_key = category + "_" + product + "_" + stock

    # Display the generated SKU in output area
    displays("Generated SKU: " + sku_key, target='output')

# Receipt Generator Function
def create_order(e):
    # Clear previous output
    document.getElementById('output').innerHTML = " "

    # Get product checkboxes and their values
    prod1 = document.getElementById("item1")   # Affogato
    prod2 = document.getElementById("item2")   # Cold Brew Malt
    prod3 = document.getElementById("item3")   # Spanish Latte
    prod4 = document.getElementById("item4")   # Americano
    prod5 = document.getElementById("item5")   # Caramel Macchiato

    # Calculate subtotal 
    subtotal = (
        float(prod1.value) * prod1.checked +
        float(prod2.value) * prod2.checked +
        float(prod3.value) * prod3.checked +
        float(prod4.value) * prod4.checked +
        float(prod5.value) * prod5.checked
    )

    # Compute VAT (12%) and total amount
    vat = subtotal * 0.12
    total_amount = subtotal + vat

    # Collect selected items into a list
    products = [
        ("Affogato", prod1),
        ("Cold Brew Malt", prod2),
        ("Spanish Latte", prod3),
        ("Americano", prod4),
        ("Caramel Macchiato", prod5),
    ]
    selected = [f"{name} ₱{p.value}" for name, p in products if p.checked]

    # Combine selected items into one string
    items_text = ", ".join(selected)

    summary = "Subtotal = ₱" + str(subtotal) + " | VAT = ₱" + str(vat) + " | Total = ₱" + str(total_amount)

    # Display items and summary
    display(items_text + " || " + summary, target='output')

