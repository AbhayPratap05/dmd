import re

def format_profile(input_lines):
    """Formats profile log data from an iterable of lines."""
    output_lines = []
    
    output_lines.append("Memory Allocation Report")
    output_lines.append("=======================")
    output_lines.append("")
    output_lines.append("Bytes Allocated  | Allocations  | Type                       | Function  | File                 | Line")
    output_lines.append("-----------------+-------------+-----------------------------+-----------+----------------------+------")
    
    for line in input_lines:
        line = line.strip()
        if not line or line.startswith("bytes allocated"):
            continue
            
        # Parse line
        match = re.match(r'^\s*(\d+)\s+(\d+)\s+([^\s]+)\s+(.*):(\d+)$', line)
        if not match:
            continue
            
        bytes_alloc, allocs, type_, func_file, line_num = match.groups()
        
        # Extract function name and file path correctly
        match_func = re.match(r'^(.*)\s+([^\s]+)$', func_file)
        if match_func:
            file_path, func = match_func.groups()
        else:
            file_path = func_file
            func = "(unknown)"  # Default if function is missing

        # Ensure function name isn't a file extension (like ".d")
        if func.startswith('.') or '.' in func:
            func = "(unknown)"

        # Format output
        output_lines.append(f"{bytes_alloc:<16} | {allocs:<11} | {type_:<27} | {func:<10} | {file_path:<20} | {line_num:<4}")
    
    return output_lines

if __name__ == "__main__":
    import sys
    for line in format_profile(sys.stdin):
        print(line)