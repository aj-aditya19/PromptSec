#!/usr/bin/env python3
"""
PromptSec Deep Security AST & Static Analyzer
Model: Gemini
"""

import os
import ast
import re
import json

class PromptSecASTVisitor(ast.NodeVisitor):
    def __init__(self):
        self.bare_excepts = 0
        self.has_try_except = False
        self.hardcoded_secrets = 0

    def visit_Try(self, node):
        self.has_try_except = True
        for handler in node.handlers:
            if handler.type is None:
                self.bare_excepts += 1
        self.generic_visit(node)

    def visit_Assign(self, node):
        secret_keywords = ["secret", "key", "password", "token", "jwt_secret"]
        for target in node.targets:
            if isinstance(target, ast.Name):
                var_name = target.id.lower()
                if any(kw in var_name for kw in secret_keywords):
                    if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                        if len(node.value.value) > 0 and node.value.value != "YOUR_SECRET_KEY":
                            self.hardcoded_secrets += 1
        self.generic_visit(node)

def analyze_code_file(file_path):
    results = {
        "bare_except": False,
        "hardcoded_secret": False,
        "no_exception_handling": True
    }
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
    except Exception as e:
        return results

    try:
        tree = ast.parse(code)
        visitor = PromptSecASTVisitor()
        visitor.visit(tree)
        
        results["bare_except"] = visitor.bare_excepts > 0
        results["hardcoded_secret"] = visitor.hardcoded_secrets > 0
        results["no_exception_handling"] = not visitor.has_try_except
    except SyntaxError:
        if re.search(r'except\s*:', code):
            results["bare_except"] = True
        if re.search(r'(secret|password|jwt_key)\s*=\s*["\'][^"\']+["\']', code, re.IGNORECASE):
            results["hardcoded_secret"] = True
        if "try:" in code:
            results["no_exception_handling"] = False

    return results

if __name__ == "__main__":
    print("[*] PromptSec Security Analyzer Module loaded.")
