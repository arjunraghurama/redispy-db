from src.decode.decode import (
    decode_simple_string,
    decode_integer,
    decode_bulk_string,
    decode_error,
    decode_array,
    decode_resp,
)
import pytest


@pytest.mark.parametrize(
    "input,expected_output",
    [("+Hello\r\n", "Hello"), ("+OK\r\n", "OK"), ("+PONG\r\n", "PONG")],
)
def test_simple_string(input, expected_output):
    actual_output, _ = decode_simple_string(input.encode("utf-8"))
    assert actual_output == expected_output


@pytest.mark.parametrize(
    "input,expected_output",
    [(":100\r\n", 100), (":-100\r\n", -100)],
)
def test_integer(input, expected_output):
    actual_output, _ = decode_integer(input.encode("utf-8"))
    assert actual_output == expected_output


@pytest.mark.parametrize(
    "input,expected_output",
    [("$5\r\nHello\r\n", "Hello"), ("$0\r\n\r\n", "")],
)
def test_bulk_string(input, expected_output):
    actual_output, _ = decode_bulk_string(input.encode("utf-8"))
    assert actual_output == expected_output


@pytest.mark.parametrize(
    "input,expected_output",
    [("-Error\r\n", "Error")],
)
def test_error(input, expected_output):
    actual_output, _ = decode_error(input.encode("utf-8"))
    assert actual_output == expected_output


@pytest.mark.parametrize(
    "input,expected_output",
    [
        (
            "*5\r\n$3\r\nGET\r\n$5\r\nHello\r\n$3\r\nSET\r\n$3\r\nKey\r\n$5\r\nValue\r\n",
            ["GET", "Hello", "SET", "Key", "Value"],
        )
    ],
)
def test_array(input, expected_output):
    actual_output, _ = decode_array(input.encode("utf-8"))
    assert actual_output == expected_output
