from pprint import pprint

from requests import get


def get_lang_lit(ip: str) -> list:
    dataset = {}
    data = get(f"https://ipinfo.io/{ip}/json")
    for x in data.json().items():
        key, val = x
        dataset[key] = val
    pprint(dataset)
    lan_lat = dataset.get('loc')
    s = lan_lat.split(',')

    latitude = s[0]
    longitude = s[1]
    return [latitude, longitude]

get_lang_lit('95.214.211.134')