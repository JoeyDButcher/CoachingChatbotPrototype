# answered check for if the user wants to change their answers or is satisfied with them
answered = False

# answered check for wether the user is changing one or all of their answers
answered2 = False

# answered check for the user choosing which one of their specific answers to change
answered3 = False

# does the user want to change an answer? yes = True no = False
change_ans = False

# Primary body of questions
print("\nHello! Welcome to this brand new prototype Coaching Chatbot. Please keep in mind: This is NOT a generative tool."
      "I will not be able to provide any real feedback for you, due to my current limitations. This tool in its current form is designed to be more of a self reflection tool.\n"
      "Everything we talk about to day will be based off of the 'GROW' method of Coaching. As such: I will now ask you"
      "four questions about what it is you're looking to achieve with Coaching.\n")

# Take input for the user's Goal
G = input("First up: What is your Goal you are looking to achieve? For some help with this, consider the following: "
          "What precisely are you looking to achieve and how would you define your goal?\n")
print("Okay! That all makes sense! Don't worry by the way, I'll review your answers with you later.")

# Take input for the Reality of the user's situation
R = input("Next: What is the Reality of your current situation? Consider the following: What's happening in your life "
          "right now? How will your situation impact your goal? What resources are available to you?\n")
print("Sounds good! We're half way there, keep it up!")

# Take input for what the user's options going forward are
O = input("Alright, what options do you have available to you? For help: Consider fully what options there are"
          "before you, how might each of these different options play out and also how you would rank all of these "
          "options.\n")
print("Alright, we're almost done now, just one more section to think about!")

# Take input for what is next for the user
W = input("Finally: What's next? How are you commit to a path forward with this? Think about: How committed you are "
          "to this goal, what are the first steps for you to take on this and what might get in your way\n")

# Show the user their final answers
print("With that, we're done! Just to confirm:\n"
      "Your Goal is: " + G + "!\n"
      "Your Reality is: " + R + "!\n"
      "Your Options are: " + O + "!\n"
      "Your What Next is: " + W + "!\n")

# Checking if the user would like to change any of their answers or not
while answered != True:
      ans = input("Are you satisfied with these answers, or would you like to change any of them upon further reflection?\n"
            "Please only answer with 'Change' or 'Leave', I won't be able to understand any other answers.\n").lower()
      
      # If they want to change them:
      if ans == "change":
            print("Okay! You're looking to change your answers, there's no harm in that!\n")
            answered = True
            change_ans = True

      # If they want to leave them as they are
      elif ans == "leave":
            print("Alright! Thank you again for using this chatbot, I hope you found your experience useful!\n")
            answered = True

      # Failsafe incase the user enters something that isn't "Change" or "Leave"
      else:
            print("I'm sorry, I don't understand? Please only reply with 'Change' or 'Leave'\n")

# If the user chooses to change their answers, they get sent to this area
if change_ans == True:
      print("Now, you can either choose to edit one specific answer, or all of them. Which is it that you'd like to do today?\n")
      
      while answered2 != True:
            one_or_all = input("Please either enter 'One' or 'All'.\n").lower()

            # If statement for user's choice of the above
            # Tree for just changing one of the answers
            if one_or_all == "one":
                  print("Okay! Which one in particular are you looking to change?\n")
                  one_num = input("Please enter the corresponding number:\n"
                        "1. Your Goal\n"
                        "2. Reality of your Situation\n"
                        "3. Your Options\n"
                        "4. What's next?\n")
                  
                  # Match (switch) statement to target which one of the four options the user wants to change
                  while answered3 != True:
                        match one_or_all:

                              # Changing the Goal
                              case 1:
                                    print("You've chosen to change your Goal! While I would reccommend in this case to go and review"
                                          "all of your answers, I'm more than happy to help you just change this one.\n")
                                    G = input("What is it that you'd like to change your goal to? Please enter it as if you were entering it for the first time\n")
                                    answered3 = True

                              # Changing the Reality
                              case 2:
                                    print("You've chosen to change the Reality of your Situation! That's completely understandable!\n")
                                    R = input("What is it you'd like to change the Reality to? Please enter it as if you were entering it for the first time\n")
                                    answered3 = True
                              
                              # Changing the Options
                              case 3:
                                    print("You've chosen to change what your options are! I hope there are more available to you than less!")
                                    O = input("What are your options now? Please enter it as if you were entering it for the first time\n")
                                    answered3 = True
                              
                              # Changing What's Next
                              case 4:
                                    print("You've chosen to change what's next for you! That's entirely understandable!")
                                    W = input("What is next for you now? Please enter it as if you were entering it for the first time\n")
                                    answered3 = True
                              
                              # Failsafe incase they enter anything that isn't valid
                              case _:
                                    print("Please only enter a valid number between 1 and 4 for your choice.\n")
                  
                  # Show the users their answers now with the amended answers
                  print("Okay! With your amended answer your answers now look like this!\n"
                        "Your Goal is: " + G + "!\n"
                        "Your Reality is: " + R + "!\n"
                        "Your Options are: " + O + "!\n"
                        "Your What Next is: " + W + "!\n"
                        "I hope this was a helpful experience for you! Please feel free to come back again if you want any more help!\n")
                  
                  answered2 = True

            # Tree for changing all of the user's answers instead of just one
            elif one_or_all == "all":
                  print("You want to change all your answers? No worries we can do that, just ensure you are taking plenty of time to think about each of your answers okay?\n")

                  # Take input for the user's Goal
                  G = input("First up: What is your Goal you are looking to achieve? For some help with this, consider the following: "
                              "What precisely are you looking to achieve and how would you define your goal?\n")
                  print("Okay! That all makes sense! Don't worry by the way, I'll review your answers with you later.")

                  # Take input for the Reality of the user's situation
                  R = input("Next: What is the Reality of your current situation? Consider the following: What's happening in your life "
                              "right now? How will your situation impact your goal? What resources are available to you?\n")
                  print("Sounds good! We're half way there, keep it up!")

                  # Take input for what the user's options going forward are
                  O = input("Alright, what options do you have available to you? For help: Consider fully what options there are"
                              "before you, how might each of these different options play out and also how you would rank all of these "
                              "options.\n")
                  print("Alright, we're almost done now, just one more section to think about!")

                  # Take input for what is next for the user
                  W = input("Finally: What's next? How are you commit to a path forward with this? Think about: How committed you are "
                              "to this goal, what are the first steps for you to take on this and what might get in your way\n")

                  print("Okay! With your amended answers your answers now look like this!\n"
                        "Your Goal is now: " + G + "!\n"
                        "Your Reality is now: " + R + "!\n"
                        "Your Options are now: " + O + "!\n"
                        "Your What Next is now: " + W + "!\n"
                        "I hope this was a helpful experience for you! Please feel free to come back again if you want any more help!\n")

                  answered2 = True
            else:
                  print("I'm sorry, I didn't understand that. Please enter only either 'One' or 'All'\n")
      
      # Exit the program once the user has finished changing their answers
      quit

else:
      quit