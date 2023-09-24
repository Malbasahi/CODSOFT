import re
import tkinter as tk
from tkinter import scrolledtext

# Define a dictionary of predefined rules and detailed medical responses
medical_rules = {
    # Greetings
    r'(hello|hi|hey)': 'Hello! How can I assist you with your medical questions?',
    r'how are you': 'I am just a computer program, but I am here to help with medical information.',
    r'(bye|goodbye)': 'Goodbye! Take care of your health!',
    r'help': 'I can provide information on various medical topics. Just ask your medical question.',
    
    # Common Symptoms
    r'(cough|cold)': 'For a cough or cold, you can try rest, staying hydrated, and over-the-counter cold remedies. Common remedies include drinking warm fluids, using throat lozenges, and getting plenty of rest. If your symptoms persist or worsen, consult a doctor, especially if you have a high fever, severe cough, or breathing difficulties. Remember that I\'m not a substitute for professional medical advice, so consult a healthcare professional for personalized guidance.',
    r'pain': 'I am sorry to hear about your pain. Pain can have various causes, including tension, stress, or underlying medical conditions. It\'s essential to consult a healthcare professional to determine the cause and receive appropriate treatment.',
    r'fever': 'If you have a fever, it\'s important to rest, stay hydrated, and take fever-reducing medication like acetaminophen. If your fever persists or is accompanied by severe symptoms, consult a healthcare professional.',
    r'(headache|migraine)': 'Headaches can have various triggers, including stress, dehydration, or underlying medical conditions. Rest, hydration, and over-the-counter pain relievers can help. If you experience frequent or severe headaches, consult a healthcare professional for evaluation and management.',
    
    # Specific Conditions
    r'COVID-19|coronavirus': 'COVID-19 is a viral respiratory illness with symptoms like fever, cough, and shortness of breath. Preventive measures include wearing masks, practicing social distancing, and frequent handwashing. If you experience COVID-19 symptoms or have been exposed to the virus, seek testing and follow local health guidelines.',
    r'medication': 'Medications can have side effects and potential risks. It\'s crucial to follow your doctor\'s instructions, take medications as prescribed, and be aware of possible side effects. Discuss any concerns with your healthcare provider.',
    r'weight': 'Weight management involves a balanced diet, regular exercise, and lifestyle choices. Consult a healthcare professional or nutritionist for personalized guidance on achieving your weight-related goals.',
    r'(allerg(y|ies))': 'Allergies can cause symptoms like sneezing, runny nose, and itchy eyes. Over-the-counter antihistamines can help manage mild allergy symptoms. If your allergies are severe or affecting your quality of life, consult an allergist for further evaluation and treatment options.',
    r'(diabetes|blood sugar)': 'Diabetes is a chronic condition that affects blood sugar levels. Managing diabetes includes monitoring blood sugar, following a healthy diet, exercising, and taking prescribed medications. It is important to work closely with a healthcare team to manage diabetes effectively.',
    r'(heart disease|cardiovascular)': 'Heart disease is a broad term that includes conditions like heart attacks and heart failure. Preventive measures include a heart-healthy diet, regular exercise, not smoking, and managing risk factors like high blood pressure and cholesterol levels. Consult a cardiologist for personalized advice on heart health.',
    r'(mental health|depression|anxiety)': 'Mental health is essential. If you are experiencing depression or anxiety, consider speaking with a mental health professional. They can provide therapy, counseling, or medication to help manage symptoms and improve your well-being.',
    r'(pregnancy|maternity)': 'Pregnancy is a unique and exciting time. Make sure to get regular prenatal care, eat a balanced diet, take prenatal vitamins, and follow your doctor\'s recommendations. Consult an obstetrician for personalized guidance during pregnancy.',
}

# Function to find a response based on user input
def get_medical_response(user_input):
    for pattern, response in medical_rules.items():
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            return response
    return "I'm not sure how to answer that. Please ask a different medical question, or consult a healthcare professional for personalized advice."

# Function to find a response based on user input
def get_medical_response(user_input):
    for pattern, response in medical_rules.items():
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            return response
    return "I'm not sure how to answer that. Please ask a different medical question, or consult a healthcare professional for personalized advice."

# Function to handle user input and display responses
def handle_input(event=None):
    user_input = input_entry.get("1.0", "end-1c")
    response = get_medical_response(user_input)
    chat_log.config(state=tk.NORMAL)
    chat_log.insert("end", f"You: {user_input}\n")
    chat_log.insert("end", f"Medical Chatbot: {response}\n")
    chat_log.config(state=tk.DISABLED)
    input_entry.delete("1.0", "end")

# Create the main window
root = tk.Tk()
root.title("Medical Chatbot")

# Create a custom design
root.geometry("600x400")
root.configure(bg="lightblue")

# Create a scrolled text widget for chat logs
chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, bg="white", width=40, height=10)
chat_log.pack(expand=True, fill="both", padx=10, pady=10)

# Create an entry field for user input
input_entry = tk.Text(root, height=3, bg="lightgray", width=40)
input_entry.pack(expand=True, fill="both", padx=10, pady=10)

# Create a button to submit user input
submit_button = tk.Button(root, text="Submit", command=handle_input, bg="green", fg="white")
submit_button.pack(pady=5)

# Bind the Enter key to trigger the submit function
input_entry.bind("<Return>", handle_input)

# Start the main event loop
root.mainloop()