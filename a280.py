import csv

fraction_to_mL = []
mL_to_A280 = []

with open("fractiontomL.csv", encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        fraction_to_mL.append(row)
        
with open("mLtoA280.csv", encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        mL_to_A280.append(row)

wtr = csv.writer(open ('out.csv', 'w'), delimiter=',', lineterminator='\n')
heading = ['Fraction','mL','mAU']
wtr.writerow(heading)

number_fractions = int(fraction_to_mL[-1][0])
first_fraction = fraction_to_mL[0][0]

i = 0
j = 0



while i < number_fractions - 2:
    low = fraction_to_mL[i][1]
    high = fraction_to_mL[i + 1][1]
    
    while mL_to_A280[j][0] < low:
        j = j + 1
    
    temp_list = [first_fraction]
    temp_list.extend(mL_to_A280[j])
    wtr.writerow(temp_list)

    i += 1
    first_fraction += 1