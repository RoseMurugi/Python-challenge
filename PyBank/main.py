# pybank Homework Rose Wachira

# Import modules

import csv
import os

# Create path for files
budget = os.path.join('Resources','budget_data.csv')
analysis = os.path.join('Resources','analysis_data.text')

 
 # define variables
NumMonths = 0
Revenue = 0
TTRevenue = 0
GProfit_decrease = 0
GProfit_increase = 0
Month_GIncrease = ""
Month_GDecrease = ""
title = str("Financial Analysis")
 
 
with open(budget) as budget_data:

    budget_data_read = csv.reader(budget_data)
    next(budget_data_read)
 
    for row in budget_data_read:

        NumMonths+=1

        CurMonth = row[0]

        CurRevenue = int(row[1])

 
        RevenueChange= CurRevenue - Revenue

        if RevenueChange > GProfit_increase:

            Month_GIncrease = CurMonth

            GProfit_increase = RevenueChange

        if RevenueChange < GProfit_decrease:

            Month_GDecrease = CurMonth

            GProfit_decrease = RevenueChange

 
        Revenue = CurRevenue

        TTRevenue += CurRevenue

 

    AvgRevenue = TTRevenue/NumMonths

    AvgRev2= round(AvgRevenue,2)

    #print(AvgRev2)


print("")

print(f"{title}")

print("-----------------------------------------------")

print(f"Total  Months: {NumMonths}")

print(f"Total: ${TTRevenue}")

print(f"Average Change: ${AvgRev2}")

print(f"Greatest Increase in Revenue: {Month_GIncrease}  (${GProfit_increase}) ")

print(f"Greatest Decrease in Revenue: {Month_GDecrease} (${GProfit_decrease})")

print("------------------------------------------------")

 

output = (


    f"\n\n"

    f"\n{title}\n"

    f"\n-----------------------------------------------\n"

    f"\nTotal Number of Months: {NumMonths} months\n"

    f"\nTotal Revenue: ${TTRevenue}\n"

    f"\nAverage Change: ${AvgRev2}\n"

    f"\nGreatest Increase in Revenue: {Month_GIncrease} ${GProfit_increase}\n"

    f"\nGreatest Decrease in Revenue: {Month_GDecrease} ${GProfit_decrease}\n"

    f"\n------------------------------------------------\n")

#print(output)

with open(analysis, "w") as txt_file:

    txt_file.write(output)

 

 

