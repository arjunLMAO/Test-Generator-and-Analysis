import json
import random

def load_question_bank(json_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find '{json_file}'. Ensure the file is in the same folder.")
        return []
    except json.JSONDecodeError:
        print(f"Error: '{json_file}' contains invalid JSON syntax.")
        return []

def generate_test(all_questions, selected_topics, num_questions=3):
    filtered = [q for q in all_questions if q.get('topic') in selected_topics]
    
    if not filtered:
        print("\n No questions found for the selected topics.")
        return []
    
    return random.sample(filtered, min(num_questions, len(filtered)))

def run_test_session(selected_questions):
    if not selected_questions:
        return
    
    score = 0
    total = len(selected_questions)
    wrong_questions = []
    option_labels = ['A', 'B', 'C', 'D']

  
    print("STARTING TEST SESSION. \n")
   

    for idx, q in enumerate(selected_questions, 1):
        print(f"Q{idx} [{q.get('subject', 'General')} | Topic: {q.get('topic', 'N/A')} | Difficulty: {q.get('difficulty', 'N/A')}]")
        print(f"{q.get('question_text')}\n")
        
        options = q.get('options', [])
        correct_answer = q.get('correct_option')
        
        for label, opt in zip(option_labels, options):
            print(f"  {label}) {opt}")
        
        user_choice = input("\nYour Answer (A/B/C/D): ").strip().upper()
        
        
        user_answer_text = ""
        if user_choice in option_labels and option_labels.index(user_choice) < len(options):
            user_answer_text = options[option_labels.index(user_choice)]
        else:
            user_answer_text = user_choice

    
        if user_answer_text.lower() == str(correct_answer).lower() or user_choice == str(correct_answer).upper():
            print("\n Correct \n")
            score += 1
        else:
            print(f"\n Incorrect Correct Answer: {correct_answer}")
            print(f"💡 Explanation: {q.get('explanation', 'No explanation provided.')}\n")
            wrong_questions.append(q)
        
        print("-" * 50)

  
   
    print("FINAL TEST RESULTS. \n")
 
    percentage = (score / total) * 100 if total > 0 else 0
    print(f"Score: {score} / {total} ({percentage:.1f}%)")
    
    if wrong_questions:
        print(f"\n Questions Queued for Spaced Repetition Review ({len(wrong_questions)}):")
        for w in wrong_questions:
            print(f" • [{w.get('topic')}] {w.get('id', 'Q')}: {w.get('question_text')[:60]}...")
            
    print("\nTest session complete.\n")

if __name__ == "__main__":
   
    questions_data = load_question_bank('test_questions.json')
    
    if questions_data:
        topics_to_select = [
            'Projectile Motion', 
            'Work-Energy Theorem', 
            'Hybridization & VSEPR', 
            'Enthalpy & Spontaneity', 
            'Limits & Continuity'
        ]
        
       
        test_questions = generate_test(questions_data, topics_to_select, num_questions=3)
        
      
        run_test_session(test_questions)
