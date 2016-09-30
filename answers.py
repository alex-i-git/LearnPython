#!/usr/bin/python3
def get_answer(user_key,user_dict):
	return user_dict[user_key]	

dialog={"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

user_key=((input('Please enter key: ').lower()).rstrip()).lstrip()
print(get_answer(user_key,dialog))
