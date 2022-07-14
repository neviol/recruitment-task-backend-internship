from solution_lib import incorrect_emails, search_email, emails_by_domain, emails_not_in_logs
import os

print("Hello, my name is Oleh Nevidomskyi\nMy Email: ole.nevidomskyi@gmail.com\n\n"
      "Please choose one of the options below to run the solutions:")


while True:
    usr_choice = int(input("\n1: Show incorrect emails.\n2: Search emails by text.\n3: "
                           "Group emails by domain.\n4: Find emails that are not in the logs files.\n\n"
                           "99: To stop the script.\n\nEnter a number: "))
    if usr_choice == 1:
        while True:
            inc_emails = input("\n99: Go Back\n1: Insert different path.\n\nEnter a number:")
            inc_emails = inc_emails.strip()
            if inc_emails == "99":
                break
            elif inc_emails == "1":
                path = input("Insert path: \n")
                incorrect_emails(path)
            else:
                print("INVALID INPUT")
    elif usr_choice == 2:
        while True:
            srch_emails = input("\n99: Go Back\n1: Insert different path.\n\nEnter a number:")
            srch_emails = srch_emails.strip()
            if srch_emails == "99":
                break
            elif srch_emails == "1":
                path = input("Insert path: \n")
                search_key = input("Insert the word you want to search by: ")
                search_email(path, search_key)
                break
            else:
                print("INVALID INPUT")
    elif usr_choice == 3:
        while True:
            grp_emails = input("\n99: Go Back\n1: Insert different path.\n\nEnter a number:")
            grp_emails = grp_emails.strip()
            if grp_emails == "99":
                break
            elif grp_emails == "1":
                path = input("Insert path: \n")
                emails_by_domain(path)
                break
            else:
                print("INVALID INPUT")
    elif usr_choice == 4:
        while True:
            log_emails = input("\n99: Go Back\n1: Insert different path.\n\nEnter a number:")
            log_emails = log_emails.strip()
            if log_emails == "99":
                break
            elif log_emails == "1":
                path = input("Insert path: \n")
                emails_not_in_logs(path)
                break
            else:
                print("INVALID INPUT")
    elif usr_choice == 99:
        print("I really want to be your intern!")
        break
