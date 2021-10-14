class Console:
    def get_letter(self,prompt):
        go_though = False
        while not go_though:
            user_input = input(prompt)
            if user_input.isalpha() and len(user_input) == 1:
                return user_input.lower()
            print("Please enter a single letter.")
    
    def write(self,message):
        print(message)