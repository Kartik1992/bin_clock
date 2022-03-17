class clock:
    def __init__(self, canvas, data):
        self.canvas = canvas
        if data[2] == 1:
            self.dot = canvas.create_oval(data[0], data[1], data[0] + 20, data[1] + 20, fill="white")
        else:
            self.dot = canvas.create_oval(data[0], data[1], data[0] + 20, data[1] + 20, fill="black")
