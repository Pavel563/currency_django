def parse_cookie(query):
    if query == '':
        return {}
    data = query.split(';')
    response = dict()  # TODO лучше делать так response = {}
    for row in data:
        if row != '':
            # row = row.split('=', maxsplit=1)
            # response[row[0]] = row[1]
            # TODO
            key, value = row.split('=', maxsplit=1)
            response[key] = value
    return response
