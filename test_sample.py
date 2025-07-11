import pytest
from sample import greet, farewell

def test_greet(capsys):
    greet()
    captured = capsys.readouterr()
    assert captured.out == "Hello! Welcome to the Job Seeker Assistant for Japan.\n"

def test_farewell(capsys):
    farewell()
    captured = capsys.readouterr()
    assert captured.out == "Goodbye! Have a great day.\n"


if __name__ == "__main__":
    # output all tests passed
    pytest.main([__file__])

