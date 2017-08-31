def hey(string: str) -> str:
    out = ""
    if len(string.strip())==0:
        out = "Fine. Be that way!"
    elif string.lower() == string.upper(): ## full of non alpha characters
        if string.strip()[-1] == "?":
            out = "Sure."
        else:
            out = "Whatever."
    elif string.upper() == string:
        out = "Whoa, chill out!"
    elif string.strip()[-1] == "?":
        out = "Sure."
    else:
        out = "Whatever."
    return out
