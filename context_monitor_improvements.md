# Context Monitor Analysis & Improvement Suggestions

## Current Issues
1. **Incorrect Token Counting**
   - Total tokens: 5,955,682 (extremely high)
   - Context usage: 111,669% (impossible percentage)
   - Session duration: 0.0 hours (despite large token count)

2. **Inappropriate File Inclusion**
   - Large data files being counted (JSON, CSV, HTML)
   - Test files included in counts
   - Scraping and utility scripts included
   - Data directories not properly excluded

## Required Changes

### 1. Configuration Updates (config.py)
Add these new settings:
```python
# Files to ignore
IGNORED_FILES = [
    "*.csv",
    "*.json",
    "*.html",
    "*.sh",
    "test_*.py",
    "*_test.py",
    "scrape_*.py",
    "collect_*.py",
    "baseball_*.json",
    "census_*.json",
    "census_*.csv",
    "baseball_*.csv",
    "baseball_*.html"
]

# Update existing IGNORED_DIRS to include:
IGNORED_DIRS = [
    "venv",
    "node_modules",
    ".git",
    "__pycache__",
    "data",
    "baseball_data",
    "census_data",
    "utils",
    "generators"
]
```

### 2. Code Updates (context_monitor.py)
Update the `update_token_counts` method to include file pattern checking:
```python
def update_token_counts(self):
    self.total_tokens = 0
    self.file_tokens.clear()
    self.session_duration = (datetime.now() - self.session_start_time).total_seconds() / 3600

    for pattern in config.FILE_PATTERNS:
        for dir_path in config.MONITORED_DIRS:
            for file_path in glob.glob(os.path.join(dir_path, pattern)):
                # Skip if file is in ignored directory
                if any(ignored in file_path for ignored in config.IGNORED_DIRS):
                    continue
                
                # Skip if file matches any ignored patterns
                if any(Path(file_path).match(ignored) for ignored in config.IGNORED_FILES):
                    continue
                
                tokens = self.count_file_tokens(file_path)
                self.file_tokens[file_path] = tokens
                self.total_tokens += tokens
```

## Additional Recommendations

### 1. Project Structure
- Keep data files in separate directories
- Use clear naming conventions
- Separate:
  - Active development code
  - Data files
  - Test files
  - Utility scripts

### 2. Future Improvements
- Add whitelist for specific files
- Implement logging for counted/ignored files
- Add debug mode for detailed token counts
- Allow custom file pattern configuration
- Add active development directory specification

### 3. Workflow Best Practices
- Maintain clear separation between code and data
- Use consistent naming patterns
- Keep test files separate from main code
- Organize utilities in dedicated directories

## Expected Results After Changes
- More accurate token counting
- Realistic context usage percentages
- Proper session duration tracking
- Focus on active development files only
- Exclusion of data and utility files 