while True:
    # Display the main menu and prompt for user input
    print("Choose your option:\n\t1 (Encrypt)\n\t2 (Decrypt)\n\t3 (Exit)")
    choice = input("Your Choice: ")

    if choice == "1":
        # If the user chooses 1 (Encrypt)
        plain_text = input("Text: ")
        encrypt_text = ""
        for c in plain_text:
            # Encrypt each character by doubling its ASCII value and adding 5
            x = ord(c) * 2 + 5
            encrypt_text += chr(x)
        # Display the encrypted text
        print("Encrypted Text: ", encrypt_text)
        print("*" * 40 + "\n")
    
    elif choice == "2":
        # If the user chooses 2 (Decrypt)
        encrypt_text = input("Encrypted Text: ")
        plain_text = ""
        for c in encrypt_text:
            # Decrypt each character by reversing the encryption process
            x = (ord(c) - 5) // 2
            plain_text += chr(x)
        # Display the decrypted text
        print("Decrypted Text: ", plain_text)
        print("*" * 40 + "\n")
    
    elif choice == "3":
        # If the user chooses 3 (Exit)
        print("Bye!")
        print("*" * 40 + "\n")
        break
    
    else:
        # If the user enters an invalid option
        print("Your choice is wrong!")
        print("*" * 40 + "\n")
