class clock:
    def __init__(self, canvas, data):
        self.canvas= canvas
        self.dot = canvas.create_oval(data[0], data[1], data[0]+20, data[1]+20, fill="black")



