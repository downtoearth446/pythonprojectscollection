lst = ["Bhindi","Aloo","Tamatar","Maggi"]
# now to get index while iterating in for loop we use enumerate for eg
for index, item in enumerate(lst):
    if index%2 == 0:
        print(f"Serial No : {index}, dish : {item}")
