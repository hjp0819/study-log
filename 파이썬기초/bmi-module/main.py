from bmi_utils import calc_bmi, classify_bmi

def main():
    cm = float(input("키를 입력하세요(cm): "))
    kg = float(input("몸무게를 입력하세요(kg): "))

    bmi = calc_bmi(kg, cm)          
    result = classify_bmi(bmi)      

    print(f"BMI: {bmi}, 판정: {result}")

if __name__ == "__main__":
    main()
    

