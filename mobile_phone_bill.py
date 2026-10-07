#Jeffrey Almendarez
#CMP131
#LAB6
#WEEK6
package_price=99.00 #our price
units_sold=int(input("Enter the number of units sold: "))
if units_sold<=0:
    print("Error: The numbers of unit sold must be greater than 0")
else:
     if units_sold >= 100:
        discount_rate=0.50
     elif units_sold >= 50:
        discount_rate=0.40
     elif units_sold >= 20:
         discount_rate=0.30
     elif units_sold>=10:
         discount_rate=0.20
     else:
         discount_rate=0.00
         
original_total=units_sold*package_price
discount_amount= original_total*discount_rate
total_cost=original_total-discount_amount
        
print(f"---Price Breakdown---")
print(f"Original total cost: ${original_total:,.2f}")
print(f"\nDiscount percentage: {discount_rate * 100:.0f}%")
print(f"Discount amount: ${discount_amount: .2f}")
print("---Final Price---")
print(f"Total cost of the purchase: ${total_cost:,.2f}")



