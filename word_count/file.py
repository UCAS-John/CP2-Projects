from timestamp import get_time

# Load Content
def load(file_path: str):
    """Read content from the specified file"""
    try:
        with open(file_path, 'r', newline="") as file:
            return file.read()
    except Exception as e:
        print(f"Error loading: {e}")
        return None

# Write content
def write(file_path: str, content: str) -> bool:
    try:
        with open(file_path, 'w', newline="") as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error writing: {e}")
        return False
    
# Return content without word count
def extract_main_content(content: str) -> str:
    lines = content.split('\n')
    main_lines = []
    
    for line in lines:
        # Skip lines that contain word count or timestamp 
        if not (line.strip().startswith("Word Count:") or 
                line.strip().startswith("Last Updated:")):
            main_lines.append(line)
    
    return '\n'.join(main_lines)

def process(file_path: str) -> bool:
    try:
        # Read original content
        og_content = load(file_path)
        if og_content is None:
            return False

        # Get main content without word count
        main_content = extract_main_content(og_content)
        
        # Calculate word count 
        word_count = len(main_content.split())
        
        timestamp = get_time()
        
        # Make update content
        updated_content = (
            f"{main_content}\n"
            f"Word Count: {word_count}\n"
            f"Last Updated: {timestamp}"
        )
        
        # Write updated content back to file
        success = write(file_path, updated_content)
        if success:
            print(f"\nDocument updated successfully!")
            print(f"Word Count: {word_count}")
            print(f"Timestamp: {timestamp}")
            return True
        return False
        
    except Exception as e:
        print(f"Error processing: {e}")
        return False