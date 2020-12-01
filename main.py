from tkinter import *
import requests

startup = True


def get_quote():
    global quote_text
    global startup
    quote_api = requests.get(url="https://api.kanye.rest")
    quote_api.raise_for_status()
    quote_data = quote_api.json()
    new_quote = quote_data["quote"]
    if startup:
        startup = False
        return new_quote
    else:
        canvas.itemconfig(quote_text, text=new_quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=get_quote(), width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
