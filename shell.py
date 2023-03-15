import betpy

while True:
    text = input('betpy > ')
    result, error = betpy.run('<shell>', text)
    
    if error:
        print(error.as_string())
    else:
        print(result)