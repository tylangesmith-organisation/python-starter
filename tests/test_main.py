from python_starter.config import Config
from python_starter.main import main


def test_main():
    # Arrange
    expected_result = Config.GREETING

    # Act
    result = main()

    # Assert
    assert result == expected_result
