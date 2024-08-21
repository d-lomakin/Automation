from smartphone import Smartphone

catalog = []


catalog.append(Smartphone("Apple", "iPhone 11", "+79161234567"))
catalog.append(Smartphone("Samsung", "Galaxy A30", "+79162345678"))
catalog.append(Smartphone("Google", "Pixel 6", "+79163456789"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79164567890"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79165678901"))


for phone in catalog:
    print(phone.brand + " - " + phone.model + ". " + phone.phone_number)
