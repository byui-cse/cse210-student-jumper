class Console:

    def get_user_guess(self, prompt):
        while True:
            user_letter = input(prompt)
            
            if user_letter.isalpha() and len(user_letter) == 1:
                return user_letter.lower()
            
            print("Please enter a single letter only.")
