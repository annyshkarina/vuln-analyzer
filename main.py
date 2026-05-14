from vuln_analyzer import analyze_code

def run():
    code = '''
password = "123456"
token = "ghp_abcdef123456"
char buf[10];
gets(buf);
'''

    result = analyze_code(code)
    print(result)

if __name__ == "__main__":
    run()