# Context Window Monitor

This tool helps you monitor your AI chat sessions and alerts you when you're approaching the context window limit. It's particularly useful for developers using AI coding assistants like Cursor.

## Features

- Real-time monitoring of chat sessions
- Token counting and context window usage tracking
- Visual alerts when approaching context limits
- Workspace management (tabs and terminals tracking)
- Platform-specific optimizations (Windows, macOS, Linux)
- Smart file filtering to exclude data and test files
- Session duration tracking
- Context-aware recommendations

## Setup

1. Install Python 3.8 or higher
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the monitor:
   ```bash
   python context_monitor.py
   ```

2. The tool will start monitoring and display:
   - Current token count
   - Context window usage percentage
   - Number of open tabs and terminals
   - Session duration
   - Smart recommendations for context management
   - Visual alerts when approaching limits

## Configuration

You can customize the following in `config.py`:

### Context Window Settings
- Warning threshold (default: 70% of context window)
- Critical threshold (default: 85% of context window)
- Context window size (default: 128000 tokens for GPT-4)

### File Management
- File patterns to monitor (default: `*.py`, `*.md`, `*.txt`)
- Directories to ignore (e.g., `venv`, `node_modules`, `data`)
- File patterns to ignore (e.g., `*.csv`, `*.json`, `test_*.py`)

### Workspace Management
- Maximum recommended open tabs (default: 5)
- Maximum recommended open terminals (default: 2)
- Session duration warning (default: 2 hours)

## Platform Support

The tool automatically adapts to your operating system:

- **Windows**: Uses `tasklist` to monitor terminals and VS Code windows
- **macOS**: Uses AppleScript to monitor Terminal and VS Code windows
- **Linux**: Uses `wmctrl` to monitor terminals and VS Code windows

## Best Practices for Context Management

1. **Session Management**
   - Start new sessions for major features or components
   - Consider starting a new session after 2+ hours of work
   - Start new chats when switching between different tasks

2. **Workspace Organization**
   - Keep data files in separate directories
   - Use clear naming conventions
   - Separate active development code from test files
   - Organize utilities in dedicated directories

3. **Resource Management**
   - Close unused tabs and terminals
   - Split large files into smaller modules
   - Keep your workspace clean and organized

4. **File Organization**
   - Save important code snippets and decisions in separate files
   - Use comments to document key decisions
   - Maintain clear separation between code and data

## Troubleshooting

If you encounter issues with tab or terminal counting:
1. Ensure you have the necessary permissions
2. Check if your terminal/editor is supported
3. The tool will continue working even if counting fails

## Contributing

Feel free to contribute by:
1. Adding support for more editors/terminals
2. Improving platform-specific implementations
3. Adding new features or optimizations 