# 🤖 MCP Agent - Modular Conversational Protocol Server

Welcome to the **MCP Agent**, your AI-powered multitool sidekick that talks, calculates, plays games, and even controls real-world lights! 🌍💡

> Think of it like **Jarvis**, but still in beta... and sometimes emotionally unstable.

---

## 🎯 What It Does (a.k.a. Why This Exists)

MCP is an AI agent with a modular brain 🧠 that can:
- 🧮 Solve math problems without crying
- 🎮 Play Rock-Paper-Scissors and *usually* lose
- 🗣️ Say hi like a socially awkward chatbot
- 💡 Turn lights on and off like a polite ghost
- 🧰 Expand with new tools because it has commitment issues

---

## 🔌 Features

| Tool Name   | Purpose                            | AI’s Mood When Using It        |
|------------|-------------------------------------|--------------------------------|
| `Greeter`  | Says hello to humans                | 😃 Friendly but clingy         |
| `Calculator` | Evaluates math expressions         | 🤓 Nerd mode activated         |
| `Paper Game` | Rock-Paper-Scissors with attitude | 🎲 RNGesus takes the wheel     |
| `Lights On` | Turns on Arduino LED               | ⚡ It’s alive!                 |
| `Lights Off` | Turns off Arduino LED              | 😴 Night night, light          |

---

## 🧠 Tech Stack

- 🦜 `LangChain` for thinking like a human (but faster)
- 🤖 `OpenRouter` for LLM access (GPT-powered brain goo)
- 🔌 `pyfirmata2` to talk to Arduino (it speaks fluent blinking)
- ⚡ `FastAPI` to expose the brain to the internet
- 🧼 Codebase clean enough to eat off (but don’t)

---

## 🗺️ API Route

```http
POST /ask

How to Run (a.k.a. Bring Frankenstein to Life)

# 1. Install the dependencies
pip install -r requirements.txt

# 2. Plug in your Arduino (yes, really)
# 3. Set your OpenRouter API key
export OPENROUTER_API_KEY=your_key_here

# 4. Start the mind of MCP
uvicorn main:app --reload

⚠️ Disclaimer
This AI might win at rock-paper-scissors, but it is not responsible for any emotional damage caused by losing.

🧞 Future Features (or "Stretch Goals Because Why Not")
🗺️ Ask for weather, because AI needs to feel the vibe outside

🧏 Voice commands, so you can talk like Iron Man

🤡 Joke generator, because this README isn't enough

🧠 Memory, because even robots forget things sometimes

🧔 About the Author
Built by someone who:

Wanted a smart assistant.

Ended up with a light switch that tells jokes.