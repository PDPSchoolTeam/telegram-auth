from requests import get


def get_lang_lit(ip: str) -> list:
    dataset = {}
    data = get(f"https://ipinfo.io/{ip}/json")
    for x in data.json().items():
        key, val = x
        dataset[key] = val
    lan_lat = dataset.get('loc')
    s = lan_lat.split(',')

    latitude = s[0]
    longitude = s[1]
    return [latitude, longitude]
