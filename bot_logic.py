import pandas as pd
from freshdesk import create_ticket

faq = pd.read_csv("data/faq.csv")
metrics_file = "data/metrics.csv"
metrics = pd.read_csv(metrics_file)

def save_metrics():
    global metrics
    metrics.to_csv(metrics_file, index=False)

def proactive_trigger(question):
    triggers = {"price": "Are you interested in a full course or CE course?",
                "exam": "Do you want tips on passing the exam?"}
    for key, msg in triggers.items():
        if key in question.lower():
            return msg
    return None

def ask_bot(question):
    global metrics
    metrics.at[0, 'questions_asked'] += 1

    match = faq[faq['question'].str.contains(question, case=False)]
    if not match.empty:
        answer = match.iloc[0]['answer']
        metrics.at[0, 'questions_answered'] += 1
        save_metrics()
        trigger = proactive_trigger(question)
        if trigger:
            answer += f"\n\nProactive question: {trigger}"
        return answer, False
    else:
        answer = "Sorry, I don't know the answer."
        metrics.at[0, 'tickets_created'] += 1
        save_metrics()
        return answer, True
