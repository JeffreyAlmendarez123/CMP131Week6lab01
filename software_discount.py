#Jeffrey Almendarez
#CMP131
#Week6
#lab01

package=(input("Pick a Package between (A, B, or C):")).upper()
if package != "A" and package != "B" and package != "C":
    print("Error: Invalid package! You must choose A, B, or C.")
else:
    minutes = int(input("Enter minutes used: "))
    if package == "A":
        base_price = 39.99
        if minutes > 450:
            extra_charge = (minutes - 450) * 0.45
        else:
            extra_charge = 0.00

    elif package == "B":
        base_price = 59.99
        if minutes > 900:
            extra_charge = (minutes - 900) * 0.40
        else:
            extra_charge = 0.00

    elif package == "C":
        base_price = 69.99
        extra_charge = 0.00

    
    total_due = base_price + extra_charge


print(f"\nPackage Selected: {package}")
print(f"Minutes Used: {minutes:.0f}")
print(f"Base Cost: ${base_price:.2f}")
print(f"Additional Charge: ${extra_charge:.2f}")
print(f"Total Amount Due: ${total_due:.2f}")