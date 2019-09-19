##############################################################################
###              SAVE MULTIPLE ITEMS(A DICTIONARY) TO FILE
##############################################################################
def saveMultipleItemsToFile(fileName,Items):
    with open(f"{fileName}.txt",'a') as file:
        for key, value in Items:
            file.write(f"{key},{value}\n")


##############################################################################
###                SAVE A SINGLE ITEM TO FILE
##############################################################################
def saveItemToFile(fileName, item):
    with open(f"{fileName}.txt",'a') as file:
        file.write(item + "\n")




