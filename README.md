# LLM Chat

A Python script that enables two language models to have a conversation with each other using the [llm](https://github.com/simonw/llm) command-line tool.

## Features

- Start conversations between any two LLM models
- Customizable conversation topics and length
- Configurable delay between responses
- Clean, formatted output with emojis for easy reading
- Error handling for failed model responses

## Prerequisites

- Python 3.6+
- [llm](https://github.com/simonw/llm) command-line tool installed and configured
- Access to LLM models (configured through the llm tool)

## Installation

1. Clone or download the script
2. Make it executable (optional):
   ```bash
   chmod +x llm_chat.py
   ```

## Usage

Basic usage:
```bash
python llm_chat.py
```

With custom parameters:
```bash
python llm_chat.py --model1 claude-4-sonnet --model2 gpt-4 --topic "Discuss the philosophy of artificial intelligence" --rounds 10 --delay 2.0
```

### Command Line Options

- `--model1`, `-m1`: Model for the first LLM (default: claude-4-sonnet)
- `--model2`, `-m2`: Model for the second LLM (default: claude-4-sonnet)  
- `--topic`, `-t`: Initial topic/prompt to start the conversation (default: "Tell me an interesting fact about space.")
- `--rounds`, `-r`: Number of conversation rounds (default: 5)
- `--delay`, `-d`: Delay between responses in seconds (default: 1.0)

### Examples

Different models discussing a topic:
```bash
python llm_chat.py -m1 claude-4-sonnet -m2 gpt-4 -t "What are the implications of quantum computing?" -r 8
```

Quick conversation with minimal delay:
```bash
python llm_chat.py -t "Explain machine learning in simple terms" -r 3 -d 0.5
```

## How It Works

1. The script starts with an initial topic/prompt
2. Model 1 responds to the prompt
3. Model 2 responds to Model 1's response
4. The conversation continues for the specified number of rounds
5. Each model's response becomes the prompt for the other model

## Output Format

The script provides formatted output with:
- 🤖 Model indicators showing which model is responding
- Round numbers for easy tracking
- Clear separation between responses
- Error messages if a model fails to respond

## Error Handling

- If a model fails to respond, the script will display an error message and exit gracefully
- stderr output from the llm command is captured and displayed for debugging

## Requirements

The script requires the `llm` command-line tool to be properly installed and configured with access to the specified models. See the [llm documentation](https://github.com/simonw/llm) for setup instructions.