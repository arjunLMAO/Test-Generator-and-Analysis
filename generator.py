import json
import random

def generate_test(json_file, selected_topics, num_questions=3):
    try:
        with open(json_file, 'r') as f:
            all_questions = json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find '{json_file}'. Make sure the file exists.")
        return []
    
   
    filtered = [q for q in all_questions if q.get('topic') in selected_topics]
    
    if not filtered:
        print("No questions found for the selected topics.")
        return []
    
  
    selected = random.sample(filtered, min(num_questions, len(filtered)))
    return selected

if __name__ == "__main__":
    
    topics = ['Projectile Motion', 'Limits & Continuity']
    selected = generate_test('dummy_questions.json', topics)

    for idx, q in enumerate(selected, 1):
        print(f"Q{idx} [{q.get('subject')} - {q.get('topic')}]: {q.get('question_text')}")
