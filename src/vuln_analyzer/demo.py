from vuln_analyzer import analyze_code

code = "char buf[10]; gets(buf);"

result = analyze_code(code)

print(result)
