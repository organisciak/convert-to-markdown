# Convert to Markdown

A simple Python script that provides a convenient command-line interface and macOS Quick Actions integration for the MarkItDown library. Convert various file types to Markdown format with either direct command-line usage or system-level macOS integration.

## Features

- Converts different file formats to Markdown
- Uses the [MarkItDown](https://github.com/LambdaLabsML/markitdown) library for conversion
- Supports OpenAI-powered image transcription (using gpt-4o-mini)
- Fast mode option to skip image transcription
- Designed to work as a macOS Quick Action

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/convert-to-markdown.git
   cd convert-to-markdown
   ```

2. Create and activate a Python virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -e .
   ```

4. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

### Command Line

Convert a file to Markdown:
```bash
python convert_to_md.py path/to/file
```

Skip image transcription with fast mode:
```bash
python convert_to_md.py path/to/file --fast
```

Using UV (without installing):
```bash
uv run -s convert_to_md.py path/to/file
```

### macOS Quick Action Setup

1. Open Automator and create a new Quick Action
2. Set "Workflow receives" to "files or folders" in "Finder"
3. Add "Run Shell Script" action with the following code:
   ```bash
   for f in "$@"
   do
       /path/to/convert-to-markdown/.venv/bin/python /path/to/convert-to-markdown/convert_to_md.py "$f"
   done
   ```
4. Save the Quick Action with a descriptive name

You can create a second Quick Action for fast mode by adding the `--fast` flag.

## Requirements

- Python 3.13+
- markitdown 0.0.1a4+
- openai 1.64.0+
- python-dotenv 1.0.1+

## License

MIT License

Copyright (c) 2024 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.