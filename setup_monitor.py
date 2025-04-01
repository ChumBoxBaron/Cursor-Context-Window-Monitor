import os
import shutil
import sys
from pathlib import Path

def setup_monitor(target_dir):
    """Set up the context monitor in the specified directory."""
    # Get the directory where this script is located
    current_dir = Path(__file__).parent.absolute()
    
    # Create target directory if it doesn't exist
    target_path = Path(target_dir)
    target_path.mkdir(parents=True, exist_ok=True)
    
    # Files to copy
    files_to_copy = [
        'context_monitor.py',
        'config.py',
        'requirements.txt',
        'README.md'
    ]
    
    # Copy files
    for file in files_to_copy:
        source = current_dir / file
        if source.exists():
            shutil.copy2(source, target_path / file)
            print(f"✓ Copied {file}")
    
    print("\nSetup complete! To use the monitor:")
    print(f"1. cd {target_dir}")
    print("2. pip install -r requirements.txt")
    print("3. python context_monitor.py")
    print("\nYou can customize settings in config.py")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python setup_monitor.py <target_directory>")
        print("Example: python setup_monitor.py C:/Users/YourName/Projects/MyProject")
        sys.exit(1)
    
    target_dir = sys.argv[1]
    setup_monitor(target_dir) 