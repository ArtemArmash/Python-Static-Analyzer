import sys
import subprocess
import json
import re

class AnalyzerFunctions:
    def __init__(self, filepath):
        self.filepath = filepath
        
    def get_file_type(self):
        result = subprocess.run(['file', self.filepath], capture_output=True, text=True)
        return result.stdout.strip().split(': ', 1)[1]
    def get_strings(self):
        result = subprocess.run(['strings', self.filepath], capture_output=True, text=True)
        file_type = result.stdout.strip().split(': ', 1)[1]
        filtered_result = [word for word in file_type.split() if len(word) >= 4]
        return "\n".join(filtered_result)
    def get_libraly_calls(self):
        result = subprocess.run(['ltrace', '-o', '/dev/stdout', self.filepath], capture_output=True, text=True)
        filtered_result = [word for word in result.stdout.splitlines()]
        return "\n".join(filtered_result)
    def get_system_calls(self):
        result = subprocess.run(['strace', self.filepath], capture_output=True, text=True)
        output = result.stderr
        calls = re.findall(r'^([a-zA-Z0-9_]+)\(', output, re.MULTILINE)
        unique_calls = list(dict.fromkeys(calls))
        return unique_calls
