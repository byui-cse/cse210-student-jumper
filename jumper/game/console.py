class Console:
    def get_letter(self, prompt):
        go_through = False
        while not go_through:
            user_input = input(prompt)
            if user_input.isalpha() and len(user_input) == 1:
                return user_input.lower()
            print("Please enter a single letter.")
    
    def write(self,message):
        print(message)