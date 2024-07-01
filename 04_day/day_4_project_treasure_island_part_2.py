# LINK: https://ascii.co.uk/art

print('''
********************************************************************
        
               |--__
                                 |
                                 X
                        |-___   / \       |--__
                        |      =====      |
                        X      | .:|      X
                       / \     | O |     / |
                      =====   |:  . |   =====
                      |.: |__| .   : |__| :.|
                      |  :|. :  ...   : |.  |
              __   __W| .    .  ||| .      :|W__  --
            -- __  W  WWWW______"""______WWWW   W -----  --
        -  -     ___  ---    ____     ____----       --__  -
            --__    --    --__     -___        __-   _
********************************************************************           
''')

print("\n Welcome to Adventure Castle. \n")
print("Your mission is to find the treasure. \n")

choice1 = input('You are in front of the front door. You choose: A / B / C\n\nType A - To ring the bell.\nType B - To enter the door.\nType C - To clap and call.\n\nChoose Now!!!\n').lower()
if choice1 == "a":
   print("Suddenly you realize that the ground has disappeared...\nYou fall into an endless dark hole...\nEchoing your scream...\nUaáááááááááa\n\nGAME OVER\n")

elif choice1 == "b":
  choice3 = input('You\'re at a hall. In it is a butler with a shotgun pointed at you. You choose:\n\nType D - To talk to him.\nType E - Raise your hands and approach him.\n\n').lower()
  if choice3 == "d":
    print("SThe butler fires the shot into his chest. This is the last vision you have. GAME OVER")
  else:
    print("The butler recognizes you as his son and heir to his fortune. Congratulations the Treasure is his. YOU WIN")

else:
  print("Suddenly you realize that the ground has disappeared...\nYou fall into an endless dark hole...\nEchoing your scream...\nUaáááááááááa\n\nGAME OVER\n")