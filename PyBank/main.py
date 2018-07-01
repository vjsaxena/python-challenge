#Necessary Import
import csv

#Define files to be used in the program
budget_csv = "Resources/budget_data.csv"
result_file = "Analysis/budget_analysis.txt"

#Define variables

total_net_amount=0
avg_change=0
month_list=[]
monthly_change_list=[]
total_months=0
prev_amount=0
net_change=0
amt=0
result_string=""

#Open File
with open(budget_csv, newline='') as budget_file:
    budget_reader = csv.reader(budget_file, delimiter=",")
    
    #skip header
    header=next(budget_reader)
    
    #Process rest of the file
    for budget_line in budget_reader:
        total_months=total_months+1                                 #count months
        total_net_amount =total_net_amount+int(budget_line[1])      #Calculate Total Net Amount
                       
        month_list.append(budget_line[0])                           #Append to List of Months
        
        #change for first month is 0
        if (total_months==1):
            amt=0
        else:
            amt=int(budget_line[1]) - prev_amount
        
        monthly_change_list.append(amt)
        prev_amount=int(budget_line[1])
        net_change=net_change+amt
        
    #Calculate Average, Greatest Increase, Greatest Decrease and respective months    
    avg_change =net_change / (total_months- 1)
    max_inc_amt=max(monthly_change_list)
    max_dec_amt=min(monthly_change_list)
    max_inc_month=month_list[monthly_change_list.index(max_inc_amt)]
    max_dec_month=month_list[monthly_change_list.index(max_dec_amt)]
   
    #Store/Print result in a string
    result_string=(f"\nFinancial Analysis\n----------------------------\n"
                   f"Total Months: {total_months}\n"
                   f"Total: ${total_net_amount}\n"
                   f"Average Change: ${avg_change:.2f}\n"
                   f"Greatest Increase in Profits: {max_inc_month} (${max_inc_amt})\n"
                   f"Greatest Decrease in Profits: {max_dec_month} (${max_dec_amt})\n"
    )
    print(result_string)
       
#Write result to disk        
with open(result_file, "w") as out_file:
    out_file.write(result_string)    

