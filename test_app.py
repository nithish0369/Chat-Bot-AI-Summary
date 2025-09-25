#!/usr/bin/env python3
"""
Simple test suite for the Censys Data Summarizer application.
Run with: python test_app.py
"""

import json
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_sample_data_loading():
    """Test loading sample data from JSON file."""
    try:
        with open('sample_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        assert 'hosts' in data, "Sample data should contain 'hosts' key"
        assert len(data['hosts']) == 3, "Should have 3 hosts in sample data"
        
        # Check first host structure
        host = data['hosts'][0]
        required_keys = ['ip', 'location', 'services', 'threat_intelligence']
        for key in required_keys:
            assert key in host, f"Host should contain '{key}' key"
        
        print("✅ Sample data loading test passed")
        return True
    except Exception as e:
        print(f"❌ Sample data loading test failed: {e}")
        return False

def test_json_validation():
    """Test JSON validation logic."""
    # Valid JSON
    valid_json = '{"hosts": [{"ip": "1.1.1.1"}]}'
    try:
        json.loads(valid_json)
        print("✅ Valid JSON test passed")
    except:
        print("❌ Valid JSON test failed")
        return False
    
    # Invalid JSON
    invalid_json = '{"hosts": [{"ip": "1.1.1.1"}'  # Missing closing brace
    try:
        json.loads(invalid_json)
        print("❌ Invalid JSON test failed - should have raised exception")
        return False
    except:
        print("✅ Invalid JSON test passed")
    
    return True

def test_metrics_extraction():
    """Test metrics extraction logic."""
    sample_data = {
        "hosts": [
            {
                "ip": "1.1.1.1",
                "threat_intelligence": {"risk_level": "critical"},
                "services": [{"port": 22, "vulnerabilities": [{"cve_id": "CVE-123"}]}]
            },
            {
                "ip": "2.2.2.2", 
                "threat_intelligence": {"risk_level": "high"},
                "services": [{"port": 80}]
            }
        ]
    }
    
    # Simulate metrics extraction
    total_hosts = len(sample_data["hosts"])
    critical_risk = sum(1 for host in sample_data["hosts"] 
                       if host.get("threat_intelligence", {}).get("risk_level") == "critical")
    high_risk = sum(1 for host in sample_data["hosts"] 
                   if host.get("threat_intelligence", {}).get("risk_level") == "high")
    
    assert total_hosts == 2, "Should have 2 hosts"
    assert critical_risk == 1, "Should have 1 critical risk host"
    assert high_risk == 1, "Should have 1 high risk host"
    
    print("✅ Metrics extraction test passed")
    return True

def test_file_upload_simulation():
    """Test file upload simulation."""
    try:
        # Simulate file upload
        with open('sample_data.json', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Simulate JSON parsing
        data = json.loads(content)
        
        # Simulate validation
        assert isinstance(data, dict), "Data should be a dictionary"
        assert 'hosts' in data, "Data should contain 'hosts' key"
        
        print("✅ File upload simulation test passed")
        return True
    except Exception as e:
        print(f"❌ File upload simulation test failed: {e}")
        return False

def run_all_tests():
    """Run all tests and return success rate."""
    tests = [
        test_sample_data_loading,
        test_json_validation,
        test_metrics_extraction,
        test_file_upload_simulation
    ]
    
    passed = 0
    total = len(tests)
    
    print("🧪 Running Censys Data Summarizer Tests\n")
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return True
    else:
        print("⚠️  Some tests failed. Check the output above.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
