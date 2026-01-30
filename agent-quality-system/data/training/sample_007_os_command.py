# sample_007_os_command.py - Command injection risk, should FAIL vuln gate

import os
import subprocess

def run_user_command(command):
    """Dangerous: runs arbitrary user commands"""
    os.system(command)

def execute_with_shell(args):
    """Dangerous: shell=True allows command injection"""
    result = subprocess.run(args, shell=True, capture_output=True)
    return result.stdout

def list_directory(path):
    """Uses os.system dangerously"""
    os.system(f"ls -la {path}")
