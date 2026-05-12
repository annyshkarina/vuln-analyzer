{\rtf1\ansi\ansicpg1251\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Vulnerability Analyzer\
\
This is a simple educational Python library for detecting code vulnerabilities using:\
\
- Classical Machine Learning (Random Forest + TF-IDF)\
- Rule-based analysis (LLM-style heuristics)\
\
## Features\
\
- Detects unsafe functions (gets, strcpy, system, eval)\
- ML-based classification of vulnerable code\
- Simple unified API\
\
## Usage\
\
```python\
from vuln_analyzer.analyzer import analyze_code\
\
code = "char buf[10]; gets(buf);"\
\
result = analyze_code(code)\
\
print(result)}