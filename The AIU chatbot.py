"""
AI Course Assistant Bot — Rule-Based Chatbot
Author: Godfrey Nduati
Reg No: 251835DAI
Description: A rule-based chatbot that answers FAQs about AI and university life.
"""

# ─────────────────────────────────────────────
# WHAT IS A RULE-BASED CHATBOT?
# It works using IF-ELSE logic and keyword matching.
# No machine learning is involved — it scans the user's
# input for known keywords and returns a pre-written response.
# ─────────────────────────────────────────────

import re  # 're' is Python's regular expressions library — used for pattern matching


# ── INTENT DEFINITIONS ──────────────────────────────────────────────────────
# Each intent has:
#   "keywords" : words we look for in the user's message
#   "response" : what the bot replies

INTENTS = [
    {
        "intent": "greeting",
        "keywords": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening", "howdy"],
        "response": (
            "Hello! 👋 Welcome to the AI Course Assistant Bot.\n"
            "I can help you with:\n"
            "  1. What is AI?\n"
            "  2. Machine Learning concepts\n"
            "  3. Deep Learning\n"
            "  4. Assignment & CAT help\n"
            "  5. Python programming tips\n"
            "  6. University registration\n"
            "  7. Exam timetable\n"
            "Just type your question!"
        )
    },
    {
        "intent": "what_is_ai",
        "keywords": ["what is ai", "define ai", "artificial intelligence", "what is artificial", "explain ai", "ai meaning"],
        "response": (
            "🤖 Artificial Intelligence (AI) is the simulation of human intelligence\n"
            "in machines programmed to think, learn, and problem-solve.\n\n"
            "Key branches of AI:\n"
            "  • Machine Learning (ML) — learning from data\n"
            "  • Deep Learning (DL)   — neural networks with many layers\n"
            "  • NLP                  — understanding human language\n"
            "  • Computer Vision      — interpreting images/video\n\n"
            "Real-world examples: ChatGPT, Google Search, M-PESA fraud detection."
        )
    },
    {
        "intent": "machine_learning",
        "keywords": ["machine learning", "ml", "supervised", "unsupervised", "regression", "classification", "clustering"],
        "response": (
            "📊 Machine Learning (ML) is a subset of AI where machines learn\n"
            "patterns from data WITHOUT being explicitly programmed.\n\n"
            "Types of ML:\n"
            "  1. Supervised Learning   — labelled data (e.g. spam detection)\n"
            "  2. Unsupervised Learning — no labels (e.g. customer segmentation)\n"
            "  3. Reinforcement Learning— learns by reward/penalty (e.g. game bots)\n\n"
            "Common algorithms: Linear Regression, Decision Trees, KNN, SVM."
        )
    },
    {
        "intent": "deep_learning",
        "keywords": ["deep learning", "neural network", "cnn", "rnn", "lstm", "transformer", "deep"],
        "response": (
            "🧠 Deep Learning uses Artificial Neural Networks (ANNs) with\n"
            "multiple layers (hence 'deep') to model complex patterns.\n\n"
            "Popular architectures:\n"
            "  • CNN  — image recognition\n"
            "  • RNN/LSTM — sequences & text\n"
            "  • Transformers — ChatGPT, BERT\n\n"
            "Libraries: TensorFlow, PyTorch, Keras\n"
            "Deep Learning requires large datasets and GPUs to train."
        )
    },
    {
        "intent": "python_help",
        "keywords": ["python", "code", "programming", "syntax", "error", "library", "pip", "import", "function", "loop"],
        "response": (
            "🐍 Python Tips for AI Programming:\n\n"
            "  Key Libraries:\n"
            "  • numpy     — numerical computations\n"
            "  • pandas    — data manipulation\n"
            "  • matplotlib— data visualization\n"
            "  • sklearn   — machine learning models\n"
            "  • tensorflow/pytorch — deep learning\n\n"
            "  Install with: pip install numpy pandas matplotlib scikit-learn\n\n"
            "  Common mistake: IndentationError means your spacing is off.\n"
            "  Python uses 4 spaces (not tabs) for indentation."
        )
    },
    {
        "intent": "assignment_help",
        "keywords": ["assignment", "cat", "project", "submit", "deadline", "marks", "report", "task", "cat2", "coursework"],
        "response": (
            "📝 Assignment & CAT Advice:\n\n"
            "  For this CAT 2, make sure you:\n"
            "  ✅ Create a public GitHub repo named 'AI_Programming_Project'\n"
            "  ✅ Write a detailed README.md (name, reg no, description)\n"
            "  ✅ Make at least 3 commits with clear messages\n"
            "  ✅ Build a rule-based chatbot with 5+ intents\n"
            "  ✅ Include screenshots of git add, commit, push\n\n"
            "  Pro tip: commit after each major change — don't commit everything at once!"
        )
    },
    {
        "intent": "github_git",
        "keywords": ["github", "git", "commit", "push", "repository", "repo", "clone", "branch", "readme"],
        "response": (
            "🐙 Git & GitHub Quick Guide:\n\n"
            "  Setup commands:\n"
            "    git init                    # initialise a repo\n"
            "    git add .                   # stage all files\n"
            "    git commit -m 'message'     # save a snapshot\n"
            "    git remote add origin URL   # link to GitHub\n"
            "    git push -u origin main     # upload to GitHub\n\n"
            "  Good commit messages:\n"
            "    ✅ 'Initial setup: add README and project structure'\n"
            "    ✅ 'feat: add chatbot greeting and AI intents'\n"
            "    ❌ 'update' or 'fix stuff'"
        )
    },
    {
        "intent": "university_info",
        "keywords": ["university", "registration", "timetable", "exam", "lecture", "unit", "fee", "portal", "student"],
        "response": (
            "🎓 University Information:\n\n"
            "  • Registration: Visit the student portal or registrar's office.\n"
            "  • Exam Timetable: Check your university's official website.\n"
            "  • Fee Payment: Use the designated payment channels.\n"
            "  • Lecture Schedules: Confirm with your class rep or department.\n\n"
            "  For urgent issues, visit the Student Affairs office directly.\n"
            "  Remember: deadlines are strict — plan ahead! 📅"
        )
    },
    {
        "intent": "farewell",
        "keywords": ["bye", "goodbye", "exit", "quit", "see you", "later", "thanks", "thank you"],
        "response": (
            "👋 Goodbye! Best of luck with your AI studies and CAT 2!\n"
            "Remember: consistency beats cramming. Keep coding daily. 🚀"
        )
    },
]

# ── FALLBACK RESPONSE (when no intent is matched) ───────────────────────────
FALLBACK = (
    "🤔 I'm not sure I understand that question.\n"
    "Try asking about: AI, Machine Learning, Deep Learning,\n"
    "Python, GitHub, Assignments, University info, or say 'hello'."
)


# ── CORE MATCHING FUNCTION ──────────────────────────────────────────────────
def match_intent(user_input: str) -> str:
    """
    Takes the user's raw text, cleans it, then checks it
    against every intent's keyword list.
    Returns the matched response or the fallback.
    """
    # Normalise: lowercase + strip punctuation
    cleaned = user_input.lower().strip()
    cleaned = re.sub(r"[^\w\s]", "", cleaned)  # remove punctuation

    for intent in INTENTS:
        for keyword in intent["keywords"]:
            # Check if keyword appears as a substring in the cleaned input
            if keyword in cleaned:
                return intent["response"]

    return FALLBACK  # no match found


# ── MAIN CHAT LOOP ──────────────────────────────────────────────────────────
def run_chatbot():
    """Entry point — runs the interactive chat loop in the terminal."""
    print("=" * 60)
    print("   🤖  AI Course Assistant Bot  (Rule-Based)")
    print("   Type 'bye' or 'exit' to quit")
    print("=" * 60)

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if not user_input:
                print("Bot: Please type something. I'm here to help!")
                continue

            response = match_intent(user_input)
            print(f"\nBot: {response}")

            # Exit condition
            cleaned = user_input.lower()
            if any(word in cleaned for word in ["bye", "exit", "quit", "goodbye"]):
                break

        except KeyboardInterrupt:
            print("\n\nBot: Session ended. Goodbye! 👋")
            break


# ── RUN ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    run_chatbot()
#This is the final project. It is a simple rule-based chatbot that answers FAQs about AI and university life. The bot uses keyword matching to determine the user's intent and provides pre-written responses.