import pytest

@pytest.fixture
def set_up():
   print("Вход в систему выполнен")
   yield
   print('Произведен выход из системы')


@pytest.fixture(scope='module')
def some():
   print("Начало")
   yield
   print('Конец')


@pytest.fixture(scope='function')
def same():
   print("Начало")
   yield
   print('Конец')