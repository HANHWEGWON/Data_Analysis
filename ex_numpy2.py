import pandas as pd

index = ['2018', '2019', '2020', '2021']

yeonghee = pd.Series([143, 150, 157, 160], index = index)
Cheolsu = pd.Series([165, 172, 175, 180], index = index)

growth = pd.DataFrame({
    '영희' : yeonghee,
    '철수' : Cheolsu
})

print("?")