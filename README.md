# Context Window Monitor

This tool helps you monitor your AI chat sessions and alerts you when you're approaching the context window limit. It's particularly useful for developers using AI coding assistants like Cursor.

## Features

- Real-time monitoring of chat sessions
- Token counting and context window usage tracking
- Visual alerts when approaching context limits
- Suggestions for managing context

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

2. The tool will start monitoring your chat sessions and display:
   - Current token count
   - Context window usage percentage
   - Alerts when approaching limits
   - Suggestions for managing context

## Configuration

You can customize the following in `config.py`:
- Warning threshold (default: 80% of context window)
- Critical threshold (default: 90% of context window)
- Context window size (default: 8000 tokens)

## Tips for Managing Context

1. Start new sessions for major features or components
2. Save important code snippets and decisions in separate files
3. Use comments to document key decisions
4. Consider splitting large files into smaller modules 