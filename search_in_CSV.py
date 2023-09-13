import csv


# Function to search for text in a CSV file (case-insensitive)
def search_csv(filename, search_text):
    found_rows = []
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)

        # Loop through each row in the CSV file
        for row in csvreader:
            # Loop through each cell in the row
            for cell in row:
                if search_text.lower() in cell.lower():
                    found_rows.append(row)
                    break  # Break out of the inner loop once a match is found

    return found_rows


# Full path to the CSV file
csv_path = "/Users/mirekch/PycharmProjects/pythonProject/wydatki.csv"

# Input for the text to search for
search_text = input("Enter the text to search for: ")

# Perform the case-insensitive search
found_rows = search_csv(csv_path, search_text)

# Display the results
if found_rows:
    print("Found the following rows:")
    for row in found_rows:
        print(row)
else:
    print("Text not found in the CSV file.")
