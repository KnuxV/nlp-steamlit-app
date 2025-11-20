# Simple NLP App – Git & Streamlit Practice Project

Live app: https://nlp-steamlit-app-3lfei7acyjojd5ddnc6yea.streamlit.app/

This is a tiny Streamlit app made on purpose for learning **Git + GitHub collaboration** in a team setting.

The app is deliberately basic and incomplete – your job is to add new features!

## Current features
- Paste any text
- Choose a tool with the pills:
  - Number of words (not yet implemented)
  - Number of sentences (not yet implemented)
  - Sentiment Analysis (using Vader)

## How to contribute (the real-world GitHub workflow)

### 1. One-time setup
```bash
# 1. Fork this repo on GitHub (button top-right → "Fork")

# 2. Clone YOUR fork
git clone https://github.com/YOUR-USERNAME/nlp-steamlit-app.git
cd nlp-steamlit-app

# 3. Add the original repo as "upstream" (so you can stay up-to-date)
# upstream is the remote to the team repo, origin is the remote to your fork
git remote add upstream https://github.com/KnuxV/nlp-steamlit-app.git
```

### 2. Always work on a new branch (never directly on main)
```bash
git checkout main
git pull upstream main                  # make sure you're up to date first
git checkout -b feature/word-count      # give your branch a clear name
```

### 3. Set up the project locally
```bash
python -m venv venv
# Linux
source venv/bin/activate        
# Windows: 
venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py
```
Try the app, play with it, make sure everything works.

### 4. Implement your feature → test → commit
```bash
git add .
git commit -m "Add word count functionality"
# You push your feature branch to your forked repo (remote=origin) first.
git push origin feature/word-count
```

### 5. Open a Pull Request
Go to your fork on GitHub → you’ll see a banner “Compare & pull request”  
→ Create PR from `feature/word-count` → `KnuxV:main`

I will review, maybe ask for small changes, then merge.

### 6. After your PR is merged → sync your local and remote main
```bash
git checkout main
git pull upstream main          # get the latest code from the original repo
git push origin main            # update your fork's main (optional but clean)
git branch -d feature/word-count # delete the old branch locally
```

Repeat the whole process for every new feature!

## Suggested Tasks – Choose What You Want to Add!

To keep collaboration smooth and conflict-free, we split the tasks into two categories:

### Category A – Super Safe & Easy (recommended for everyone)
These only require:
- Adding a new file in `src/` (e.g. `src/your_feature.py`)
- Update the `TOOLS` dictionary in `app.py`
- Update the import at the top of `app.py`

→ Almost zero risk of merge conflicts!

1. **Word count** → `src/word_count.py` (required – currently empty)
2. **Sentence count** → `src/sentence_count.py` (required – currently empty)
3. Character count (with and without spaces)
4. Average word length
5. Count punctuation marks
6. Count numbers/digits in the text
7. Count emojis (use the `emoji` package or a simple regex)
8. Vowel vs consonant counter
9. Word frequency → return top 10 most common words (use `collections.Counter`)
10. “Tweet checker” → show if text ≤ 280 characters + how many characters left
11. Reading time estimate (e.g. ~250 words per minute)

### Category B – A bit more UI, still safe if done carefully
These need small changes in `app.py` (usually inside the `if selection == "Your Tool":` block)

12. Count occurrences of a specific word (add a small text input below the main text area)
13. Extract all URLs and display them as clickable markdown links
14. Convert text to UPPERCASE / lowercase / Title Case (add 3 buttons)
15. Find & replace a word (two small inputs + button)
16. Highlight the longest word(s) in the original text

### Category C – Slightly bigger features (great for learning file handling or extra libraries)

17. Upload a .txt file instead of typing (`st.file_uploader`)
18. Add a readability score (Flesch-Kincaid – pure Python formula, no extra package needed)
19. Generate and display a word cloud (`wordcloud` + `matplotlib`)
20. Dark / Light mode switch (`st.toggle` or session state)

### Bonus fun ones
- Add a “Copy result to clipboard” button
- Add a “Clear text” button
- Show a progress bar while “analyzing” (fake delay with `st.progress` + `time.sleep`)
