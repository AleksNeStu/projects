from collections import defaultdict


def get_id_map(data):
    id_dict = defaultdict(list)
    for item in data:
        id_dict[item["id"]].append(item)
    return id_dict


def get_by_id(data, target_id):
    id_map = get_id_map(data)
    res = id_map.get(target_id)
    if res and len(res) == 1:
        return res[0]
