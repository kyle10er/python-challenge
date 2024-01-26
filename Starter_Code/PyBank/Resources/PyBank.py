import csv
import os

#Calling csv file 
csvpath = os.path.join("/Users/kyle.tavtener/Desktop/UPENN-VIRT-DATA-PT-12-2023-U-LOLC/02-Homework/03-Python/Starter_code/PyBank/Resources/budget_data.csv")

#creating a function and initializing the variables to start
def BudgetAnalysis(csvpath):
    count = 0
    TotalProfit = 0 
    StartingProfit = 0
    TotalProfitChange = 0 
    ProfitChange = []
    Months = []
    

    with open(csvpath, "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',') #Choosing a comma as a new value
        next(csvreader)
    #Incrementing Total profit starting with tthe secod column of the data
        for row in csvreader:
            count = count + 1 
            Profit = int(row[1])
            TotalProfit += Profit
            #adding values to the lists every time there is a new month or change in profit
            if StartingProfit != 0:
                Change = Profit - StartingProfit
                ProfitChange.append(Change)
                Months.append(row[0])
                TotalProfitChange += Change

            StartingProfit = Profit

        AverageChange = TotalProfitChange / (count - 1)
        MaxProfitIncrease = max(ProfitChange)
        MaxMonthIncrease = Months[ProfitChange.index(MaxProfitIncrease)]
        MaxProfitDecrease = min(ProfitChange)
        MaxMonthDecrease = Months[ProfitChange.index(MaxProfitDecrease)]

    Summary = (
        f"\nFinancial Analysis\n"
        f"------------------------------------------------------\n"
        f"Total Months: {count}\n"
        f"Total: ${TotalProfit}\n"
        f"Average Change: ${AverageChange:2f}\n"
        f"Greatest Increase in Profits: {MaxMonthIncrease} (${MaxProfitIncrease})\n"
        f"Greatest Decrease in Profit: {MaxMonthDecrease} (${MaxProfitDecrease})\n"
    )
    print(Summary)
#Creating a summary table and then printing in the terminal and via an output file

    output_file = "/Users/kyle.tavtener/Desktop/result.txt"
    with open(output_file, "w") as results: 
        results.write(Summary)

BudgetAnalysis(csvpath)

            

       
