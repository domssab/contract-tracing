# Printing menu
print("Contact Tracing"
      "\nMenu: "
      "\n1 -> Add an item"
      "\n2 -> Search"
      "\n3 -> Exit")

#Main menu
mainmenu = 0
while mainmenu in (0,1,2,3)
      # Input for menu
      mainmenu = int(input("Choose what to do: "))
      if mainmenu == 1:
