#!/usr/bin/python3
import urllib.request
import urllib.error
import json
import sys

# Base URL for the API
BASE_URL = "http://localhost:8000"

class Response:
    """Simple response class to mimic requests.Response"""
    def __init__(self, data, status_code, headers):
        self.text = data.decode('utf-8') if isinstance(data, bytes) else data
        self.status_code = status_code
        self.headers = headers
    
    def json(self):
        return json.loads(self.text)

def test_endpoint(endpoint, expected_status=200, expected_content_type=None):
    """Test a specific endpoint and return the response."""
    try:
        url = f"{BASE_URL}{endpoint}"
        request = urllib.request.Request(url)
        
        try:
            with urllib.request.urlopen(request) as response:
                data = response.read()
                status_code = response.getcode()
                headers = dict(response.headers)
        except urllib.error.HTTPError as e:
            data = e.read()
            status_code = e.code
            headers = dict(e.headers)
        
        response_obj = Response(data, status_code, headers)
        
        print(f"Testing {endpoint}:")
        print(f"  Status Code: {response_obj.status_code} (Expected: {expected_status})")
        
        if expected_content_type:
            content_type = response_obj.headers.get('content-type', '')
            print(f"  Content-Type: {content_type} (Expected: {expected_content_type})")
        
        print(f"  Response: {response_obj.text}")
        
        if response_obj.status_code == expected_status:
            print(f"  ✅ PASS")
        else:
            print(f"  ❌ FAIL")
        
        print()
        return response_obj
        
    except urllib.error.URLError:
        print(f"❌ ERROR: Could not connect to {BASE_URL}{endpoint}")
        print("Make sure the server is running on localhost:8000")
        return None
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return None

def test_json_endpoint(endpoint, expected_keys=None):
    """Test an endpoint that should return JSON."""
    response = test_endpoint(endpoint, expected_content_type="application/json")
    if response and response.status_code == 200:
        try:
            data = response.json()
            print(f"  JSON Data: {json.dumps(data, indent=2)}")
            
            if expected_keys:
                missing_keys = [key for key in expected_keys if key not in data]
                if missing_keys:
                    print(f"  ❌ Missing keys: {missing_keys}")
                else:
                    print(f"  ✅ All expected keys present: {expected_keys}")
        except json.JSONDecodeError:
            print(f"  ❌ Response is not valid JSON")
        print()
    return response

def main():
    """Run all tests."""
    print("=" * 50)
    print("Testing Simple API HTTP Server")
    print("=" * 50)
    print()
    
    # Test root endpoint
    test_endpoint("/")
    
    # Test data endpoint
    test_json_endpoint("/data", expected_keys=["name", "age", "city"])
    
    # Test status endpoint
    test_json_endpoint("/status", expected_keys=["message"])
    
    # Test info endpoint
    test_json_endpoint("/info", expected_keys=["version", "description"])
    
    # Test 404 endpoint
    test_endpoint("/nonexistent", expected_status=404, expected_content_type="application/json")
    
    print("=" * 50)
    print("Testing completed!")
    print("=" * 50)

if __name__ == "__main__":
    main()

