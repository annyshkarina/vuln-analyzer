from vuln_analyzer import analyze_code

if __name__ == "__main__":
    code = """
    password = "123456"
    char buf[10];
    gets(buf);
    """

    result = analyze_code(code)
    print(result)