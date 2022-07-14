import re


def _conv_to_float(s):

    if s == "-" or not isinstance(s, str):
        return None

    if s[0] == "(" or s[-1] == ")":
        s = s.replace("(", "")
        s = s.replace(")", "")
    if s[-1] == "%":
        s = s.replace("%", "")
    if s[-1] in list("BMK"):
        powers = {"B": 10**9, "M": 10**6, "K": 10**3, "": 1}
        m = re.search("([0-9\.]+)(M|B|K|)", s)
        if m:
            val, mag = m.group(1), m.group(2)
            return float(val) * powers[mag]
    try:
        result = float(s)
    except:
        result = None
    return result
