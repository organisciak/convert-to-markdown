# /// script
# dependencies = [
#     "markitdown",
#     "openai",
#     "python-dotenv",
# ]
# ///
#!/Users/peter.organisciak/anaconda3/bin python
# This script converts various filetypes to a markdown file, 
# saved in the same directory as the input file.
#
# OpenAI API key is loaded from the .env file. This is used for transcribing images.
#
# Quick Action Instructions:
# It is useful with Mac OS Quick Actions, where you can select a file and 
# then select this script as the action.
# To set up a quick action, go to Automator, create a new quick action with the
# following settings:
# Workflow receives: files or folder in Finder
# Action is 'Run Shell Script'
# The shell script:
# for f in "$@"
# do
#     /path/to/convert-to-markdown/.venv/bin/python /path/to/convert-to-markdown/convert_to_md.py "$f"
# done
# The --compile-bytecode flag is not needed for normal use, but is recommended
# The --fast flag is used to skip image transcription. Useful to have a second quick action with it.
import sys
from pathlib import Path
import argparse
from openai import OpenAI
from dotenv import load_dotenv
from markitdown import MarkItDown

# Load environment variables early
load_dotenv()

def convert_by_file_name(file_name: Path, fast_mode=False, suffix=None):
    if not file_name.exists():
        print(f"File {file_name} does not exist")
        sys.exit(1)

    if file_name.is_dir():
        print(f"Input {file_name} is a directory")
        sys.exit(1)

    # Use provided suffix or default based on mode
    if suffix is None:
        suffix = '_converted_fast' if fast_mode else '_converted'
    
    output_file = file_name.with_stem(file_name.stem + suffix).with_suffix(".md")
    
    # Initialize MarkItDown with or without image transcription
    if fast_mode:
        md = MarkItDown()  # Fast mode - no image transcription
    else:
        client = OpenAI()
        md = MarkItDown(llm_client=client, llm_model="gpt-4o-mini")  # Default mode with image transcription
    
    try:
        # Convert the file
        result = md.convert(str(file_name))
        
        # Write the result to file
        with open(output_file, 'w', encoding='utf-8') as md_file:
            md_file.write(result.text_content)
        
        print(f"Converted {file_name} to {output_file}")
    except Exception as e:
        print(f"Error converting {file_name}: {str(e)}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Convert files to markdown')
    parser.add_argument('input_file', help='File to convert')
    parser.add_argument('--fast', action='store_true', help='Fast mode - skip image transcription')
    parser.add_argument('--suffix', type=str, help='Custom suffix for output filename (default: "_converted" or "_converted_fast")')
    
    args = parser.parse_args()
    input_file = Path(args.input_file)
    
    convert_by_file_name(input_file, fast_mode=args.fast, suffix=args.suffix)
    
if __name__ == "__main__":
    main()
