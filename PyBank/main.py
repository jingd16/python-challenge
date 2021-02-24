import os
import csv

#Define path to read + write CSV
csvpath = os.path.join("..", "Resource", "budget_data.csv")
output_file = os.path.join("..", "analysis", "PyBank.txt")

Total_Month_Counter = 0
Total_Net_Profit = 0
Month_change = 0
Average_change_list = []
sum_list = 0.00
Greatest_Increase = 0.00
Greatest_Increase_list = []
Greatest_Decrease = 0.00
Greatest_Decrease_list = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skip the header line
    csv_header = next(csvreader)

    for row in csvreader:
        #------------
        #Count and add up how many rows(month) is included
        #-------------
        Total_Month_Counter = Total_Month_Counter + 1
        
        #------------
        #total of profit/lose
        #------------
        Total_Net_Profit = Total_Net_Profit + int(row[1])

        #-------------
        #Work out the difference in each month and add to a list
        #-------------

        #Caculate the change between months + Append it to a list
        Month_change = int(row[1]) - Month_change
        Average_change_list.append(Month_change) 

        #Compare the Greatest_Increase value, and assign the data to a new list to save the month with greatest increase.
        if Month_change > Greatest_Increase:
            Greatest_Increase_list = [row[0], Month_change]
            Greatest_Increase = Month_change

        if Month_change < Greatest_Decrease:
            Greatest_Decrease_list = [row[0], Month_change]
            Greatest_Decrease = Month_change


        #Reset monthly_change to 0
        Month_change = int(row[1])

    #================
    #Print all the results in terminal
    #================

    print("Financial Analysis")
    print("------------------------------")
    print("Total Months: " + str(Total_Month_Counter))
    print("Total: $" + str(Total_Net_Profit))

    #Exclude the first difference before sum the list
    Average_change_list.pop(0)
    average_change = sum(Average_change_list) / len(Average_change_list)
    print("Average Change: $" + str(round(average_change,2)))

    #print(str(Greatest_Increase_list))
    print("Greatest Increase in Profits: " + str(Greatest_Increase_list[0]) + " ($" + str(Greatest_Increase_list[1]) + ")")

    #print(str(Greatest_Decrease_list))
    print("Greatest Decrease in Profits: " + str(Greatest_Decrease_list[0]) + " ($" + str(Greatest_Decrease_list[1]) + ")")


# Print all the results to a CSV file
with open(output_file, "w") as outputFile:
    csvwriter = csv.writer(outputFile)

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["------------------------------"])
    csvwriter.writerow(["Total Months: " + str(Total_Month_Counter)])
    csvwriter.writerow(["Total: $" + str(Total_Net_Profit)])
    csvwriter.writerow(["Average Change: $" + str(round(average_change,2))])
    csvwriter.writerow(["Greatest Increase in Profits: " + str(Greatest_Increase_list[0]) + " ($" + str(Greatest_Increase_list[1]) + ")"])
    csvwriter.writerow(["Greatest Decrease in Profits: " + str(Greatest_Decrease_list[0]) + " ($" + str(Greatest_Decrease_list[1]) + ")"])