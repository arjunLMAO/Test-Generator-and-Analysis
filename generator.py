import json
import random

def generate_test(json_file, selected_topics, num_questions=3):
    with open(json_file, 'r') as f:
        all_questions = json.load(f)
    
    # Filter by topic
    filtered = [q for q in all_questions if q['topic'] in selected_topics]
    
    # Pick questions
    selected = random.sample(filtered, min(num_questions, len(filtered)))
    return selected

# Test your script
selected = generate_test('dummy_questions.json', ['Projectile Motion', 'Limits & Continuity'])
for idx, q in enumerate(selected, 1):
    print(f"Q{idx}: {q['question_text']}")
