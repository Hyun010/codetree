class T:
    def __init__(self,name="codetree",code=50):
        self.name=name
        self.code=code

product_name, product_code = input().split()
product_code = int(product_code)

t1=T()
t2=T(product_name,product_code)
print(f'product {t1.code} is {t1.name}')
print(f'product {t2.code} is {t2.name}')