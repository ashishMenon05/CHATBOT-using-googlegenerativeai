#project config


import google.generativeai as genai
genai.configure(api_key="AIzaSyAWP9_sQN4dvGeSRrdbiBZ1vESW6KfeY3c")
apple = genai.GenerativeModel("gemini-2.5-flash")
chat = apple.start_chat(history=[])
print("hi there i am HABIBI your partner")
while True:
    user_input = input("User : ")

    if user_input.lower() == "exit":
        break
    response = chat.send_message(user_input)
    print("HABIBI :",response.text)

    
