import pytest
from pytest_mock import MockerFixture

import sys

import convert

from convert import polish_letters
from convert import asci_letters

import sys

VALID_INPUT = [
    ("my_file.py", "/tmp/demo.log", "/tmp/demo.log"),
    ("my_file2.py", "/tmp/demo2.log", "/tmp/demo2.log"),
]

INVALID_INPUT = [
    ("my_file.py","",""),
    ("my_file2.py","",""),
]

@pytest.mark.parametrize("filename, args, result", VALID_INPUT)
def test_main(filename, args, result):
    sys.argv = [filename, args]
    assert convert.main() == result

@pytest.mark.parametrize("filename, args, result", INVALID_INPUT)
def test_main_fail(filename, args, result):
    sys.argv = [filename]
    with pytest.raises(SystemExit) as pytest_wrap_error:
        convert.main()
    assert pytest_wrap_error.type == SystemExit
    assert pytest_wrap_error.value.code == 1

def test_replaceLetters():
    assert convert.replaceLetters(polish_letters) == asci_letters

def test_readFile(mocker: MockerFixture):
    # Read a mocked "/tmp/foo" file data
    mocked_tmp_foo_data = mocker.mock_open(read_data="text line")
    builtin_open = "builtins.open"
    mocker.patch(builtin_open, mocked_tmp_foo_data)
    assert convert.readFile("foo") == "text line"

def test_execute(mocker: MockerFixture):
    mocked_tmp_foo_data = mocker.mock_open(read_data="text line")
    builtin_open = "builtins.open"
    mocker.patch(builtin_open, mocked_tmp_foo_data)
    assert convert.execute("foo", "foo") == "Letters converted.."
