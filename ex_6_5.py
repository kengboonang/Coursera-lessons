
text = "X-DSPAM-Confidence:    0.8475";
tf = text.find(":")
print(tf)
tz = text.find("0")
print(tz)
tme = text[tz:]
print(tme)
tyes = float(tme)
print(tyes)
