

import google.generativeai as genai

genai.configure(api_key="AIzaSyCPFFXiTyuyWHl8fz68KCFtsy772IMYKwM")

model = genai.GenerativeModel("models/gemini-pro")


chat = model.start_chat(history=[])

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat.send_message(user_input)
    print("Gemini:", response.text)
