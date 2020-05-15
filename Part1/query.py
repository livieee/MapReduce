import sys
import csv


# name of csv file
def main():
    input_city = input("Enter the City: ")
    filename = "cityInformation"
    file = open(filename)
    match = False
    for row in file:
        row = row.split()
        city = row[0]
        count = row[1]
        if input_city.lower() in city.lower():
            print(city + ": " + count)
            match = True
    if not match:
        print("No information of " + input_city)

if __name__ == "__main__":
    main()


