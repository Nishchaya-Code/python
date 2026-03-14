from hf import generate_response

def get_essay_details():
    print('\n=== AI Writing Assistant ===\n')
    topic = input('what is the topic of the essay').strip()
    essay_type=input('what type of essy are writing').strip()
    lengths=['300 words','900 words','1200 words','1500 words']
    print ('word count')
    for i,l in enumerate(lengths,1): print(f'{i}){l}')
    try:
        idx = int (input('>').strip())
        length = lengths[idx-1]if 1<=idx<=len(lengths) else '300 words'
    except ValueError:
        length='300 words'
    'target_audiance':input(Target audiance).strip()
    return{'topic': topic, 'essay-type': essay_type, 'length':length,
'target_audiance': target_audiance}

 def generate_essay_content(details):
       