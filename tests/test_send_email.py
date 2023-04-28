import pytest
from send_email import send_email
from unittest.mock import MagicMock

@pytest.fixture
def smtp_mock():
    mock = MagicMock()
    yield mock
    mock.quit.assert_called_once()

def test_send_email(smtp_mock):
    send_email('from@example.com', 'password', 'to@example.com', 587, True, 'Test Subject', 'Test Body', smtp_mock)

    assert smtp_mock.connect.called_once_with(('smtp.gmail.com', 587))
