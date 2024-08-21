from Address import Address
from Mailing import Mailing


to_address = Address("123456", "Тверь", "Ленина", "1", "25")
from_address = Address("568132", "Саратов", "Пушкина", "65", "30")


mailing = Mailing(to_address, from_address, 345, "TRACK123456")


print("Отправление " +
      mailing.track +
      " из " +
      mailing.from_address.index +
      ", " +
      mailing.from_address.city +
      ", " +
      mailing.from_address.street +
      ", " +
      mailing.from_address.house +
      " - " +
      mailing.from_address.apartment +
      " в " +
      mailing.to_address.index +
      ", " +
      mailing.to_address.city +
      ", " +
      mailing.to_address.street +
      ", " +
      mailing.to_address.house +
      " - " +
      mailing.to_address.apartment +
      ". Стоимость " +
      str(mailing.cost) +
      " рублей.")
