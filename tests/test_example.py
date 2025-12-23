from hexlet_pytest.example import reverse
import pytest
import time

@pytest.fixture
def now():
    return int(time.time() * 1000)

def test_time1(now):
    print(now)

def test_time2(now):
    print(now)

@pytest.fixture
def coll():
    return [1, 2, 3, 4]


def test_first_example(coll):
    coll.append(5)
    assert coll == [1, 2, 3, 4, 5]


def test_second_example(coll):
    coll.pop()
    assert coll == [1, 2, 3]

def test_reverse():
    assert reverse("Hexlet") == "telxeH"

def test_reverse_for_empty_string():
    assert reverse("") == ""


def test_stack():
    stack = []
    # Добавляем два элемента в стек и затем извлекаем их
    # Почему два? Так надежнее, чем один, а три — уже избыточно
    stack.append("one")
    stack.append("two")

    assert stack.pop() == "two"
    assert stack.pop() == "one"

def test_emptiness():
    stack = []
    assert not stack
    stack.append("one")
    assert bool(stack)  # not not stack

    stack.pop()
    assert not stack

def test_pop_with_empty_stack():
    stack = []
    # проверить что вызывается конкретное исключение можно с помощью конструкции with pytest.raises()
    # если внутри блока вызовется исключение, то тест будет пройден
    with pytest.raises(IndexError):
        stack.pop()
@pytest.fixture()
def coll():
    return [1, 2, 3, 4]


@pytest.fixture(autouse=True)
def setup_coll(coll):
    coll[0] = "a"


def test_first_example(coll):
    assert coll == ["a", 2, 3, 4]


def test_second_example(coll):
    assert coll[0] == "a"

# def test_database(db):
#     assert is_connected(db) is True
# фикстура capsys представляет абстракцию для консольного вывода
# она перехватывает stdout и stderr, и позволяет проверять вывод программ
# именно так мы проверяли функции из начальных курсов
def hello_world():
    print('Hello, world!')


def test_output(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == 'Hello, world!\n'
