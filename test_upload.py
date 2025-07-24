import requests
import os

def test_upload():
    url = "http://localhost:8000/api/tender-notices/upload-excel"
    
    # Path to the test file
    file_path = "TEST_FILES/NIT_1 work.xlsx"
    
    # Prepare the file data
    files = {
        'file': ('NIT_1 work.xlsx', open(file_path, 'rb'), 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    }
    
    # Additional form data
    data = {
        'tender_no': 'TEST_001',
        'notice_title': 'Test Tender from Script',
        'organization': 'Test Organization',
        'publication_date': '2025-07-24',
        'last_date_submission': '2025-08-24'
    }
    
    try:
        # Make the POST request
        response = requests.post(url, files=files, data=data)
        
        # Print the response
        print(f"Status Code: {response.status_code}")
        print("Response:")
        print(response.json())
        
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Make sure to close the file
        if 'files' in locals():
            files['file'][1].close()

if __name__ == "__main__":
    test_upload()
