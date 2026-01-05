import json 
import random
import os

def check_data_exists(file):
    if os.path.exists(file):
        print("Data File Found...")

        return read_json_data(file)
    else:
        print(f"Data File Not found make sure the file is there in {os.getcwd()}")

def read_json_data(file):
    """ reading the data from the json file
    """
    with open(file, 'r') as file:
        data = json.load(file)

    return data;


def generate_file(data, index):
    if not os.path.exists('quizfiles'):
        os.mkdir('quizfiles')
        os.mkdir('quizfiles/quizes')
        os.mkdir('quizfiles/answers')
    
    # 1. Prepare Data
    all_questions = data['python_quiz']
    sample_size = 35
    shuffled_subset = random.sample(all_questions, sample_size)

    # 2. Open both Quiz and Answer Key files
    with open(f'quizfiles/quizes/quiz_{index}.txt', 'w') as quiz_file, \
         open(f'quizfiles/answers/answers_{index}.txt', 'w') as ans_file:
        
        # Write Header
        quiz_file.write(f"Name: {'_'*20} Date: {'_ '*3} Period: {'_'*5}\n")
        quiz_file.write("\n" + " " * 20 + "PYTHON QUIZ (Form A)\n\n")
        ans_file.write("ANSWER KEY FOR QUIZ 1\n\n")

        # 3. Loop through the random sample
        for num, question in enumerate(shuffled_subset, 1):
            q_text = question['question']
            correct_ans = question['answer']
            
            # Split and shuffle options safely
            options_list = question['options'].split(', ')
            random.shuffle(options_list) # Randomize the order of A, B, C, D

            # Write Question to File
            quiz_file.write(f"\n{num}. {q_text}\n")
            
            # Write Options
            for i, option in enumerate(options_list):
                letter = chr(65 + i) # A, B, C, D...
                quiz_file.write(f" [ ] {letter}. {option}\n")
                
                # Check if this shuffled option is the correct one to build Answer Key
                if option == correct_ans:
                    ans_file.write(f"{num}. {letter}\n")
            
            quiz_file.write("\n")
    print(f"Done: Quiz {index}")



if __name__ == '__main__':
    file = 'data.json'
    data = check_data_exists(file)
    student_count = 50
    for i in range(student_count):
        generate_file(data, index = i+1)

    print("Thanks for using me")
    print("Files saved..")
    
