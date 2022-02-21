import sys
import clipboard
import json

#clipboard.copy("ABC")
SAVED_DATA = "clipboard.json"

def save_item(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_item(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}
if len(sys.argv) == 2:
    document = sys.argv[1]
    data = load_item(SAVED_DATA)

    if document == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_item(SAVED_DATA, data)
        print("Data saved!")

    elif document == "load":
        key = input("Enter a key: ")

        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist")
        
    
    elif document == "list":
        for i in data:
            print(f"{i}: {data[i]}")
    
    else:
        print("Unknown variable")

else:
    print("Please pass exactly one command!!")