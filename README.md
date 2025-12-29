# RECIPIE VISION

## Overview

This project is an **Optical Character Recognition (OCR) AI agent** built with LangGraph and LangChain that extracts text from images using vision-capable language models. The agent can process images and convert them into structured text files.

## Features

- 📸 **Image Text Extraction**: Automatically extract text from images using vision AI models
- 🤖 **LLM-Powered**: Uses Ollama (local) or OpenAI/Google Gemini (cloud) for vision capabilities
- 🔄 **Agent Architecture**: Built with LangGraph for intelligent tool orchestration
- 💾 **File Output**: Saves extracted text to organized output files
- 🛠️ **Extensible**: Easy to add new tools like temperature conversion and unit conversions

## Project Structure

```
ocr-llm-agent/
├── agent/
│   └── tools.py                    # Core extraction tool
├── additions/
│   ├── additions_1_opencv.py       # Image preprocessing (threshold, deskew)
│   ├── additions_2_temperature.py  # Temperature conversion tool
│   └── additions_3_unit_conversions.py  # Unit conversion tools
├── images/
│   └── chocolate_cake_recipe.png   # Sample input image
├── output/
│   └── extracted_text.txt          # Generated output text file
├── main.py                         # Main agent implementation
├── requirements.txt                # Python dependencies
└── description.md                  # Project documentation
```

## Installation

1. **Clone or navigate to the project:**

```bash
cd ocr-llm-agent
```

2. **Create and activate virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
   Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
```

## Usage

### Running the Agent

1. **Start Ollama (if using local models):**

```bash
ollama serve
```

2. **Run the main script:**

```bash
python main.py
```

The agent will process the image and save the extracted text to `output/extracted_text.txt`.

## Input & Output

### Input Section

**Location:** `images/` folder

Place your image files here for text extraction. The agent supports:

- PNG images
- JPG/JPEG images
- Other standard image formats

**Example:** `images/chocolate_cake_recipe.png`

### Output Section

**Location:** `output/` folder

The extracted text is automatically saved as:

- **File:** `output/extracted_text.txt`
- **Format:** Plain text with line breaks

**Example Output:**

```
Best chocolate cake recipe
Ingredients
- 2 cups all-purpose flour
- 2 cups sugar
- 3/4 cup unsweetened cocoa powder
- 2 teaspoons baking powder
...
Instructions
1. Preheat oven to 350°F...
```
