def add_quotation_mark(s):
    s_lines = s.split("\n")
    for line_index in range(1, len(s_lines) - 1):
        s_lines[line_index] = "\"" + s_lines[line_index] + "\"" + " - Unknown -"
    return "\n".join(s_lines)

s = """
You changed my life for the best, you bring sunshine to it, you make my everyday living with you look like paradise, you are the best wife in the world, I wish we can live together forever and never die one day. I love you with all my heart, happy 15th anniversary my beautiful wife, I pray for more astonishing years to come.

"""
print(add_quotation_mark(s))