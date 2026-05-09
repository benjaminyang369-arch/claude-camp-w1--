# Enter meal fee amount
meal_fee = float(input("meal_fee: "))

# enter tip rate
tip_rate = float(input("tip_rate_%: "))

# to divided by 100 for tip amount
tip_amount = meal_fee * tip_rate / 100

total_amount = meal_fee + tip_amount

print(f"your total meal amout is {total_amount:.2f}")
print(f"your tip is {tip_amount:.2f}")