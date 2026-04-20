cart = {
    "item1": {"name": "Speaker", "price": 750, "qty": 2},
    "item2": {"name": "Mouse", "price": 1500, "qty": 2},
     "item3": {"name": "Keyword", "price": 500, "qty": 3}
}

l = []
c = 0
for item in cart.values():
    l.append(item['price'])
for n in l:
    if n > c:
        c = n
print(c)