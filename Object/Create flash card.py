import random
flashcard = {'Con ong':'bee',   
            'Con thỏ': 'rabbit',
            'Con cua': 'crab',
            'Con mèo': 'cat',
            'Con ngựa': 'horse',
            'Con khỉ': 'monkey',
            'Con lừa': 'donkey'}
class flashcard:
        def __init__(self, flashcard):
            self.animals = dict(flashcard)
        def quiz(self):
            while True:
                vietnamese, english = random.choice(list(self.animals.items()))
                print(f'Tiếng anh của {vietnamese} là:')
                user_answer = input()
                if user_answer.lower() == english:
                    print('Correct')
                else: 
                    print('Incorrect')
                option = int(input('Nhấn 0 để tiếp tục: '))
                if option: 
                    break 
            print('The end')
fc = flashcard(flashcard)
fc.quiz()