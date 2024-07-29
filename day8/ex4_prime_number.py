# Write your code below this line 👇
def prime_msg(p_flag):
  if p_flag == "Y":
    print("It's a prime number.")
  else:
    print("It's not a prime number.")


def prime_checker(number):
  if number > 100:
    print ("Number out of our test range")
    return
  elif number == 1:
    prime_msg("N")
    return
  elif number == 2 or number == 3 or number == 5 or number == 7:
    prime_msg("Y")
    return
  else:
    for i in (2,3,5,7):
      if number%i == 0:
        prime_msg("N")
        return

  prime_msg("Y")




# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)