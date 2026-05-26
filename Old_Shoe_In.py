import sys
import Old_Shoe_Sale

# Read prices from command-line arguments
prices = [int(value) for value in sys.argv[1:]]

print('Enter the total number they can carry')
p = int(input('Enter the total number Shreya and mother can carry: '))

# Call the function
Old_Shoe_Sale.oldShoeSale(p, prices)