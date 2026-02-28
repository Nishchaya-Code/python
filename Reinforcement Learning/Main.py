from groq import generate_response 

def reinforcement_learning():
    print('\n===REINFORCEMENT LEARNINGb ACTIVITY ===\n')
    prompt = input("'Enter a prompt for the AI model (eg., 'Describe the lion'): ").strip()
    if not prompt:
        print('Please enter a prompt to run the activity ')
        return
    
    initial_response = generate_response(prompt, tempreture=.3 , max_tokens=1024)
    print(f'\nInitial AI response: {initial_response}')

    try:
        rating=int(input('Rate the response from 1(bad) to 5(The opposit of bad)'))
        if rating<1 or rating>5:
            print('Invalid rating. Using 3')
            rating=3
    except ValueError:
        print('Invalid rating. Using 3.')
        rating=3

    feedback=input('Provide feedback for improvement: ').strip()
    improved_respons=f'{initial_response} (Impoved with tour feedback: {feedback})'
    print(f'\n')