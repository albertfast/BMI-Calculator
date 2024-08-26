'''
name = input("Enter your name : ")
weight = int(input("Enter your weight in pounds: "))
height = int(input("Enter your height in inches: "))
BMI = round((weight * 703) / (height * height))
#print("Your Body Mass Index = ", BMI)

if BMI>0:
    print(f"{name}, your Body Mass Index is {BMI} and ", end="")
    if(BMI<18.5):
        print(name +", you are underweight.")
    elif(BMI<=24.9):
        print(name +", you are normal weight.")
    elif(BMI<29.9):
        print(name +", you are overweight.")
    elif(BMI<34.9):
        print(name +", you are obese.")
    elif(BMI<=39.9):
        print(name +", you are severely obese.")
    else:
        print(name +", you are morbidly obese.")
else:
    print("Enter valid input!")
'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi_result = None
    if request.method == 'POST':
        name = request.form['name']
        weight = int(request.form['weight'])
        height = int(request.form['height'])
        BMI = round((weight * 703) / (height * height))
        if BMI < 18.5:
            bmi_result = f"{name}, your Body Mass Index is {BMI} and you are underweight."
        elif BMI <= 24.9:
            bmi_result = f"{name}, your Body Mass Index is {BMI} and you are normal weight."
        elif BMI < 29.9:
            bmi_result = f"{name}, your Body Mass Index is {BMI} and you are overweight."
        elif BMI < 34.9:
            bmi_result = f"{name}, your Body Mass Index is {BMI} and you are obese."
        elif BMI <= 39.9:
            bmi_result = f"{name}, your Body Mass Index is {BMI} and you are severely obese."
        else:
            bmi_result = f"{name}, your Body Mass Index is {BMI} and you are morbidly obese."

    return render_template('index.html', bmi_result=bmi_result)

if __name__ == '__main__':
    app.run(debug=True)

