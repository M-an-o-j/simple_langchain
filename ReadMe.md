# 🤖 MCP Server – LangChain x Arduino UNO Integration

Welcome to my first step into the chaotic yet delightful world of **LangChain agents**!  
This repo is a proud (and slightly unstable) blend of:

- 🤝 FastAPI + WebSocket
- 🧠 LangChain (yes, Harrison Chase, you rock)
- 🔌 Arduino UNO (with `pyfirmata2`)
- 💡 Real-life LIGHT CONTROL using just... words. Yes, literally.

## 🌟 What Can It Do?

You say:  
> _"I want brightness in my room"_  
🌟 BOOM! The lights turn ON.

You say:  
> _"I want to cut brightness in my room"_  
🌑 BAM! The lights go OFF.

🎬 The whole thing is controlled via Swagger UI and also has a shiny ChatGPT-style frontend (because what’s an AI project without a slick chat interface, right?).

## 🧪 Tools Used (aka the Avengers lineup)

| Tool | Why It's Here |
|------|---------------|
| 🧮 Calculator | Because even robots need help with math sometimes. |
| 🎮 Paper Game | A.k.a. rock-paper-scissors showdown with a bot. |
| 👋 Greeter | Polite AI who never forgets to say hello. |
| 💡 Lights On | Tells Arduino UNO to stop being lazy and wake up the bulb. |
| 📴 Lights Off | Tells Arduino UNO to go back to sleep. |

## 🧠 LangChain Newbie Alert!

⚠️ This is my **first attempt** with **LangChain**. Inspired by Harrison Chase himself, I dove head-first into tool-using agents like a kid in a candy shop.  
(Also learned about LangGraph halfway through, but hey, next time!)

## 💡 Arduino + PyFirmata2

- Integrated a good old **Arduino UNO** using `pyfirmata2` to control physical devices like an actual light bulb.
- No simulation. It's REAL. My bulb lives in fear now.

## 💬 Live Demo (Coming Soon™️)

Planning to post a video demo where I:
1. Say something fancy on Swagger.
2. Watch the bulb light up like I just discovered fire.
3. Flex like Tony Stark in a small apartment.

## 🔌 How to Run

```bash
pip install -r requirements.txt
python main.py ```

Then open your browser and head to http://localhost:8000/docs
Swagger awaits.

Want to chat instead? The index.html is here to rescue — styled like ChatGPT, but with my DIY spirit.

🙏 Special Thanks
Harrison Chase for making LangChain usable even by over-caffeinated devs like me.

The poor Arduino UNO on my desk, forced to listen to AI drama.

And you... for reading this madness. 🌈

🛠️ More experiments coming. But first, more coffee ☕
