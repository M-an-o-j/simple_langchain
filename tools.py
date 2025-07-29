from pyfirmata2 import Arduino
import time

PORT = 'COM7' 
board = None
initialized = False

def init_board():
    """
    Initialize the Arduino board connection.

    If the board is not already initialized, it creates a connection to the Arduino
    board and starts sampling. If the board was already initialized, it just returns.
    If the initialization fails for any reason, it raises an exception.

    :raises: Exception if the board fails to initialize
    """
    global board, initialized
    if not initialized:
        try:
            board = Arduino(PORT)
            board.samplingOn()
            initialized = True
            print("Arduino board initialized.")
        except Exception as e:
            print(f"Board init failed: {e}")
            raise e


def light_on(dummy: str) -> str:
    """
    Turns on the built-in LED on the Arduino board.

    Args:
        dummy (str): A placeholder argument not used in the function.

    Returns:
        str: A message indicating whether the LED was successfully turned on or if there was an error.
    """

    try:
        init_board()
        board.digital[13].write(1)
        return "Built-in LED turned ON"
    except Exception as e:
        return f"Failed to turn on LED: {e}"


def light_off(dummy: str) -> str:
    """
    Turns off the built-in LED on the Arduino board.

    Args:
        dummy (str): A placeholder argument not used in the function.

    Returns:
        str: A message indicating whether the LED was successfully turned off or if there was an error.
    """
    try:
        init_board()
        board.digital[13].write(0)
        return "Built-in LED turned OFF"
    except Exception as e:
        return f"Failed to turn off LED: {e}"


# --- Other tools ---
def calculator(expression: str) -> str:
    """
    Evaluates a given mathematical expression and returns the result as a string.

    Args:
        expression (str): A mathematical expression, e.g. "2+2" or "3*4"

    Returns:
        str: The result of the expression, e.g. "4" or "12"
    """
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {str(e)}"

def greet(name: str) -> str:
    """
    Greets the user with their name.

    Args:
        name (str): The name to use in the greeting.

    Returns:
        str: A greeting message with the user's name.
    """
    return f"Hello, {name}! How can I help you today?"

def paper_game(user_input: str) -> str:
    """
    Play rock-paper-scissors with the computer.

    Args:
        user_input (str): The user's choice of "rock", "paper", or "scissors"

    Returns:
        str: A message indicating the result of the game and the computer's choice
    """
    import random
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    if user_input == computer_choice:
        result = "It's a tie!"
    elif (user_input == "rock" and computer_choice == "scissors") or \
         (user_input == "paper" and computer_choice == "rock") or \
         (user_input == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "You lose!"
    return f"You chose {user_input}, the computer chose {computer_choice}. {result}"
