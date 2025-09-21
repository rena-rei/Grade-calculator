Math_ums  = []
Sci_ums = []

def main():
    while True:
        choice = input("\nChoose a subject (Math / Physics / Biology / Chemistry) or type 'exit' to quit: ").strip().lower()
        if choice == "math":
            if math() == None: 
                print ("Exited")
        elif choice in ["physics", "biology", "chemistry"]:
            if science(choice) == None:
                print ("Exited")
        elif choice == "exit":
            return
        else:
            print("Please enter a valid subject: ")

def math():
    global Math_ums
    Math_ums = []
    for i in range(6):
            index = f"pure {i+1}" if i+1 in [1, 2, 3, 4] else  f"optional unit {i-3}"
            ums = get_ums(100, index)
            if ums == None:
                return None
            else:
                Math_ums.append(ums)
    t_ums = sum(Math_ums)
    if t_ums >= 480 and (Math_ums[2] + Math_ums[3] >= 180):
        print(f"Overall got an A* with {t_ums} ums.")
    else:
        if t_ums <= 480:
            print(f"Cannot achieve an A* as you lack {480-t_ums} ums.")
            grade(t_ums, "math")
        elif (Math_ums[2] + Math_ums[3] <= 180):
            print(f"Cannot achieve an A* as you didn't perform at 90%.")
            grade(t_ums, "math")

def science(subject):
    global Sci_ums
    Sci_ums = []
    for i in range(6):
        ums_max = 120 if i+1 in [1, 2, 4, 5] else 60
        ums = get_ums(ums_max, f"Unit {i+1}" )
        if ums == None:
            return None
        else:
            Sci_ums.append(ums)
    t_ums = sum(Sci_ums)
    if t_ums >= 480 and (sum(Sci_ums[3:6]) >= 270):
        print(f"Overall got an A* with {t_ums} ums in {subject}.")
    else:
        if t_ums < 480:
            print(f"Cannot achieve an A* as you lack {480-t_ums} ums.")
            grade(t_ums, subject)
        elif (sum(Sci_ums[3:6]) <= 270):
            print(f"Cannot achieve an A* as you didn't perform at 90%.")
            grade(t_ums, subject)      
            
def grade(total_ums, subject):
    thresholds = {
        480: "A",
        420: "B",
        360: "C",
        300: "D",
        240: "E"
    }
    
    for threshold, grade in thresholds.items():
        if total_ums >= threshold:
            print(f"Overall got an {grade} in {subject} with {total_ums} ums")
            return
    
    print(f"Unclassified in {subject}")

def get_ums(ums_max, index):
    while True:
        try:
            ums = input(f"Enter the ums out of {ums_max} for {index} or type 'exit' to quit: ").lower()
            if ums == "exit":
                return None
            elif int(ums) <= ums_max:
                return int(ums)
            elif int(ums) >= ums_max:
                print(f"Maximum for this unit is {ums_max}")
        except ValueError:
            print("Invalid input. Please enter a valid integer or type 'exit' to quit.")

if __name__ == "__main__":
    main()
