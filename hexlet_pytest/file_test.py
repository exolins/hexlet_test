from hexlet_pytest.example import reverse
from pathlib import Path
def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


# тестируем функцию process(), которая как-то обрабатывает файл
def test_process():
    before_html = read_file("before.txt")
    expected = read_file("result.txt")
    actual = reverse(before_html)

    assert actual == expected
