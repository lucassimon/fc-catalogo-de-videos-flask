def replace_id_to_take_snapshot(items):
    for item in items:
        item["id"] = "replaced to take snapshot"

    return items
