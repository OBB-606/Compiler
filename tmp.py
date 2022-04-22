from re import findall

input = "<head>sfssf</head><title>Rock</title>"
template = r"<title>(\w+)</title>"
print(findall(template, input))