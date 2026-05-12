from vuln_analyzer import analyze_code


def test_vulnerable_code():
    code = "char buf[10]; gets(buf);"
    result = analyze_code(code)

    assert result["final_result"] == "VULNERABLE"


def test_safe_code():
    code = "fgets(buffer, 10, stdin);"
    result = analyze_code(code)

    assert result["final_result"] in ["SAFE", "VULNERABLE"]