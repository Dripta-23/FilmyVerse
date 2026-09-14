#MAIN CODE
import mysql.connector as org
import pickle
# ---------------- Global lists ----------------
Plans = ["1 year: 499/-", "3 months: 149/-", "1 month: 49/-"]
Items = ["Movie", "Web Series", "Anime"]
available_languages = ["Hindi", "Bengali", "English"]
Genres = ["Comedy", "Action", "Sci-Fi", "Crime-Thriller", "Drama", "Educational"]
# ---------------- Global Variables ----------------
attempts = 3
buffInSec = 1
dbName = "class_12_computer_project"
exit_flag = False
conn = None
cur = None
# ---------------- Watch menu ----------------
def watch_choice():
    print()
    print("Opening Watch Menu... Please wait...")
    print("Choose the type of content you want to browse.")
    print()
    sleep(buffInSec)
    print("=" * 60)
    spaces = (60 - len("WATCH CHOICE")) // 2
    print(" " * spaces + "WATCH CHOICE")
    print("=" * 60)
    print("1) Movie                       - Browse movies across industries and languages")
    print("2) Web Series                  - Browse web series titles and seasons")
    print("3) Anime                       - Browse anime titles")
    print("0) Return to Main Menu")
    print("=" * 60)
    try:
        ch = int(input("Enter your choice: "))
        print()
        sleep(buffInSec)
        if ch in [1, 2, 3]:
            language_selection(ch, ["Hindi", "Bengali", "English"])
        elif ch == 0:
            print("Loading...")
            main()
        else:
            print("Invalid choice. Returning to Watch menu.")
            watch_choice()
    except ValueError:
        print("Enter a valid number. Returning to watch menu.")
        watch_choice()
# ---------------- Language selection ----------------
def language_selection(choice, available_languages):
    print()
    print("Please select your preferred language for streaming...")
    print("Select one of the options below to continue.\n")
    spaces = (60 - len("LANGUAGE MENU")) // 2
    print(" " * spaces + "LANGUAGE MENU")
    print("=" * 60)
    for i in range(len(available_languages)):
        print(str(i + 1) + ") " + available_languages[i] + "                - Browse titles in " + available_languages[i])
    print(str(len(available_languages) + 1) + ") Return to Watch Menu")
    print("0) Return to Main Menu")
    print("=" * 60)
    try:
        ch1 = int(input("Enter your language choice: "))
        print()
        print("Processing your language choice...")
        sleep(buffInSec)
        if ch1 < 0 or ch1 > len(available_languages) + 1:
            print("Invalid choice. Returning to Language selection menu ")
            language_selection(choice, available_languages)
        elif ch1 == 0:
            main()
        elif ch1 == len(available_languages) + 1:
            watch_choice()
        else:
            genre_selection(choice, available_languages[ch1 - 1])
    except ValueError:
        print("Enter a number. Returning to Language menu.")
        language_selection(choice, available_languages)
# ---------------- Genre selection ----------------
def genre_selection(choice, selected_language):
    print()
    print("Loading genres... Please wait...")
    print("Choose a genre to filter titles. You can go back if needed.")
    print()
    sleep(buffInSec)
    spaces = (60 - len("GENRE")) // 2
    print(" " * spaces + "GENRE")
    print("=" * 60)
    for i in range(len(Genres)):
        print(str(i + 1) + ") " + Genres[i] )
    print(str(len(Genres) + 1) + ") Return to Language Menu")
    print("0) Return to Main Menu")
    print("=" * 60)
    try:
        ch2 = int(input("Enter your choice: "))
        print()
        if ch2 < 0 or ch2 > len(Genres) + 1:
            print("Invalid choice. Returning to Genre selection menu.")
            genre_selection(choice, selected_language)
        elif ch2 == 0:
            main()
        elif ch2 == len(Genres) + 1:
            print("Returning to language menu............")
            language_selection(choice, available_languages)
        else:
            selected_genre = Genres[ch2 - 1]
            selected_type = Items[choice - 1]
            print("Preparing your selected category...")
            sleep(buffInSec)
            print()
            print("You selected: " + selected_type + " | " + selected_language + " | " + selected_genre)
            print("=" * 60)
            sleep(buffInSec)
            # File paths are relative for portability.
            if selected_type == "Movie":
                display_content("movies_full.dat", selected_genre, selected_language, "Movie",choice) 
            elif selected_type == "Web Series":
                display_content("webseries_full.dat", selected_genre, selected_language, "Web Series",choice)
            elif selected_type == "Anime":
                display_content("anime_full.dat", selected_genre, selected_language, "Anime",choice)
    except ValueError:
        print("Enter a number. Returning to genre selection menu.")
        genre_selection(choice, selected_language)
# ---------------- Display content menu ----------------
def display_content(filename, selected_genre, selected_language, selected_type, choice):
    print("Loading available titles... Please wait...")
    print()
    sleep(buffInSec)
    try:
        f = open(filename, "rb") 
    except FileNotFoundError:
        print("Data file '" + filename + "' not found. Returning to main menu.")
        print()
        return
    try:
        all_records = pickle.load(f)
    except Exception:
        print("Could not read data file. Returning to main menu.")
        f.close()
        return
    f.close()
    filtered = []
    for rec in all_records:
        if str(rec[3]).lower() == selected_genre.lower() and str(rec[2]).lower() == selected_language.lower():
            filtered.append(rec)
    if len(filtered) == 0:
        print("No " + selected_type + "s found for genre '" + selected_genre + "' in " + selected_language + ".")
        return
    print("Found " + str(len(filtered)) + " results.")
    sleep(buffInSec)
    while True:
        print()
        print("=" * 80)
        if selected_type == "Anime":
            print("1) Show by Year                     - Filter anime titles by release year")
            print("2) Show all                         - Show all matching anime titles")
            print("3) Back to genre selection menu")
            print("0) Back to main menu")
        else:
            print("1) Categorize by Industry           - Group titles by industry (Bollywood, Hollywood, etc.)")
            print("2) Show by Year                     - Filter titles by release year")
            print("3) Show all                         - List all matching titles")
            print("4) Back to genre selection menu")
            print("0) Back to main menu")
        print("=" * 80)
        try:
            opt = int(input("Enter your choice: "))
            print()
            print("Loading...")
            sleep(buffInSec)
            if selected_type == "Anime":
                if opt == 1:
                    show_by_year(filtered)
                elif opt == 2:
                    display_titles(filtered)
                elif opt == 3:
                    genre_selection(choice, selected_language)
                    break
                elif opt == 0:
                    main()
                    break
                else:
                    print("Invalid option.")
            else:
                if opt == 1:
                    categorize_by_industry(filtered)
                elif opt == 2:
                    show_by_year(filtered)
                elif opt == 3:
                    display_titles(filtered)
                elif opt == 4:
                    genre_selection(choice, selected_language)
                    break
                elif opt == 0:
                    main()
                    break
                else:
                    print("Invalid option.")
        except ValueError:
            print("Enter a valid number.")
# ---------------- Features ----------------
def categorize_by_industry(records):
    print("Now categorizing by industry... Please wait...")
    sleep(buffInSec)
    industries = []
    for r in records:
        ind = r[4]
        if ind not in industries:
            industries.append(ind)
    if len(industries) == 0:
        print("No industry information available.")
        return
    for ind in industries:
        print()
        print("=" * 80)
        print(ind.upper())
        print("=" * 80)
        group = []
        for r in records:
            if r[4] == ind:
                group.append(r)
        display_titles(group)
def show_by_year(records):
    print()
    sleep(buffInSec)
    try:
        yr = int(input("Enter the year: "))
        print("Now showing titles by year...")
        found = []
        for r in records:
            if r[1] == yr:
                found.append(r)
        if len(found) == 0:
            print("No titles found for the year " + str(yr) + ".")
        else:
            print("=" * 80)
            print("Titles released in " + str(yr))
            print("=" * 80)
            display_titles(found)
    except ValueError:
        print("Enter a valid year.")
def display_titles(records):
    print()
    print("Please Wait...Loading titles...")
    sleep(buffInSec)
    for r in records:
        print("-" * 80)
        print("Title      : " + str(r[0]))
        print("Year       : " + str(r[1]))
        print("Language   : " + str(r[2]))
        print("Genre      : " + str(r[3]))
        print("Industry   : " + str(r[4]))
        print("Director   : " + str(r[5]))
        print("IMDB       : " + str(r[6]))
        print("Type       : " + str(r[7]))
        print("Seasons    : " + str(r[8]))
        print("Duration   : " + str(r[9]))
        print("Main Cast  : " + str(r[10]))
        print("Summary    : " + str(r[11]).split('\\n')[0])
        sleep(buffInSec)
        if "\\n" in str(r[11]):
            print("             " + str(r[11]).split('\\n')[1])
    print("-" * 80)
    print()
# ---------------- Database and account functions ----------------
def check_database_existence():
    global cur, conn, dbName
    print("Checking if database exists...")
    sleep(buffInSec)
    try:
        cur.execute("show databases")
        found = False
        for row in cur:
            if row[0] == dbName:
                found = True
                break
        cur.fetchall() 
        if not found:
            print("Database not found. Creating new database...")
            sleep(buffInSec)
            create_new_database()
        else:
            cur.execute("use " + dbName) 
            print()
            print("Welcome to FiLMYVERSE — your personalized OTT terminal.")
            print("Please follow the on-screen prompts to navigate the app.")
            print()
            print("=" * 60)
            print()
            print("Please wait... loading interface...")
            sleep(buffInSec)
            main()
    except org.Error as e:
        pass
# ---------------- Database Creation ----------------
def create_new_database():
    global cur, conn, dbName
    print("Creating new database for FiLMYVERSE...")
    sleep(buffInSec)
    try:
        cur.execute("create database " + dbName)
        cur.execute("use " + dbName)
        cur.execute("""
            create table user_info (
                username varchar(50) not null,
                email_id varchar(100) not null,
                password varchar(50) not null,
                subscription_status varchar(50))""")
        conn.commit()
        print("Database created successfully!")
    except org.Error as e:
        print("Database creation error:", e)
    finally:
        enter_data_in_database()
# ---------------- Account creation ----------------
def enter_data_in_database():
    global conn, cur
    print()
    print("Starting account creation process...")
    print()
    sleep(buffInSec)
    try:
        username = input("Enter username: ")
        print()
        i=0
        while i<3:
            email = input("Enter email id: ")
            print()
            print("Validating email format...")
            sleep(buffInSec)
            x = email.split("@")
            y = email.split(".")
            if "@" not in email or "." not in email or len(x) < 2 or len(y) < 2 or len(x[1]) < 1 or len(y[-1]) < 1 or " " in email:
                print("Invalid email format. Attempts left", 2-i)
                print()
                i+=1
            else:
                break
        if i==3:
            enter_data_in_database() 
            return
        for attempt in range(attempts):
            print()
            print("Now verifying your password input...")
            print()
            sleep(buffInSec)
            print("Let's secure your account with a strong password.")
            print()
            print("Password must be at least 8 characters long.")
            print()
            print("It must include at least one special character (!@#$%^&*_-|=<>).")
            print()
            pwd = input("Enter password: ")
            print()
            special = 0
            for c in pwd:
                if c in "!@#$%^&*_-|=<>":
                    special = 1
                    break
            if len(pwd) >= 8 and special == 1:
                print("Password accepted. Remember Your Password")
                print("Proceeding to subscription plans...")
                print()
                sleep(buffInSec)
                plan = subscription_plan()
                cur.execute("insert into user_info (username,email_id,password,subscription_status) values (%s,%s,%s,%s)", (username, email, pwd, plan))
                conn.commit()
                print()
                print("Account created successfully. Redirecting to Watch Menu...")
                print()
                sleep(buffInSec)
                watch_choice()
                return
            else:
                print("Invalid password. Attempts left:", 2 - attempt)
        print("Too many failed attempts.")
    finally:
        pass
# ---------------- Subscription plan ----------------
def subscription_plan():
    print("Displaying available subscription plans...")
    sleep(buffInSec)
    for attempt in range(attempts):
        print()
        print("Subscription Plans:")
        for i in range(len(Plans)):
            print(str(i + 1) + ") " + Plans[i])
        try:
            ch = int(input("Enter your choice: "))
            print()
            if ch not in [1, 2, 3]:
                print(attempts-(attempt+1), "attempts remaining..")
                continue
            expected_amount = int(Plans[ch - 1].split(': ')[1].replace('/-', ''))
            amt = int(input("Enter amount: "))
            print("Verifying payment and plan selection...")
            print()
            sleep(buffInSec)
            if amt == expected_amount:
                print("Subscription activated successfully!")
                print()
                sleep(buffInSec)
                return Plans[ch - 1]
            else:
                print("Incorrect plan or amount.")
                print(attempts-(attempt+1), "attempts remaining..")
                print()
        except ValueError :
            print(attempts-(attempt+1), "attempts remaining..")
            print("Enter valid numbers.")
    print("Too many invalid attempts for subscription.")
    main() 
# ---------------- Login function ----------------
def check_user_info():
    global conn, cur
    print("Loading login page...")
    print()
    sleep(buffInSec)
    try:
        total_attempts = 3
        while total_attempts > 0:
            username = input("Enter username: ")
            print()
            print("Checking username in database...")
            print()
            sleep(buffInSec)
            cur.execute("select username,password from user_info where username=%s", (username,))
            row = cur.fetchone()
            if not row:
                total_attempts -= 1
                print("User not found.")
                print("Attempts left:", total_attempts)
                print()
                continue
            pwd = input("Enter password: ")
            print()
            print("Now verifying your password...")
            print()
            sleep(buffInSec)
            if pwd == row[1]:
                print("Password verified...")
                print()
                print("Login successful! Redirecting to Watch Menu...")
                print()
                sleep(buffInSec)
                watch_choice()
                return
            else:
                total_attempts -= 1
                print("Wrong password.")
                print("Attempts left:", total_attempts)
                print()
        print("Too many wrong attempts.")
        print()
        sleep(buffInSec)
        print("Returning to main menu...")
        print()
        sleep(buffInSec)
        main()
    finally:
        pass
# ---------------- Sleep and Exit function ----------------
def sleep(buffInSec):
    if cur:
        cur.execute("select sleep(" + str(buffInSec) + ")")
        cur.fetchone()
def exit():
    global conn, cur, exit_flag
    print("Exitting ...")
    exit_flag = True
    try:
        if cur:
            cur.close()
        if conn and conn.is_connected():
            conn.close()
    except:
        pass
# ---------------- Main menu ----------------
def main():
    global exit_flag
    while not exit_flag:
        print()
        print("=" * 60)
        spaces = (60 - len("MAIN MENU")) // 2
        print(" " * spaces + "MAIN MENU")
        print("=" * 60)
        print("1) Create account    - Create a new FiLMYVERSE account")
        print("2) Login             - Login to your existing account")
        print("0) Exit              - Close the application")
        print("=" * 60)
        try:
            print()
            choice = int(input("Enter your choice: "))
            print()
            if choice == 1:
                print("Redirecting to account creation section...")
                sleep(buffInSec)
                enter_data_in_database()
            elif choice == 2:
                print("Redirecting to login page...")
                print()
                sleep(buffInSec)
                check_user_info()
            elif choice == 0:
                print("Exiting the FiLMYVERSE application...")
                sleep(buffInSec)
                print("Thank you for using FiLMYVERSE. Goodbye!")
                exit_flag = True
                exit()
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Enter a valid number.")
# ---------------- Program start ----------------
try:
    conn = org.connect(host="localhost",
                      user="root",
                      password="")
    cur = conn.cursor()
except org.Error as e:
    print("Database connection error:", e)
    exit()
try:
    print()
    check_database_existence() 
except KeyboardInterrupt:
    print("\nKeyboard Interruption Error")
    exit()
if not exit_flag:
    exit()
