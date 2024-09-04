
import pytest
from StringUtils import StringUtils

# Инициализация экземпляра класса
utils = StringUtils()


def test_capitilize():
    # Позитивный тест
    assert utils.capitilize("skyeng") == "Skyeng"
    assert utils.capitilize("Skyeng") == "Skyeng"

    # Негативный тест (например, пустая строка)
    assert utils.capitilize("") == ""


def test_trim():
    # Позитивный тест
    assert utils.trim("   skyeng") == "skyeng"
    assert utils.trim("skyeng") == "skyeng"

    # Негативный тест (например, пустая строка)
    assert utils.trim("   ") == ""


def test_to_list():
    # Позитивные тесты
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]

    # Негативные тесты
    assert utils.to_list("") == []
    assert utils.to_list(None) == []


def test_contains():
    # Позитивные тесты
    assert utils.contains("SkyEng", "S") is True
    assert utils.contains("SkyEng", "U") is False


def test_delete_symbol():
    # Позитивные тесты
    assert utils.delete_symbol("SkyEng", "k") == "SyEng"
    assert utils.delete_symbol("SkyEng", "Eng") == "Sky"


def test_starts_with():
    # Позитивные тесты
    assert utils.starts_with("SkyEng", "S") is True
    assert utils.starts_with("SkyEng", "E") is False


def test_end_with():
    # Позитивные тесты
    assert utils.end_with("SkyEng", "g") is True
    assert utils.end_with("SkyEng", "y") is False


def test_is_empty():
    # Позитивные тесты
    assert utils.is_empty("") is True
    assert utils.is_empty("   ") is True
    assert utils.is_empty("SkyEng") is False

    # Негативные тесты
    assert utils.is_empty(None) is True


def test_list_to_string():
    # Позитивные тесты
    assert utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert utils.list_to_string(["Sky", "Eng"]) == "Sky, Eng"
    assert utils.list_to_string(["Sky", "Eng"], "-") == "Sky-Eng"

    # Негативные тесты
    assert utils.list_to_string([]) == ""
