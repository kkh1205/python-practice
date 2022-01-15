############ 계산기 만들기 ###########

def calcul():
  print('\nyou can insert two number and cal. \n inputable cal : +, -, *, /, //, %\n')
  a = input('please input num : ')
  cal = str(input('please input cal : '))
  b = input('please input num : ')

  # validation check cal
  if(cal != '+' and cal != '-' and cal != '*' and cal != '/' and cal != '//' and cal != '%'):
    def wrong_cal():
      print('Please enter the correct cal : +, -, *, /, //, %')
      calcul()

    return wrong_cal()
  
  # validation check num
  def translate_num(in_num):
    try:
      n = float(in_num)
      return n
    except ValueError:
      print('wrong type. please input number')
      calcul()
  
  a = translate_num(a)
  b = translate_num(b)
  
  def integer_ck (num):
    if(num.is_integer() == True):
      return int(num)
    else:
      return num
  
  if (cal == '+'):
    def return_cal():
      result = a+b
      result = round(result,2)
      result = integer_ck(result)
      print(result)
      calcul()

    return return_cal() 
  
  elif (cal == '-'):
    def return_cal():
      result = a-b
      result = round(result,2)
      result = integer_ck(result)
      print(result)
      calcul()

    return return_cal()
  
  elif (cal == '*'):
    def return_cal():
      result = a*b
      result = round(result,2)
      result = integer_ck(result)
      print(result)
      calcul()

    return return_cal()

  elif (cal == '/'):
    def return_cal():
      result = a/b
      result = round(result,2)
      result = integer_ck(result)
      print(result)
      calcul()

    return return_cal()

  elif (cal == '//'):
    def return_cal():
      result = a//b
      result = round(result,2)
      result = integer_ck(result)
      print(result)
      calcul()

    return return_cal()

  elif (cal == '%'):
    def return_cal():
      result = a%b
      result = round(result,2)
      result = integer_ck(result)
      print(result)
      calcul()

    return return_cal()

calcul()