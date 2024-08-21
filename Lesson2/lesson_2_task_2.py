def is_year_leap(year):
    return year % 4 == 0


year = int(input("Введите год: "))


leap_year = is_year_leap(year)


print(f"год {year}: {leap_year}")
