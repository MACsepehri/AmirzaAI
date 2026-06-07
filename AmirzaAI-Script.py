from time import sleep
from os import system
from openai import OpenAI
import os

TOKEN = "sk-0ViIkDfs4Fxw4UnSs8ME1kgCXWo7hvRtwFcRDvQ74faVtsIl"
client = OpenAI(base_url='https://api.gapgpt.app/v1', api_key=TOKEN)

def get_answer(question, min_length):
    instruction = f"تو باید کلمات {min_length} حرفی به بالا را با حروفی که بهت داده میشه حل کنی. سعی کن فقط با معنی ها رو بگی و چیز اضافی نگی لطفا کم نگو تا جایی که میتونی زیاد بگو."

    history = {
        "role": "user", 
        "content": [
            {"type": "text", "text": instruction},
            {"type": "text", "text": question}
        ]
    }
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[history]
    )
    log_text(response.choices[0].message.content)

def cls(): 
    system("cls")

def log_text(text, sleep_time=0.03):
    for chunk in text:
        print(chunk, end="", flush=True)
        sleep(sleep_time)
    print()

def welcome_text():
    log_text("Hello ADMIN! Welcome to AmirzaAi. Here I can help you to complete your online / offline games!\n")

def starter():
    log_text("You can decide start from which length :\n")
    log_text("1 => '3' up to more.\n")
    log_text("2 => '4' up to more.\n")
    log_text("3 => '5' up to more.\n")
    log_text("4 => '6' up to more.\n")
    return int(input("Your choice! AmirzaAi is waiting for you! : "))

def main():
    welcome_text()
    while True:
        q = starter()
        word_input = input("Enter your letters (in persian): ")
        
        match q:
            case 1:
                get_answer(word_input, 3)
            case 2:
                get_answer(word_input, 4)
            case 3:
                get_answer(word_input, 5)
            case 4:
                get_answer(word_input, 6)
        input("Press 'Enter' to start again! ")
            

if __name__ == "__main__":
    cls()
    main()
