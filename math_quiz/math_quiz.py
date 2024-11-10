import random


def random_int(min, max):
    """
    returns a random integer.
    """
    return random.randint(int(min), int(max))


def random_calc():
    """
    returns a random calculation operator (either +, -, or *).
    """
    return random.choice(['+', '-', '*'])


def calc_result(n1, n2, o):
    """
    Shows equation and calculates result of the equation
    """
    equation = f"{n1} {o} {n2}"
    if o == '+': result = n1 + n2   #add numbers if o is +
    elif o == '-': result = n1 - n2 #substract numbers if o is -
    else: result = n1 * n2  #multiply numbers otherwise
    return equation, result #return the equation and then the result

def math_quiz():
    """
    math quiz in which random numbers between 1-10 and 1-5.5 
    are either added, substracted, or multiplied

    user gets the numbers and operator and has to calculate the correct result to get a score.

    if user is incorrect, they don't get a point and if anything but a number is entered, it will stay 
    on that question until a number is provided.

    game ends after 3 questions
    """
    s = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(int(t_q)):
        n1 = random_int(1, 10); n2 = random_int(1, 5.5); o = random_calc()  #get random numbers and operator

        PROBLEM, ANSWER = calc_result(n1, n2, o)   #get equation and correct result
        print(f"\nQuestion: {PROBLEM}") #print equation for user to see

        while True:  # Loop until valid input is provided
            try:
                useranswer = int(input("Your answer: "))
                break  # Exit loop if input is valid
            except ValueError:
                print("Invalid input. Please enter a number.")  

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1  
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{int(t_q)}") 

if __name__ == "__main__":
    math_quiz()
