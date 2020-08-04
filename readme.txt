Export UNICORN 7 data as a .csv.

Create 2 new csv files in the same directory as a280.py as follows:
    1) fractiontomL.csv
        In column A, copy the numerical fractions from column K of the exported .csv
        In column B, copy the mLs corresponding to each fraction from column I of the exported .csv
    2) mLtoA280.csv
        In column A, copy all of the mLs from column A of the exported .csv
        In column B, copy the mAU corresponding to each mL from column B of the exported .csv

Open Command Prompt
    1) cd C:\... <-- enter the directory/folder where a280.py and the 2 .csv files are located
    2) python a280.py

You should see a new file called out.csv.
