from vuln_analyzer.analyzer import analyze_code

code = "char buf[10]; gets(buf);"

result = analyze_code(code)

print("\n======================")
print("Input code:")
print(code)

print("\n======================")
print("Analysis result:")
print(result)