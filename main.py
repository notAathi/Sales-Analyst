import numpy as np
from operationfile import operation

def getTotal(ind, dataframe):
    totalSal= np.sum(dataframe[ind])
    return int(totalSal)

def maxSum(dataframe):
    i=0
    best_company=i+1
    num_prod=0

    for i in range(len(dataframe)):
        result=getTotal(i, dataframe)
        if result>num_prod:
            num_prod=result
            best_company=i+1
    print(f"The best company is {best_company} and their max production is {num_prod}.")
    # return best_company
    
# def minSum(dataframe):
#     i=0
#     min_prod=1000000000
#     worst_company=i+1
#     num_prod=0

#     for i in range(len(dataframe)):
#         result=getTotal(i, dataframe)
#         if result<min_prod:
#             num_prod=result
#             worst_company=i+1
#     print(f"The worst company is {worst_company} and their min production is {num_prod}.")

def minSum(dataframe):
    worst_company = 0
    min_prod = float('inf')

    for i in range(len(dataframe)):
        result = getTotal(i, dataframe)
        if result < min_prod:
            min_prod = result
            worst_company = i + 1
    print(f"The worst company is {worst_company} and their min production is {min_prod}.")
# def minSum():
#     pass



def filehandling():
    lines = []
    with open("comp.txt", "r") as file:
        for line in file:
            values = line.strip().split(',')
            int_values = [int(val) for val in values ]
            lines.append(int_values)
    
        dataframe = np.array([np.array(row) for row in lines], dtype='object')
        return dataframe

def main():
    dataframe = filehandling()
    print(dataframe)

    first_batch = operation(dataframe[0])
    first_batch.display()
    first_batch.salary()
    first_batch.plot()
    maxSum(dataframe)
    minSum(dataframe)
main()


