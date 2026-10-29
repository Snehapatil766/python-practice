import tkinter as tk

# Submit button function
def submit():
    name = name_entry.get()
    age = age_entry.get()
    mobile = mobile_entry.get()
    gmail = gmail_entry.get()

    # Append data into text file
    with open("data.txt", "a") as file:
        file.write(name + "," + age + "," + mobile + "," + gmail + "\n")

    print("Data submitted successfully")


# Read button function
def read_data():
    with open("data.txt", "r") as file:

        print("\nName\tAge\tMobile Number\tGmail")
        print("-" * 65)

        for line in file:
            data = line.strip().split(",")

            print(data[0], "\t", data[1], "\t", data[2], "\t", data[3])


# Create window
root = tk.Tk()
root.title("Data Collection")
root.geometry("400x300")

# Name
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Age
tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

# Mobile Number
tk.Label(root, text="Mobile Number").pack()
mobile_entry = tk.Entry(root)
mobile_entry.pack()

# Gmail
tk.Label(root, text="Gmail").pack()
gmail_entry = tk.Entry(root)
gmail_entry.pack()

# Submit button
tk.Button(root, text="Submit", command=submit).pack(pady=10)

# Read button
tk.Button(root, text="Read", command=read_data).pack()

# Run the window
root.mainloop()