# vuln-analyzer

![CI](https://github.com/USERNAME/REPO/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue)

## Description
A simple Python security analysis library that detects vulnerable code using ML, rule-based patterns, and secret scanning.

## Install
pip install vuln-analyzer

## Usage
from vuln_analyzer import analyze_code

print(analyze_code("char buf[10]; gets(buf);"))
