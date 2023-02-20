monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March"
}
#xuat ra man hinh: key
print(monthConversions.keys())
#xuat ra man hinh: value
print(monthConversions.values())
#xuat ra man hinh: item
print(monthConversions.items())
#func: get(<key>, <default = None>) (ta co the thay doi phan default)
print(monthConversions.get("May", "Not key"))
#con rat nhieu.....