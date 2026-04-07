def insert_unique_items(collection, items, pincode_field, item_field):
    inserted = []
    duplicates = []

    for item in items:
        query = {item_field: item[item_field], pincode_field: item[pincode_field]}
        exists = collection.find_one(query)

        if exists:
            duplicates.append(item)
        else:
            collection.insert_one(item)
            inserted.append(item)

    return inserted, duplicates