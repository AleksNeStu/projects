from typing import List

data = [
    {"name": 1},
    {"name": 2},
    {"name": 3},
    {"name": 4},
    {"name": 5},
    {"name": 6},
    {"name": 7},
    {"name": 8},
    {"name": 9},
]


def offset_limit(data: List[dict], offset: int, limit: int):
    r1 = data[offset - 1:][:limit]
    r2 = data[offset - 1:offset - 1 + limit]

    assert r1 == r2
    return r2

def paginate(data: List[dict], page, per_page):
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    paginated_items = data[start_idx:end_idx]
    return paginated_items


p1 = offset_limit(data, offset=1, limit=7)
p2 = paginate(data, page=1, per_page=7)
assert p1 == p2

p3 = offset_limit(data, offset=8, limit=7)
p4 = paginate(data, page=2, per_page=7)
assert p3 == p4

print(p1, p2)