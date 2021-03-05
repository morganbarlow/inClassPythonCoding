def pretty_price (sales,flex):
  #if isinstance finds a flex number that is an interger then -->
  if isinstance(flex,int): 
    #you change flex from an interget to a FloatingPoint
    flex = flex *0.01
  #you then return sales as a an even interger 
  #and add the flex number to then end
  return int(sales) + flex

#when printed with pretty price you will get a $.$$ number
print(pretty_price(4.76, .44))
print(pretty_price(6.32,66))
print(pretty_price(5,0.55))

