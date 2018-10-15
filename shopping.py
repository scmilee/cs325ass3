#standard file reader from all of my previous assignments
#used https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/ as a resource and our group discussion!
unsortedMatrix = [];
with open('./shopping.txt') as f:
    for line in f:
        numbers_float = map(int, line.split());
        unsortedMatrix.append(numbers_float);

#shopping takes in the current family members capactiy, the array of weights and prices, and the N number of items
def shopping(capacity, weight, price, n): 
    #0 out a matrix of values that will fit the dimentions of weight and items
    K = [[0 for x in range(capacity+1)] for x in range(n+1)] 
    #start the loop through the item list
    for i in range(n+1): 
        #start the loop through the capacity values
        for w in range(capacity+1):
            #mulligan 0 values 
            if i==0 or w==0: 
                K[i][w] = 0
            elif weight[i-1] <= w:
                #get either the last value or the last items price plus the last index that will allow a carry increase(dependent on current weight value)
                # #and set it as the current value  
                K[i][w] = max(price[i-1] + K[i-1][w-weight[i-1]],  K[i-1][w])   
            else: 
                K[i][w] = K[i-1][w]
     # stores the result of Knapsack 
    res = K[n][capacity] 
    choices = []
    choices.append(res)
    w = capacity 
    #a loop to loop backwards through the process of adding items to the cart
    for i in range(n, 0, -1): 
        if res <= 0: 
            break
        #has to be i-1 or else you get extra data points in the choices value
        if res == K[i - 1][w]: 
            continue
        else: 
            #add the item index to the result array, adjusting the price and current carrying capacity
            #to reflect the freshly "moved" item.
            choices.append(i)
            res = res - price[i - 1] 
            w = w - weight[i - 1]
        #return the array of choices and the finishign value
    return choices
        
#a function that iterates over the family members and calls shopping with each members capacity
def solve(itemPrices,itemWeights,capacities,numberOfItems):
    total_price = 0;
    familyLenght = len(capacities)
    result = []
    for i in range(0,familyLenght):
        result.append(shopping(capacities[i],itemWeights,itemPrices, numberOfItems[0]));
        #the result is an array of values, the first being the members maximum,
        #with the following numbers being the choices of items they made
    return result
#get the amount of test cases from the input
testCase = unsortedMatrix[0]
testCases = []
del unsortedMatrix[0]
for testcases in range(0, testCase[0]):#loop through for the amount of testcases given
    capac = []
    prodPrice = []
    prodWight = []
    #every time the unsorted matrix is touched the value is then deleted from the array
    #this is done to prevent having to keep track of the index for various sizes of n
    numberOfitems = unsortedMatrix[0]
    del unsortedMatrix[0]
    #for each item add it respective price and weight values
    for items in range(0, numberOfitems[0]):
        prodPrice.append(unsortedMatrix[0][0])
        prodWight.append(unsortedMatrix[0][1])
        del unsortedMatrix[0]
    #the number of family members
    familyCount = unsortedMatrix[0]
    del unsortedMatrix[0]
    for family in range(0, familyCount[0]):
        capac.append(unsortedMatrix[0][0])
        del unsortedMatrix[0]
    # the matrix of results per family added to their respective test case
    testCases.append(solve( prodPrice, prodWight,capac, numberOfitems))

# this area deals with looping over the matrix of data points that we've created thus far
#and writes it to the shopping.out file
f1=open('./shopping.out', 'w+');
#initializes test cases first
for arrayIndex in range(0,len(testCases)):
    testCase = testCases[arrayIndex];
    totalPrice = 0;
    stringCase = "Test Case " + str(arrayIndex + 1) + "\n";
    memberStrings= "";
    #starts to loop through test case data 
    for index in range(0,len(testCase)):
        totalPrice += testCase[index][0]
        del testCase[index][0]
        results = testCase[index]
        #loops through each family members data
        for ind in range(0, len(results)) :
            tempString = "    "
            tempString += str(index + 1) + ": "
            for itemIndex in reversed(range(0, len(results))):
                tempString += str(results[itemIndex]) + " "
        tempString += "\n"
        memberStrings += tempString
    #add all of the built out strings to the file
    f1.write(stringCase);
    f1.write("Total Price " + str(totalPrice) + "\n")
    f1.write("Member Items\n")
    f1.write(memberStrings)
    f1.write('\n');
f1.close()