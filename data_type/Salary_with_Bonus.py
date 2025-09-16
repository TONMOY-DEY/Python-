name=input()
fixd_salary=float(input())
sales_total_made=float(input())


commission=sales_total_made*0.15

final_salary=commission+fixd_salary

print(f"TOTAL = R$ {final_salary:.2f}")

