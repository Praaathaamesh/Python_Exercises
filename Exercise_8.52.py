# mixing of lists elements and generate a funny story
import random

Opener = ['There was once, ','Thousand years ago, ','Week ago, ']
Charac = ['A king and he had','Samir and he had','My father and he had']
Object = [' a spoiled banana',' a Fish sandwich',' a rat']
Activity = ['. after eating it, ','. after selling it, ',',after buying it, ']
Disease = ['he died.','he slept for a years.','he took an arrow to the knee.']

print(random.choice(Opener)+random.choice(Charac)+random.choice(Object)+random.choice(Activity)+random.choice(Disease))