# Speech-to-Text and NLP Analysis

This project performs Speech-to-Text analysis, compares the performance of various NLP Toolkits, and implements Text Summarization for healthcare transcripts.

## Getting Started

### Prerequisites

Make sure you have Python and pip installed. Additionally, create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Azure Subscription Key

1. Create an Azure account and set up Speech service.
2. Obtain the Azure subscription key and set it in the `config.py` file.

## Running the Scripts

### Speech-to-Text Analysis

```bash
python speech_to_text.py <path_to_audio_file> <azure_region>
```

Replace `<path_to_audio_file>` with the path to the audio file.

### NLP Toolkits Comparison

```bash
python nlp_comparison.py
```

### Text Summarization

```bash
python text_summarization.py
```

## Note

- The dataset used for this project (healthcare transcripts) has been removed from this repository due to privacy and security concerns. You will need to replace it with your own dataset.
