import pandas as pd;

def test_1():
    def register_offer(offer_id, offers=[]):
        return offers + [offer_id]

    first = register_offer("A")
    print(first)
    second = register_offer("B")
    print(first)
    print(second)

    assert first == ["A"]
    assert second == ['B']

    both = register_offer("B", first)
    assert first == ['A']
    assert both == ['A', 'B']
    print(both)
def test_2():
    def average_measurements(values):
        total = 0
        count = 0

        if values is None:
            return None
        else:
            for value in values:
                if value is not None:
                    total += value
                    count += 1
            if count == 0:
                return None
            else:
                return total / count

    list1 = None
    list2 = [1, None, 2, 3]
    list3 = [None, None]
    list4 = [1, 2, 3]
    list5 = [0, 10, None]


    assert average_measurements(list1) is None
    assert average_measurements(list2) == 2.0
    assert average_measurements(list3) is None
    assert average_measurements(list4) == 2.0
    assert average_measurements(list5) == 5.0
def test_3():
    def available_offers(offers):
        offers_available = []
        for offer in offers:
            if offer["stock"] > 0:
                offers_available.append(offer)

        return offers_available

    offers1 = [{"offer_id": "A", "stock": 10}, {"offer_id": "B", "stock": 0}]
    offers2= [{"offer_id": "A", "stock": 10}, {"offer_id": "B", "stock": 2}]
    offers3 = [{"offer_id": "A", "stock": 0}, {"offer_id": "B", "stock": 0}]

    assert available_offers(offers1) == [{"offer_id": "A", "stock": 10}]
    assert available_offers(offers2) == [{"offer_id": "A", "stock": 10}, {"offer_id": "B", "stock": 2}]
    assert available_offers(offers3) == []
def test_4():
    def total_price(offers):
        total = 0.0

        for offer in offers:
            try:
                converted_price_as_float = float(offer["price"])
            except KeyError:
                raise ValueError(f"Missing price value: {offer}")
            except TypeError:
                raise ValueError(f"Invalid price value: {offer['price']}")
            if converted_price_as_float >= 0:
                total += converted_price_as_float
            else:
                raise ValueError(f"Negative price value: {offer['price']}")

        return total

    offers1 = []
    offers2 = [{"price": 1}, {"price": 2}, {"price": 3}]
    offers3 = [{"price": 1}, {"price": 2.25}, {"price": "3.75"}]
    offers4 = [{"price": 1}, {"price": 2.25}, {"price": "3.75"}, {"price": 0}]
    offers5 = [{"price": 1}, {"price": 2.25}, {"price": "3.75"}, {"price": -2}]
    offers6 = [{"price": 1}, {"price": 2.25}, {"price": "3.75"}, {"price": [-2]}]
    offers7 = [{"price": 1}, {"price": 2.25}, {"price": "3.75"}, {"price": None}]
    offers8 = [{"price": 1}, {"price": 2.25}, {"price": "3.75"}, {}]
    offers9 = [{"price": "gratuit"}]

    assert total_price(offers1) == 0.0
    assert total_price(offers2) == 6.0
    assert total_price(offers3) == 7.0
    assert total_price(offers4) == 7.0
    try:
        total_price(offers5)
    except ValueError as e:
        print(e)
    try:
        total_price(offers6)
    except ValueError as e:
        print(e)
    try:
        total_price(offers7)
    except ValueError as e:
        print(e)
    try:
        total_price(offers8)
    except ValueError as e:
        print(e)
    expected_offers9_value = "could not convert string to float: 'gratuit'"
    try:
        total_price(offers9)
    except ValueError as e:
        offers9_value = str(e)
    assert offers9_value == expected_offers9_value

def test_5():
    def summarize_offers(offers, sellers):
        offers_with_stock = offers.query("stock > 0")

        enriched = offers_with_stock.merge(
            sellers,
            on="seller_id",
            how="left",
        )

        enriched["country"] = enriched["country"].fillna("UNKNOWN")

        summary = enriched.groupby("country").agg(
            offers_count=("offer_id", "count"),
            stock_count=("stock", "sum"),
            average_price=("price", "mean"),
        )

        return summary[summary["stock_count"] > 0][["offers_count", "average_price"]].reset_index()

    offers1 = pd.DataFrame([
        {"offer_id": 1, "stock": 3, "price": 10, "seller_id": "A"},
        {"offer_id": 2, "stock": 2, "price": 2, "seller_id": "A"},
        {"offer_id": 3, "stock": 3, "price": 20, "seller_id": "B"},
        {"offer_id": 4, "stock": 0, "price": 5, "seller_id": "C"},
        {"offer_id": 5, "stock": 5, "price": 12, "seller_id": "D"},
        {"offer_id": 6, "stock": 4, "price": 6, "seller_id": "E"},
        
    ]
    )
    # Other way to define
    offers1_alt = pd.DataFrame({"offer_id": [1, 2, 3, 4, 5, 6], "stock": [3, 2, 3, 0, 5, 4], "price": [10, 2, 20, 5, 12, 6], "seller_id": ["A", "A", "B", "C", "D", "E"]})
    assert offers1_alt.equals(offers1)

    sellers1 = pd.DataFrame([
        {"seller_id": "A", "country": "France"},
        {"seller_id": "B", "country": "Italie"},
        {"seller_id": "C", "country": "Espagne"},
        {"seller_id": "E", "country": "France"},
    ]
    )

    print(summarize_offers(offers1, sellers1))
    expected_summary = pd.DataFrame(
        {"country": ["France", "Italie", "UNKNOWN"], "offers_count": [3, 1, 1], "average_price": [6.0, 20.0, 12.0]}
    )
    offers1_copy = offers1.copy(deep=True)
    sellers1_copy = sellers1.copy(deep=True)

    assert summarize_offers(offers1, sellers1).equals(expected_summary)
    assert offers1_copy.equals(offers1)
    assert sellers1_copy.equals(sellers1)


test_1()
test_2()
test_3()
test_4()
test_5()
