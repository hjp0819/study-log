def calc_bmi(kg : float,cm:float):
    m = cm / 100 # cm->m변환
    bmi =  kg / (m*m)
    return round(bmi,1)
