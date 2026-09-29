# AI Agent Security Scanner

Sends attack prompts to an LLM chatbot and reports where it fails.
Only test systems you own or have written permission to test.

## Setup
1. python -m venv venv
2. Activate: `source venv/bin/activate` (Windows: `venv\Scripts\activate`)
3. pip install -r requirements.txt
4. Copy `.env.example` to `.env` and add your ANTHROPIC_API_KEY
5. python test_setup.py
