users_data = [
    {
        "id": 1,
        "role": "admin",
        "name": "Alice",
        "degree": [
            {
                "id": 1,
                "created_at": "2020-01-01T00:00:00",
                "type_degree": "expert"
            }
        ]
    },
    {
        "id": 2,
        "role": "investor",
        "name": "Eve"
    },
    {
        "id": 3,
        "role": "trader",
        "name": "Charlie",
        "degree": [
            {
                "id": 1,
                "created_at": "2021-02-15T10:30:00",
                "type_degree": "newbie"
            }
        ]
    },
    {
        "id": 4,
        "role": "admin",
        "name": "Bob"
    },
    {
        "id": 5,
        "role": "investor",
        "name": "David"
    },
    {
        "id": 6,
        "role": "trader",
        "name": "Frank"
    },
    {
        "id": 7,
        "role": "admin",
        "name": "Grace"
    }
]

trades_data = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
    {"id": 3, "user_id": 2, "currency": "ETH", "side": "buy", "price": 130, "amount": 1.5},
    {"id": 4, "user_id": 2, "currency": "ETH", "side": "sell", "price": 135, "amount": 1.0},
    {"id": 5, "user_id": 3, "currency": "BTC", "side": "buy", "price": 128, "amount": 2.0},
    {"id": 6, "user_id": 3, "currency": "BTC", "side": "sell", "price": 135, "amount": 2.5},
    {"id": 7, "user_id": 4, "currency": "ETH", "side": "buy", "price": 120, "amount": 3.0},
    {"id": 8, "user_id": 4, "currency": "ETH", "side": "sell", "price": 125, "amount": 2.0},
    {"id": 9, "user_id": 5, "currency": "BTC", "side": "buy", "price": 130, "amount": 1.0},
    {"id": 10, "user_id": 5, "currency": "BTC", "side": "sell", "price": 135, "amount": 0.5},
    {"id": 11, "user_id": 6, "currency": "ETH", "side": "buy", "price": 140, "amount": 2.5},
    {"id": 12, "user_id": 6, "currency": "ETH", "side": "sell", "price": 145, "amount": 3.0},
    {"id": 13, "user_id": 7, "currency": "BTC", "side": "buy", "price": 123, "amount": 1.0},
    {"id": 14, "user_id": 7, "currency": "BTC", "side": "sell", "price": 125, "amount": 1.5},
]
