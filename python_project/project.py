# Import in-built modules
import random
import sys

# Open Project.txt and append the code to the file
sys.stdout = open('project.txt', 'a+')


# Function used to get user's age and check whether user has met the age requirement to play
def age():
    file = open('project.txt', 'a+')
    user_age = int(input("Enter your age: "))
    if user_age >= 18:
        print("You are eligible to play")
    else:
        print("You are not eligible to play")
        sys.exit()
    file.write(str(user_age) + '\n')


# This Class is used to get user's number predictions and add them to number list
class NumberPrediction:

    def __init__(self, prediction, user_predicted, num_answer):
        self.user_predictions = prediction  # User's number prediction list
        self.user_prediction = user_predicted  # Input for User's number prediction
        self.num_of_correct_predictions = num_answer  # The number of times User predicted correctly

    # This function used to capture User's number predictions
    def predictions(self):
        self.user_predictions = []  # User's number prediction list
        count = 0  # count used for while loop
        attempts_left = 6  # User's attempts
        while count < 6:  # This while loops ends at 6 try's
            f = open('project.txt', 'a+')  # Opens project.txt and appends code to the file
            self.user_prediction = int(input("Predict a number from 1 - 49: "))
            # Method to add user's numbers to the user's list
            if self.user_prediction in range(1, 49):
                attempts_left -= 1  # Decreases attempts
                self.user_predictions.append(self.user_prediction)  # Adds numbers user's list
                print("Attempts left: ", attempts_left)
            # If the number is not in the range(1, 49) it will continue to top of method using continue statement
            elif self.user_predictions not in range(1, 49):
                print("Out of range", "\n" "Attempts left: ", attempts_left)
                continue  # Continues to the top of method
            count = count + 1  # adds to the count variable (once count reaches 6 the loop breaks
            f.write(str(self.user_prediction) + '\n')
        # This method removes duplicate numbers in the user's prediction list
        self.user_predictions = list(dict.fromkeys(self.user_predictions))
        print("User's list of unique predictions: ", self.user_predictions)

    # This function generates 6 random numbers from range(1, 49)
    def generated_numbers(self):
        # Generates random numbers from range(1, 49)
        num = set()
        while len(num) < 6:  # loop ends at 6 try's
            num.add(random.randint(1, 49))
        random_num_list = list(num)
        print("Numbers Randomly generated from 1 to 49: ", random_num_list)
        a = self.user_predictions  # User's prediction list with unique numbers
        b = random_num_list  # 6 random numbers in generated list from range(1, 49)
        # Returns a new list with numbers that is the same when comparing user's list and random generated list
        user_correct_predictions_list = set(a) & set(b)
        # The amount of numbers predicted correctly
        self.num_of_correct_predictions = len(user_correct_predictions_list)
        print("These are the numbers you predicted correctly: ", user_correct_predictions_list)

    # This function shows the user what prize he/she has won
    def prizes(self):
        if self.num_of_correct_predictions == 6:  # If predicted 6 numbers correctly
            print("You won: R10 000 000.00")
        elif self.num_of_correct_predictions == 5:  # If predicted 5 numbers correctly
            print("You won: R8 584.00")
        elif self.num_of_correct_predictions == 4:  # If predicted 4 numbers correctly
            print("You won: R2 384.00")
        elif self.num_of_correct_predictions == 3:  # If predicted 3 numbers correctly
            print("You won: R100.50")
        elif self.num_of_correct_predictions == 2:  # If predicted 2 numbers correctly
            print("You won: R20.00")


# Executes function age()
age()
# Call Class NumberPrediction
return_prediction = NumberPrediction(random.randint(1, 49), 0, 0)
# Executes NumberPrediction Class Functions
return_prediction.predictions()
return_prediction.generated_numbers()
return_prediction.prizes()
# To avoid confusion when appending module to file again
print("=====================")
sys.stdout.close()
# ========================================================================
# Can't see output because of sys.stdout method when writing to project.txt so these are the output steps below
# Remove sys.stdout and sys.stdout.close() to see output on console
# ========================================================================
# ====== Input Steps=====
# Enter your age:
# You are eligible to play or You are not eligible to play
# Predict a number from 1 - 49: (Input number)
# Attempts left:  5
# Predict a number from 1 - 49: (Input number)
# Attempts left:  4
# Predict a number from 1 - 49: (Input number)
# Attempts left:  3
# Predict a number from 1 - 49: (Input number)
# Attempts left:  2
# Predict a number from 1 - 49: (Input number)
# Attempts left:  1
# Predict a number from 1 - 49: (Input number)
# Attempts left:  0
# User's list of unique predictions:  []
# Numbers Randomly generated from 1 to 49:  []
# These are the numbers you predicted correctly:  {}
# You won: (prize)
# =====================
