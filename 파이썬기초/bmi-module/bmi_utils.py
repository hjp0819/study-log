def calc_bmi(kg : float,cm:float):
    m = cm / 100 # cm->m변환
    bmi =  kg / (m*m)
    return round(bmi,1)


def classify_bmi(bmi:float):
    result = ""
    if bmi < 18.5 :
        result = "저체중"
    elif bmi < 23 :
        result= "정상"
    elif bmi < 25 :
        result="과체중"
    else :
        result="비만"
    
    return f"{result}입니다."
