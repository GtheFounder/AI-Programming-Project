# AI Programming Project

## 👤 Student Information
| Field | Details |
|-------|---------|
| **Full Name** | Godfrey Nduati |
| **Registration Number** | 251835DAI |
| **Course** | Artificial Intelligence Programming |
| **Assessment** | CAT 2 |

---

## 📌 Project Title
**AI Course Assistant Bot — Rule-Based Chatbot**

## 📝 Short Description
A rule-based conversational chatbot built in Python that answers
Frequently Asked Questions (FAQs) about Artificial Intelligence,
Machine Learning, Python programming, GitHub/Git workflow,
and university-related queries.

The bot uses **keyword matching and if-else logic** — no machine learning
libraries are required. It demonstrates core Python programming concepts
including functions, loops, lists of dictionaries, and the `re` module.

---

## 🤖 Supported Intents (9 Total)
| # | Intent | Example Trigger |
|---|--------|----------------|
| 1 | Greeting | "Hello", "Hi", "Hey" |
| 2 | What is AI | "What is AI?", "Define artificial intelligence" |
| 3 | Machine Learning | "Explain machine learning", "What is ML?" |
| 4 | Deep Learning | "What is deep learning?", "neural networks" |
| 5 | Python Help | "Python libraries", "how to fix error" |
| 6 | Assignment Help | "CAT 2 tips", "how to submit project" |
| 7 | GitHub & Git | "git commit", "how to push to GitHub" |
| 8 | University Info | "exam timetable", "registration", "fees" |
| 9 | Farewell | "bye", "exit", "thank you" |

---

## 🐍 Python Libraries Used
| Library | Purpose | Built-in? |
|---------|---------|-----------|
| `re` | Regular expressions for text cleaning | ✅ Yes (no install needed) |

> No external libraries required! Pure Python 3.


### Example Interaction
```
You: hello
Bot: Hello! 👋 Welcome to the AI Course Assistant Bot...

You: what is machine learning?
Bot: 📊 Machine Learning (ML) is a subset of AI...

You: bye
Bot: 👋 Goodbye! Best of luck with your AI studies...
```

---

## 📁 Project Structure
```
AI_Programming_Project/
│
├── ai_chatbot.py      # Main chatbot source code
└── README.md          # Project documentation (this file)
```

---

## 💡 How the Bot Works (Technical Overview)
```
User Input
    ↓
Lowercase + Remove Punctuation (re module)
    ↓
Loop through all INTENTS
    ↓
Does any keyword appear in user input?
    ↓ YES              ↓ NO
Return response    Return fallback message
```