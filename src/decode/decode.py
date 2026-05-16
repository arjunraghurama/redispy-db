def decode_length_prefix(data: bytes):
    pos = 1
    while pos < len(data) and data[pos] != ord("\r"):
        pos += 1
    return int(data[1:pos]), pos + 2


def decode_simple_string(data: bytes):
    pos = 1
    while pos < len(data) and data[pos] != ord("\r"):
        pos += 1
    return data[1:pos].decode("utf-8"), pos + 2


def decode_bulk_string(data: bytes):
    length, pos = decode_length_prefix(data)
    return data[pos : pos + length].decode("utf-8"), pos + length + 2


def decode_error(data: bytes):
    pos = 1
    while pos < len(data) and data[pos] != ord("\r"):
        pos += 1
    return data[1:pos].decode("utf-8"), pos + 2


def decode_integer(data: bytes):
    pos = 1
    while pos < len(data) and data[pos] != ord("\r"):
        pos += 1
    return int(data[1:pos]), pos + 2


def decode_array(data: bytes):
    length, pos = decode_length_prefix(data)
    # store only the commands
    result = []
    for _ in range(length):
        val, step = decode_resp(data[pos:])
        result.append(val)
        pos += step
    return result, pos


def decode_resp(data: bytes):
    if len(data) == 0:
        raise ValueError("No data received")

    if data[0] == ord("+"):
        return decode_simple_string(data)
    elif data[0] == ord("-"):
        return decode_error(data)
    elif data[0] == ord(":"):
        return decode_integer(data)
    elif data[0] == ord("$"):
        return decode_bulk_string(data)
    elif data[0] == ord("*"):
        return decode_array(data)
    else:
        raise ValueError(f"Unknown data type, {chr(data[0])}")
