import os
from backend.server import parse_excel_file

def test_excel_parsing():
    test_files_dir = "TEST_FILES"
    
    # Get all Excel files in the test directory
    excel_files = [f for f in os.listdir(test_files_dir) 
                  if f.endswith(('.xlsx', '.xls'))]
    
    if not excel_files:
        print(f"No Excel files found in {test_files_dir}")
        return
    
    print(f"Found {len(excel_files)} Excel files for testing\n")
    
    for filename in excel_files:
        try:
            filepath = os.path.join(test_files_dir, filename)
            print(f"\nTesting file: {filename}")
            print("-" * 50)
            
            # Read the file as binary
            with open(filepath, 'rb') as f:
                file_content = f.read()
            
            # Parse the Excel file
            work_items = parse_excel_file(file_content, filename)
            
            # Print results
            print(f"Successfully parsed {len(work_items)} work items:")
            for i, item in enumerate(work_items, 1):
                print(f"\nWork Item {i}:")
                print(f"  Work No: {item.work_no}")
                print(f"  Description: {item.work_description}")
                if item.estimated_cost is not None:
                    print(f"  Estimated Cost: {item.estimated_cost}")
                if item.completion_time:
                    print(f"  Completion Time: {item.completion_time}")
                if item.location:
                    print(f"  Location: {item.location}")
                if item.category:
                    print(f"  Category: {item.category}")
            
            print("\n" + "="*50)
            
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
            print("\n" + "="*50)

if __name__ == "__main__":
    test_excel_parsing()
