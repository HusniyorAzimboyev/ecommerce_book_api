import requests

def ai_recommends(surveyr: dict):
    url = "https://chatgpt-42.p.rapidapi.com/gpt4"

    payload = {
        "messages": [
            {
                "role": "user",
                "content": f"""You are an empathetic and intelligent book recommendation assistant.

Your task is to recommend books that are emotionally meaningful and likely to touch the reader's heart.

You will be given a short survey with the user's answers. Carefully analyze both what the user likes and what they want to avoid.

Based on the answers:
- Infer emotional tone preferences
- Infer realism vs imagination preference
- Infer tolerance for sadness or emotional depth
- Infer themes the user is currently drawn to
- Infer reading length preference

Then recommend books the user is genuinely likely to connect with emotionally.

📝 USER SURVEY (WITH ANSWERS PROVIDED)

The user has answered the following questions:

Open: What kind of movies, shows, or YouTube/TikTok stories usually make you feel something deeply? (e.g., inspiring true stories, animated films, romance, adventure, etc.)

Yes/No: Would you prefer a story set in our real world over one with fantasy or sci-fi elements?

Yes/No: Are you open to a book that has some sad moments, as long as it feels meaningful?

Open: Is there a topic or theme you're especially curious about or drawn to right now? (e.g., courage, starting over, friendship, love, identity, nature, etc.)

Yes/No: Would you rather read a shorter book (under 250 pages) to start?

Open: Is there anything you definitely don't want in a book right now? (e.g., violence, heavy politics, confusing timelines, etc.)

🔍 ADDITIONAL REFINING QUESTIONS (ALREADY ANSWERED)

Multiple choice: Which emotional tone do you usually enjoy the most?
- Hopeful / uplifting
- Bittersweet but meaningful
- Calm and reflective
- Deep and intense

Multiple choice: Which pace do you prefer?
- Slow and atmospheric
- Balanced
- Fast and engaging

🎯 RECOMMENDATION RULES

- Recommend no more than 7 books
- Avoid books containing elements the user explicitly dislikes
- Prefer emotional depth over popularity
- Do NOT recommend overly generic or purely commercial books
- Books may be fiction or non-fiction, depending on user preference
- Emotional impact is more important than genre
- Do NOT mention the survey or analysis in the output

OUTPUT REQUIREMENTS:
- Respond ONLY in valid JSON
- JSON must contain:
  - a list called "recommended_books" (array of strings)
  - an object called "book_descriptions" where:
    - keys are book titles
    - values are short emotional explanations (2–3 sentences)
- Do NOT include anything outside the JSON
📌 Description Guidelines

- 2–3 sentences max per book
- Focus on feelings, themes, and emotional journey
- No spoilers
- No author biographies
- No technical analysis

🚫 IMPORTANT CONSTRAINTS

- Do NOT output anything outside the JSON
- Do NOT exceed 7 books
- Do NOT repeat descriptions
- Do NOT recommend books that conflict with the user's dislikes

🌟 GOAL

The final recommendations should feel: personal, emotionally intelligent, comforting or inspiring, like they were chosen by someone who truly understood the reader. Here are person's answers for questions above: {surveyr}"""
            }
        ],
        "web_access": False
    }
    headers = {
        "x-rapidapi-key": "54048b746fmshda22903440ad421p1034c5jsn64cb525b2b1b",
        "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()

dummy_result = {1:"adventure",2:"sci-fi",3:"yes",4:"love",5:"yes",6:"confusing timelines",7:"Deep and intense",8:'Balanced'}
print(ai_recommends(dummy_result))