from groq import generate_response
def run_activity():
    print('ZERO-SHOT,ONE SHOT & FEW SHOT LEARNING ACTIVITY')
    category = input('Enter a category(e.g, animal food, city):').strip()
    item=input(f'enter a specific {category} to classify').strip
    if not category or not item:
        print ('please fill in both fields to run the activity')
        return
    zero_shot = f'Is {item} a {category}? answer yes or no'
    print('\n--- ZERO-SHOT LEARNING ---')
    print(f'Respinse: {generate_response(zero_shot, tempreture=0.3, max_tokens=1024)}')

    one_shot= f"""Example:
category: fruit
Item: apple
Answer: Yes, apple is a fruit

Now you try:
Category:{category}
Item:{item}
Answer:"""
    print('\n--- FEW-SHOT LEARNING ---')
    print(f'response: {generate_response(few_shot, tempreture=0.3, max_tokens=1024)}')

    creative_prompt=f"""Write a one sentance story about the given word.
Example 1: Word: Moon
Story: It was a cows dream to jump over the moon
Word{item}
Story:"""
    print('\n--- CREATIVE FEW-SHOT ---')
    print(f'Response: {generate_response(creative_prompt, temperature=0.7, max_tokens=1024)}')

    print('\n--- REFLETION QUESTIONS ---')
    print('1. How did the responses differ between zero-shot, one-shot, and few-shot?')
    print('2. Which approach gave the most helpful response')
    print("3. How did the exampokes influence the model's output?")

if __name__=="__main__":
    run_activity