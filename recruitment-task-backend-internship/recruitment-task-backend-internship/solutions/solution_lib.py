import os
import csv


def incorrect_emails(path):
    email_count = 0     # sum of incorrect emails
    invalid_emails = ""     # empty string for incorrect emails
    dirs = os.listdir(path)

    for filename in dirs:   # iterates through directory
        if filename.endswith(".csv"):   # checks if file is .csv
            with open(os.path.join(path, filename), 'r') as f:  # opens .csv
                csv_f = csv.reader(f)
                next(csv_f)     # skips the header
                for row in csv_f:   # iterates through rows in csv
                    row = ''.join(row)
                    identifier_csv = row.partition(';')     # separates the name and email using ";"
                    row = identifier_csv[2]
                    identifier_email_csv = row.partition('@')
                    dot_identifier_email_csv = identifier_email_csv[2].partition('.')
                    if len(identifier_email_csv[2]) < 1 or len(identifier_email_csv[0]) < 1 or line.count('@') > 1 or \
                            len(dot_identifier_email_csv[2]) < 1 or len(dot_identifier_email_csv[2]) > 5:    # checks for the amount of characters on each side of the @
                        email_count += 1    # ads the number of incorrect emails to the email_count variable
                        invalid_emails += row   # ads the incorrect emails to the invalid_emails variable
        else:
            with open(os.path.join(path, filename), 'r') as f:  # opens the file
                for line in f:  # iterates through lines in file
                    identifier_email_txt = line.partition('@')
                    dot_identifier_email_txt = identifier_email_txt[2].partition('.')
                    if len(identifier_email_txt[2]) < 1 or len(identifier_email_txt[0]) < 1 or line.count('@') > 1 or \
                            len(dot_identifier_email_txt[2]) < 1 or len(dot_identifier_email_txt[2]) > 5:
                        email_count += 1
                        invalid_emails += line

    print("Invalid emails ({}):\n{}".format(email_count, invalid_emails))


def search_email(path, string):
    email_count = 0     # sum of correct emails
    valid_emails = ""     # empty string for correct emails
    dirs = os.listdir(path)

    for filename in dirs:   # iterates through directory
        if filename.endswith(".csv"):   # checks if file is .csv
            with open(os.path.join(path, filename), 'r') as f:  # opens .csv
                csv_f = csv.reader(f)
                next(csv_f)     # skips the header
                for row in csv_f:   # iterates through rows in csv
                    row = ''.join(row)
                    identifier_csv = row.partition(';')     # separates the name and email using ";"
                    row = identifier_csv[2]
                    if string in row:   # checks if sting is in row
                        identifier_email_csv = row.partition('@')
                        dot_identifier_email_csv = identifier_email_csv[2].partition('.')
                        if len(identifier_email_csv[2]) >= 1 and len(identifier_email_csv[0]) >= 1  and line.count('@') == 1 and len(dot_identifier_email_csv[2]) > 1 and len(dot_identifier_email_csv[2]) < 5: # checks for the amount of characters on each side of the @
                            if row not in valid_emails:
                                if "\n" not in row:     # checks if the row will begin from a new line
                                    row = "    " + row
                                    valid_emails += row
                                    valid_emails += "\n"    # adds a new line if the row doesn't already have one
                                    email_count += 1
                                else:
                                    row = "    " + row
                                    valid_emails += row
                                    email_count += 1
        else:
            with open(os.path.join(path, filename), 'r') as f:  # opens the file
                for line in f:  # iterates through lines in file
                    if string in line:
                        identifier_email_txt = line.partition('@')
                        dot_identifier_email_txt = identifier_email_txt[2].partition('.')
                        if len(identifier_email_txt[2]) >= 1 and len(identifier_email_txt[0]) >= 1 and line.count('@') == 1 and len(dot_identifier_email_txt[2]) > 1 and len(dot_identifier_email_txt[2]) < 5:
                            if line not in valid_emails:
                                email_count += 1
                                line = "    " + line
                                valid_emails += line

    print("Found emails with \"{}\" in email ({}): \n{}".format(string, email_count, valid_emails))


def emails_by_domain(path):
    valid_emails_list = []      # empty list for correct emails
    domain_list = []

    dirs = os.listdir(path)

    for filename in dirs:   # iterates through directory
        if filename.endswith(".csv"):   # checks if file is .csv
            with open(os.path.join(path, filename), 'r') as f:  # opens .csv
                csv_f = csv.reader(f)
                next(csv_f)     # skips the header
                for row in csv_f:   # iterates through rows in csv
                    row = ''.join(row)
                    identifier_csv = row.partition(';')     # separates the name and email using ";"
                    row = identifier_csv[2]
                    identifier_email_csv = row.partition('@')
                    dot_identifier_email_csv = identifier_email_csv[2].partition('.')
                    if len(identifier_email_csv[2]) >= 1 and len(identifier_email_csv[0]) >= 1 and line.count('@') == 1 and len(dot_identifier_email_csv[2]) > 1 and len(dot_identifier_email_csv[2]) < 5:   # checks for the amount of characters on each side of the @
                        if row not in valid_emails_list:
                            if "\n" not in row:  # checks if the row will begin from a new line
                                valid_emails_list.append(row + "\n")
                            else:
                                valid_emails_list.append(row)
        else:
            with open(os.path.join(path, filename), 'r') as f:  # opens the file
                for line in f:  # iterates through lines in file
                    identifier_email_txt = line.partition('@')
                    dot_identifier_email_txt = identifier_email_txt[2].partition('.')
                    if len(identifier_email_txt[2]) >= 1 and len(identifier_email_txt[0]) >= 1 and line.count('@') == 1 and len(dot_identifier_email_txt[2]) > 1 and len(dot_identifier_email_txt[2]) < 5:
                        if line not in valid_emails_list:
                            if "\n" not in line:  # checks if the row will begin from a new line
                                valid_emails_list.append(line + "\n")
                            else:
                                valid_emails_list.append(line)

    valid_emails_list.sort()
    result = []
    for email in valid_emails_list:
        if email not in result:
            result.append(email)
    result.sort(key=lambda x: x.split('@')[1])

    areTheSame = lambda x, y: x.partition('@')[2] == y.partition('@')[2]
    sorted_emails_list = []
    for w in result:
        l = next((x for x in sorted_emails_list if areTheSame(w, x[0])), [])
        if l == []:
            sorted_emails_list.append(l)
        l.append("    " + w)

    for l_email in sorted_emails_list:
        emails_count = 0
        for email in l_email:
            email_domain = email.partition('@')[2][:-1]
            emails_count += 1
        l_email.insert(0, "\nDomain {} ({}):".format(email_domain, emails_count))


    res = ['\n'.join(ele) for ele in sorted_emails_list]
    res = ''.join(res)
    print(res)



def emails_not_in_logs(path):
    valid_emails_list = []      # empty list for correct emails
    domain_list = []
    email_count = 0

    dirs = os.listdir(path)

    for filename in dirs:   # iterates through directory
        if filename.endswith(".csv"):   # checks if file is .csv
            with open(os.path.join(path, filename), 'r') as f:  # opens .csv
                csv_f = csv.reader(f)
                next(csv_f)     # skips the header
                for row in csv_f:   # iterates through rows in csv
                    row = ''.join(row)
                    identifier_csv = row.partition(';')     # separates the name and email using ";"
                    row = identifier_csv[2]
                    identifier_email_csv = row.partition('@')
                    dot_identifier_email_csv = identifier_email_csv[2].partition('.')
                    if len(identifier_email_csv[2]) >= 1 and len(identifier_email_csv[0]) >= 1 and line.count('@') == 1 and len(dot_identifier_email_csv[2]) > 1 and len(dot_identifier_email_csv[2]) < 5:   # checks for the amount of characters on each side of the @
                        if row not in valid_emails_list:
                            if "\n" not in row:  # checks if the row will begin from a new line
                                row = row.strip()
                                valid_emails_list.append(row + "\n")
                            else:
                                row = row.strip()
                                valid_emails_list.append(row)

        elif filename.endswith(".txt"):
            with open(os.path.join(path, filename), 'r') as f:  # opens the file
                for line in f:  # iterates through lines in file
                    identifier_email_txt = line.partition('@')
                    dot_identifier_email_txt = identifier_email_txt[2].partition('.')
                    if len(identifier_email_txt[2]) >= 1 and len(identifier_email_txt[0]) >= 1 and line.count('@') == 1 and len(dot_identifier_email_txt[2]) > 1 and len(dot_identifier_email_txt[2]) < 5:
                        if line not in valid_emails_list:
                            if "\n" not in line:  # checks if the row will begin from a new line
                                line = line.strip()
                                valid_emails_list.append(line + "\n")
                            else:
                                line = line.strip()
                                valid_emails_list.append(line)
    valid_emails_list.sort()
    result = []
    for email in valid_emails_list:
        if email not in result:
            result.append(email)

    for filename in dirs:

        if filename.endswith(".logs"):
            with open(os.path.join(path, filename), 'r') as log:
                filecontent = log.readlines()
                storage = []
                for line in filecontent:
                    line = line.strip()
                    line = line.split(" ")[-1]
                    line = line.strip("'")
                    storage.append(line)


    storage.sort()
    result.sort()
    list_difference = []
    for email in result:
        if email not in storage:
            email = "   " + email
            if email.endswith("\n"):
                email = email.replace("\n", "")
            if email not in list_difference:
                    list_difference.append(email)
                    email_count += 1



    list_difference = "\n".join(list_difference)
    print("Emails not sent ({})\n{}".format(email_count, list_difference))
