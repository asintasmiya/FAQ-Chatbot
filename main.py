
import tkinter as tk
from tkinter import scrolledtext
def get_response(question):
    """Retrieve response from FAQ database"""
    faq = {
        "what are your hours": "We are open from 9 AM to 5 PM, Monday to Friday.",
        "do you offer online classes": "Yes, we offer online classes. Visit our website for details.",
        "how to contact support": "Contact support at support@example.com or call 123-456-7890.",
        "return policy": "Our return policy lasts 30 days from purchase date.",
        "payment methods": "We accept credit cards, PayPal, and bank transfers."
    }
    
    question = question.lower()
    return faq.get(question, "I'm sorry, I don't have an answer for that. Please check our FAQ page.")

def run_gui():
    def ask_question():
        question = entry.get()
        if question.strip():
            response = get_response(question)
            chat_area.config(state='normal')
            chat_area.insert(tk.END, f'You: {question}\n', 'question')
            chat_area.insert(tk.END, f'Bot: {response}\n\n', 'answer')
            chat_area.config(state='disabled')
            entry.delete(0, tk.END)

    def clear_chat():
        chat_area.config(state='normal')
        chat_area.delete('1.0', tk.END)
        chat_area.config(state='disabled')

    def set_theme(theme):
        if theme == 'Light':
            root.config(bg='#f0f4f8')
            chat_area.config(bg='white', fg='black', insertbackground='black')
            entry.config(bg='white', fg='black', insertbackground='black')
            question_label.config(bg='#f0f4f8', fg='#2e3a59')
        elif theme == 'Black':
            root.config(bg='#181818')
            chat_area.config(bg='#181818', fg='white', insertbackground='white')
            entry.config(bg='#181818', fg='white', insertbackground='white')
            question_label.config(bg='#181818', fg='#e0e0e0')

    root = tk.Tk()
    root.title('FAQ Chatbot')
    root.geometry('430x400')

    theme_var = tk.StringVar(value='Light')
    theme_menu = tk.OptionMenu(root, theme_var, 'Light', 'Black', command=set_theme)
    theme_menu.pack(pady=(10,0))

    question_label = tk.Label(root, text='Ask your questions:', font=('Arial', 12, 'bold'), bg='#f0f4f8', fg='#2e3a59')
    question_label.pack(pady=(0,0))

    chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', height=15)
    chat_area.tag_config('question', foreground='red')
    chat_area.tag_config('answer', foreground='blue')
    chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    entry = tk.Entry(root, width=40)
    entry.pack(padx=10, pady=(0,10), side=tk.LEFT, expand=True, fill=tk.X)
    entry.focus()

    ask_btn = tk.Button(root, text='Ask', command=ask_question)
    ask_btn.pack(padx=(0,10), pady=(0,10), side=tk.RIGHT)

    clear_btn = tk.Button(root, text='Clear', command=clear_chat)
    clear_btn.pack(padx=(0,10), pady=(0,10), side=tk.RIGHT)

    set_theme('Light')  
    root.mainloop()

if __name__ == "__main__":
    run_gui()

