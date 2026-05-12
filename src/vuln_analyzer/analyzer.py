from .ml_vulnerability_detector import predict_code
from .llm_analyzer import analyze_code_llm
from .secrets import detect_secrets

def analyze_code(code: str) -> dict:
    ml_result = predict_code(code)
    llm_result = analyze_code_llm(code)
    secret_result = detect_secrets(code)
    final_result = "VULNERABLE" if ml_result == "VULNERABLE" else "SAFE"
    return {
        "input": code,
        "ml_result": ml_result,
        "llm_result": llm_result,
        "final_result": final_result,
        "secrets": secret_result
    }
