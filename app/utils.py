def dict_as_data(dikt, data):
    for key in dikt.keys():
        data.__setattr__(key, dikt[key])

    return data


def data_as_dict(data, ignore=[]):
    keys = data.__dict__.keys()
    data = dict.fromkeys(keys)

    for key in keys:
        if key in ignore:
            continue
        data[key] = getattr(data, key)

    return data
