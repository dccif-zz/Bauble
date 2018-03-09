import re

TargetRegex = r"([a-z])\1"
TuneRegex1 = r"\b(?=((([1-7])\3)(?=[,\s]{1})){1}(?!\2))\b"
TuneRegex2 = r"\b(?=((([1-7])\3)[,\s]+){1}(?!\2))\b"
# re.compile(TuneRegex2,re.DEBUG)
print(re.search(TargetRegex,"dd") != None)

re.findall(r"\bregex\b","学习 regex")
