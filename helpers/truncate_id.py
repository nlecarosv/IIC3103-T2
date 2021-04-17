def truncate_id(id_to_be_reviewed):
    if len(id_to_be_reviewed) > 22:
        return id_to_be_reviewed[:22]
    return id_to_be_reviewed
