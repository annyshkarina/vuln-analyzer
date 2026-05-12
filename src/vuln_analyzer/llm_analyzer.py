def analyze_code_llm(code):
    issues = []
    if "gets(" in code:
        issues.append("Buffer Overflow: gets() is unsafe")
    if "strcpy" in code:
        issues.append("Buffer Overflow: strcpy has no bounds checking")
    if "system(" in code:
        issues.append("Command Injection risk via system()")
    if "eval(" in code:
        issues.append("Code Injection risk via eval()")
    if "scanf('%s'" in code:
        issues.append("Input overflow risk via scanf")
    if "fgets" in code:
        issues.append("Safe input function detected: fgets")
    if "strncpy" in code:
        issues.append("Safer alternative used: strncpy")
    if not issues:
        return "No obvious vulnerabilities detected"
    return "\n".join(issues)

if __name__ == "__main__":
    code = "char buf[10]; gets(buf);"
    print("=== LLM analysis ===")
    print(analyze_code_llm(code))