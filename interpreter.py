from PIL import Image
import pytesseract

def imageToInstructions(image):
    expression = pytesseract.image_to_string(image)

    expression = expression.lower()
    expression = expression.replace("x", "*")
    expression = expression.replace("÷", "/")
    expression = ''.join(i for i in expression if i.isdigit() or i == "*" or i == "/" or i == "+" or i == "-" or i == "(" or i == ")" \
        or i == "[" or i == "]" or i == "{" or i == "}")
    try:
        answer = eval(expression)
    except ZeroDivisionError:
        answer = 0
    except:
        return

    instructions = []
    with open("instructions/1.txt", "r") as structs1, open("instructions/2.txt", "r") as structs2, open("instructions/3.txt", "r") as structs3, \
        open("instructions/4.txt", "r") as structs4, open("instructions/5.txt", "r") as structs5, open("instructions/6.txt", "r") as structs6, \
        open("instructions/7.txt", "r") as structs7, open("instructions/8.txt", "r") as structs8, open("instructions/9.txt", "r") as structs9, \
        open("instructions/negative.txt", "r") as structsNeg, open("dot.txt", "r") as structsDot, open("0.txt", "r") as structs0:
        for char in expression:
            if char == "0":
                instructions.append(structs0.readlines)
                #excecuteInstructions(structs.readlines)
            elif char == "1":
                instructions.append(structs1.readlines)
                #excecuteInstructions(structs1.readlines)
            elif char == "2":
                instructions.append(structs2.readlines)
                #excecuteInstructions(structs2.readlines)
            elif char == "3":
                instructions.append(structs3.readlines)
                #excecuteInstructions(structs3.readlines)
            elif char == "4":
                instructions.append(structs4.readlines)
                #excecuteInstructions(structs4.readlines)
            elif char == "5":
                instructions.append(structs5.readlines)
                #excecuteInstructions(structs5.readlines)
            elif char == "6":
                instructions.append(structs6.readlines)
                #excecuteInstructions(structs6.readlines)
            elif char == "7":
                instructions.append(structs7.readlines)
                #excecuteInstructions(structs7.readlines)
            elif char == "8":
                instructions.append(structs8.readlines)
                #excecuteInstructions(structs8.readlines)
            elif char == "9":
                instructions.append(structs9.readlines)
                #excecuteInstructions(structs9.readlines)
            elif char == "-":
                instructions.append(structsNeg.readlines)
                #excecuteInstructions(structsNeg.readlines)
            elif char == ".":
                instructions.append(structsDot.readlines)
                #excecuteInstructions(structsDot.readlines)

def excecuteInstructions(instructions, motorX, motorY, motorZ):
    for struct in instructions:
        dir = struct[0] == "+"
        motor = struct[1]
        steps = float(struct[1:])

        if motor == "X":
            motorX.run(steps, dir)
        elif motor == "Y":
            motorY.run(steps, dir)
        elif motor == "Z":
            motorZ.run(steps, dir)