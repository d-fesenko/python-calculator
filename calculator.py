import tkinter as tk

result = ""

def addoperand(operand):
    global result
    result += str(operand)

    updatetext(result)

def evaluate():
    global result
    try:
        evaluated = eval(result)
        result = str(int(evaluated)) if evaluated%1 == 0 else str(evaluated)
        
        updatetext(result)
    except:
        updatetext("Error")

def updatetext(newtext):
    text_result.delete(1.0, "end") #Deletes content of result field from index 1 to end
    text_result.insert(1.0, newtext)

def clear():
    global result
    result = ""
    updatetext(result)

root = tk.Tk()
root.geometry("300x275")

#Text field for the calculator result
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

btn_1 = tk.Button(root, text="1", command = lambda: addoperand(1), width = 5, font = ("Arial", 14))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command = lambda: addoperand(2), width = 5, font = ("Arial", 14))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command = lambda: addoperand(3), width = 5, font = ("Arial", 14))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command = lambda: addoperand(4), width = 5, font = ("Arial", 14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command = lambda: addoperand(5), width = 5, font = ("Arial", 14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command = lambda: addoperand(6), width = 5, font = ("Arial", 14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command = lambda: addoperand(7), width = 5, font = ("Arial", 14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command = lambda: addoperand(8), width = 5, font = ("Arial", 14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command = lambda: addoperand(9), width = 5, font = ("Arial", 14))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command = lambda: addoperand(0), width = 5, font = ("Arial", 14))
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", command = lambda: addoperand("+"), width = 5, font = ("Arial", 14))
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", command = lambda: addoperand("-"), width = 5, font = ("Arial", 14))
btn_minus.grid(row=3, column=4)

btn_mult = tk.Button(root, text="*", command = lambda: addoperand("*"), width = 5, font = ("Arial", 14))
btn_mult.grid(row=4, column=4)

btn_div = tk.Button(root, text="/", command = lambda: addoperand("/"), width = 5, font = ("Arial", 14))
btn_div.grid(row=5, column=4)

btn_lparen = tk.Button(root, text="(", command = lambda: addoperand("("), width = 5, font = ("Arial", 14))
btn_lparen.grid(row=5, column=1)

btn_rparen = tk.Button(root, text=")", command = lambda: addoperand(")"), width = 5, font = ("Arial", 14))
btn_rparen.grid(row=5, column=3)

btn_clear = tk.Button(root, text="C", command = clear, width = 5, font = ("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2)

btn_eval = tk.Button(root, text="=", command = evaluate, width = 5, font = ("Arial", 14))
btn_eval.grid(row=6, column=3, columnspan=2)

root.mainloop()