def main():
  # Program Variables
  loop = True
  
  # Main Program Loop

  while loop:
    selection = getMenuSelection()

    if selection == "1":
      option1()
    elif selection == "2":
      option2()
    elif selection == "3":
      option3()
    elif selection == "4":
      if input("\nType confirm if you are finished: ") == "confirm":
        loop = False
        print("goodbye")
      else:
        loop = True
        print("\nReturning you to the main menu")
    elif selection == "":
      print("\nplease make a selection, returned to menu")
    else:
      print("\nInvalid selection please use numbers 1-4, returned to menu")


      
      
 
#----------------------------------------------------------------------------------------------------

def getMenuSelection():
  print("\nMAIN MENU")
  print("1: Option 1")
  print("2: Option 2")
  print("3: Option 3")
  print("4: Exit")
  return input("Enter menu selection:")


#OPTION 1---------------------------------------------------------------------------------------------------
def option1():
  print("\nOption 1 - Calculator")
  
  num1 = float(input("enter first number: "))
  op = input("enter operator (*,/,+,-): ")
  num2 = float(input("enter second number: "))


  if op == "+":
      print(num1 + num2)
  elif op == "-":
      print(num1 - num2)
  elif op == "*":
      print(num1 * num2)
  elif op == "/":
      print(num1 / num2)
  else:
      print("please insert a valid operation")


#END OF OPTION 1 -------------------------------------------------------------------------------------------------

#START OF OPTION 2 -----------------------------------------------------------------------------------------------
def option2():
  print("\nOption 2 - Guessing game")
  print("\nThe word has something to do with this program")
  secret_word = "python"
  guess = ""
  guess_number = 0
  guess_limit = 3
  out_of_guesses = False

  while guess != secret_word and not(out_of_guesses):
    if guess_number < guess_limit:
      guess = input("\nInput a guess for the word: ")
      guess_number += 1
    else:
      out_of_guesses = True

  if out_of_guesses:
    print("\nYou lost, the word was python.")
  else:
    print("\nGood work you guessed right!")
    
#END OF OPTION 2--------------------------------------------------------------------------------------------------
#START OF OPTION 3------------------------------------------------------------------------------------------------
def option3():
  print("\nOption 3")

  print("this program changes vowels to an s \n")

  def translate(phrase):
      translation = ""
      for letter in phrase:
          if letter.lower() in "aeiou":
              if letter.isupper():
                  translation = translation + "S"
              else:
                translation = translation + "s"   
          else:
              translation = translation + letter
      return translation

  print(translate(input("enter a phrase ")))

  input("press enter")

#END OF OPTION 3--------------------------------------------------------------------------------------------------
