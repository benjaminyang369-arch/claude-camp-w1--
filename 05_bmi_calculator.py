height = float(input("your_height_m:"))
weight = float(input("your_weight_kg:"))

bmi = weight / (height ** 2)
if bmi < 18.5:
    advice = "偏瘦"
elif bmi < 25:
    advice = "正常"
elif bmi < 30:
    advice = "偏胖"
else:
    advice = "肥胖"

print(f"your_bmi_is {bmi:.2f}, your are {advice}")