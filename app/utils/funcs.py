def dict_as_data(dikt, data):
    for key in dikt.keys():
        setattr(data, key, dikt[key])

    return data


def data_as_dict(data, ignore=None):
    if ignore is None:
        ignore = []

    keys = vars(data).keys()
    data = dict.fromkeys(keys)

    for key in keys:
        if key in ignore:
            continue
        data[key] = getattr(data, key)

    return data
