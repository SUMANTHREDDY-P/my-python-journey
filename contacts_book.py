
#---------------Quation ---------------
# build a contact book using nested dicts/lists with search & sort  
#---------------answer-------------
contacts = [
    { "name": "Ananya Singh", "number": "+91 91234 56789" },
    { "name": "Vivaan Patel", "number": "+91 93456 78901" },
    { "name": "Diya Iyer", "number": "+91 94567 89012" },
    { "name": "Aditya Verma", "number": "+91 95678 90123" },
    { "name": "Ishaan Gupta", "number": "+91 96789 01234" },
    { "name": "Aaradhya Joshi", "number": "+91 97890 12345" },
    { "name": "Kabir Rao", "number": "+91 98901 23456" },
    { "name": "Meera Nair", "number": ["+91 99012 34567" ,"+91 98024 68024" ]},
    { "name": "Sai Reddy", "number": "+91 90123 45678" },
    { "name": "Reyansh Das", "number": "+91 91122 33445" },
    { "name": "Prisha Chatterjee", "number": "+91 92233 44556" },
    { "name": "Krishna Menon", "number": "+91 93344 55667" },
    { "name": "Ahana Bose", "number": ["+91 94455 66778" , "+91 99900 11223"] },
    { "name": "Aryan Kulkarni", "number": "+91 95566 77889" },
    { "name": "Saanvi Deshmukh", "number": ["+91 96677 88990" , '+91 94680 13579'] },
    { "name": "Samaira Joshi", "number": "+91 94758 69708" },
    { "name": "Yuvan Jain", "number": "+91 95869 70819" },
    { "name": "Kavya Agrawal", "number": "+91 96970 81920" },
    { "name": "Ayaan Bansal", "number": "+91 97081 92031" },
    { "name": "Navya Garg", "number": "+91 98192 03142" },
    { "name": "Vivaan Goel", "number": "+91 99203 14253" },
    { "name": "Isha Singhal", "number": ["+91 90314 25364" , '91 96802 46802'] },
    { "name": "Ranveer Kaul", "number": "+91 91526 37485" },
    { "name": "Kiara Dhar", "number": "+91 92637 48596" },
    { "name": "Shlok Handoo", "number": "+91 93748 59607" },
    { "name": "Siya Razdan", "number": "+91 94859 60718" },
    { "name": "Advait Tikoo", "number": "+91 95960 71829" },
    { "name": "Hazel Wanchoo", "number": "+91 96071 82930" },
    { "name": "Tushar Bhatia", "number": ["+91 97182 93041","92536 47586"] },
    { "name": "Ridhima Anand", "number": "+91 98293 04152" },
    { "name": "Laksh Khurana", "number": "+91 99304 15263" },
    { "name": "Khushi Grover", "number": "+91 90415 26374" }
]
while True:

        print("\n --- CONTACT MENU ---")
        print("1. View All Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Sort & View (A-Z)")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")


        # 1. VIEW ALL
        if choice == "1":
            print("\n--- All Contacts ---")
            for item in contacts:
                # Join multiple numbers into a single comma-separated string
                all_nums = "".join(item["number"])
                print(f"{item['name']} : {all_nums}")

        # 2. ADD CONTACT
        elif choice == "2":
            print("\n--- Add Contact ---")
            new_name = input("Enter name: ")

            # Collect multiple numbers into a plain list
            new_numbers = []
            adding = True
            while adding:
                num = input("Enter phone number: ")
                new_numbers.append(num)

                more = input("Add another number? (y/n): ")
                if more.lower() != "y":
                    adding = False

            # Create a new dictionary and append it to our main list
            new_contact = {"name": new_name, "number": new_numbers}
            contacts.append(new_contact)
            print("✅ Contact added!")

        # 3. SEARCH CONTACT
        elif choice == "3":
            print("\n--- Search ---")
            query = input("Search name or number: ").lower()

            # Track whether we found at least one match
            found_any = False

            for item in contacts:
                # Check if search string matches name
                name_match = query in item["name"].lower()

                # Check if search string matches any number in the list
                number_match = False
                for num in item["number"]:
                    if query in num:
                        number_match = True

                # If we find a match, print it and turn our flag to True
                if name_match or number_match:
                    all_nums = "".join(item["number"])
                    print(f"Found 🔍 {item['name']} : {all_nums}")
                    found_any = True  # We found someone!

            # Exception Check: If our flag is still False after checking everyone
            if not found_any:
                print("❌ No contact found matching your search query.")
        # 4. SORT BY NAME (A-Z)
        elif choice == "4":
            print("\n--- Sorted A-Z ---")

            # Step 1: Create a simple list of just the names, then sort it alphabetically
            names_only = []
            for item in contacts:
                names_only.append(item["name"])
            names_only.sort()

            # Step 2: Loop through the sorted names, find the matching dictionary, and print it
            for sorted_name in names_only:
                for item in contacts:
                    if item["name"] == sorted_name:
                        all_nums = "".join(item["number"])
                        print(f"{item['name']} : {all_nums}")

        # 5. EXIT
        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option. Try again")

