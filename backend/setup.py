#!/usr/bin/env python3
"""
Setup script for RogChat
This script helps set up the environment and run initial checks
"""

import sys
import subprocess
import importlib.util

def check_python_version():
    """Check if Python version is sufficient"""
    if sys.version_info < (3, 7):
        print("[ERROR] Python 3.7 or higher is required")
        return False
    print(f"[OK] Python version {sys.version_info} is sufficient")
    return True

def check_dependencies():
    """Check if required dependencies are installed"""
    required_packages = [
        'requests',
        'trafilatura',
        'qdrant_client',
        'cohere',
        'xmltodict'
    ]

    missing_packages = []
    for package in required_packages:
        if importlib.util.find_spec(package) is None:
            missing_packages.append(package)

    if missing_packages:
        print(f"[ERROR] Missing packages: {', '.join(missing_packages)}")
        print("Run: pip install -e .")
        return False

    print("[OK] All required packages are installed")
    return True

def run_tests():
    """Run basic import tests"""
    tests = [
        ("config", "from config import *"),
        ("main", "from main import *"),
        ("chat", "from chat import *"),
    ]

    print("\nRunning import tests...")
    for module_name, import_stmt in tests:
        try:
            exec(import_stmt)
            print(f"[OK] {module_name} module imported successfully")
        except Exception as e:
            print(f"[ERROR] {module_name} module failed to import: {e}")
            return False

    return True

def main():
    print("RogChat Setup Script")
    print("=" * 30)

    if not check_python_version():
        return False

    if not check_dependencies():
        return False

    if not run_tests():
        return False

    print("\nAll checks passed! RogChat is ready to use.")
    print("\nTo start using RogChat:")
    print("  - To ingest content: python main.py ingest")
    print("  - To start chat: python main.py chat")

    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)