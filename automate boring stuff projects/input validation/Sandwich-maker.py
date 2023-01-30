import pyinputplus as pyip

bread = {'wheat':20,'white':22,'sourdough':25}
protein = {'chicken':50,'turkey':70,'ham':23,'tofu':30}
cheese = {'cheddar':65,'Swiss':89,'mozzarella':80}
vegetables = {'mayo':4,'mustard':5,'lettuce':7,'tomato':8}

Total_price = 0

while True:
    print('Hi\nWelcome to Bright\'s kitchen\nWe serve bread,protein and cheese')
    bread_request = pyip.inputYesNo('Do you want some bread?')
    if bread_request == 'yes':
        bread_type = pyip.inputMenu(['wheat','white','sourdough'],numbered=True)
        print(bread_type)
        Total_price += bread[bread_type]


    protein_request = pyip.inputYesNo('Would you Order Some Protein?')
    if protein_request == 'yes':
        protein_type = pyip.inputMenu(['chicken','turkey','ham','tofu'],numbered=True)
        print(protein_type)
        Total_price += protein[protein_type]

    cheese_request = pyip.inputYesNo('Do you like cheese?')
    if cheese_request == 'yes':
        cheese_type = pyip.inputMenu(['cheddar','Swiss','mozzarella'],numbered=True)
        print(cheese_type)
        Total_price += cheese[cheese_type]

    veges_request = pyip.inputYesNo('Do you like vegetables?')
    if veges_request == 'yes':
        veges_type = pyip.inputMenu(['mayo','mustard','lettuce','tomato'],numbered=True)
        print(veges_type)
        Total_price += vegetables[veges_type]
    finished = pyip.inputYesNo('Is that all you want?')
    if finished == 'no':
        continue
    break


quantity_request = pyip.inputNum('How many quantity do you want?',min=1)
print(quantity_request)
print(f'Total Price: {quantity_request * Total_price}')
