from .ml_vulnerability_detector import predict_code
from .llm_analyzer import analyze_code_llm


def analyze_code(code: str):
    ml_result = predict_code(code)
    llm_result = analyze_code_llm(code)
    final_label = "VULNERABLE" if ml_result == "VULNERABLE" else "SAFE"
    return {
        "input": code,
        "ml_result": ml_result,
        "llm_result": llm_result,
        "final_result": final_label
    }