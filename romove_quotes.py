def change_status(_status):
    if _status == "quote_started":
        _status = "quote_ended"
    else:
        _status = "quote_started"
    return _status


def delete_quote(s):
    status = "quote_ended"
    new_s = ""
    quote = ""
    for character in s:
        if character == "\"":
            status = change_status(status)
            if status == "quote_ended":
                if quote[:5] == "only_":
                    new_s += quote
                else:
                    new_s += " "
                quote = ""
            else:
                pass
            new_s += "\""
        else:
            if status == "quote_ended":
                new_s += character
            else:
                quote += character
    return new_s


with open('quote_data.txt', mode="r") as read_f:
    s = read_f.read()
result_string = delete_quote(s)

with open('quote_data_result.txt', mode="w") as write_f:
    write_f.write(result_string)
