from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()
r = client.messages.create(
    model="claude-sonnet-4-6", max_tokens=50,
    messages=[{"role": "user", "content": "Say 'setup works'"}])
print(r.content[0].text)
