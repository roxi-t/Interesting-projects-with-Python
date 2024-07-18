while True :
    print("Choose your option :\n\t1(Encrypt\n\t2(Decrypet\n\t3(Exit")
    choice = input("Your Choice : ") 
    if choice == "1" :
       plain_text = input("text : ")
       Encrypt_text = ""
       for c in plain_text :
           x = ord(c) * 2 +5
           Encrypt_text += chr(x)
       print("Encrypt_text : " , Encrypt_text)
       print("*"*40 +"\n")
    elif choice == "2" :
        Encrypt_text = input("Encrypt_text : ")
        plain_text = ""
        for c in Encrypt_text :
           x = (ord(c) -5) // 2
           plain_text += chr(x)
        print("plain_text : " , plain_text)
        print("*"*40 +"\n")
    elif choice == "3" :
         print("bye!")
         print("*"*40 +"\n")
         break
    else:
        print("your choice is wronge ! ")
        print("*"*40 +"\n")