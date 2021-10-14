class Console:

    def read(self, prompt):
        return input(prompt)
    
    def read_number(self, prompt):
        return float(input(prompt))
    
    def write(self, text):
        return print(text)