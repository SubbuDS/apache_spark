f = open('census_2010.json')

for i in range(0,4):
    print(f.readline())
    
    
    
#census data :
#"{\"females\": 1994141, \"total\": 4079669, \"males\": 2085528, \"age\": 0, \"year\": 2010}\n{\"females\": 1997991, \"total\": 4085341, \"males\": 2087350, \"age\": 1, \"year\": 2010}\n{\"females\": 2000746, \"total\": 4089295, \"males\": 2088549, \"age\": 2, \"year\": 2010}\n{\"females\": 2002756, \"total\": 4092221, \"males\": 2089465, \"age\": 3, \"year\": 2010}\n{\"females\": 2004366, \"total\": 4094802, \"males\": 2090436, \"age\": 4, \"year\": 2010}"

f = open('census_2010.json')

for i in range(0,4):
    print(f.readline())
    
    
    
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.printSchema()


first_five = df.head(5)
for r in first_five:
    print(r.age)
    
    
    
df[['age']].show()
df[['age', 'males', 'females']].show()


five_plus = df[df['age'] > 5]
five_plus.show()


df[df['females'] < df['males']].show()


pandas_df = df.toPandas()
pandas_df['total'].hist()



