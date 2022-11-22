import re
from database import insertdata


def cal(user_message):
    msg = user_message.split(" ")

    def ad(user_message):
        matches = [int(s) for s in re.findall(r'\d+', user_message)]
        nums= sum(matches)
        print("DOBBY:The answer is", nums)
        insertdata.insert_detail("DOBBY:", nums)
        return nums




    def sb(user_message):
        matches = [int(s) for s in re.findall(r'\d+', user_message)]
        nums = matches[0]
        for val in range(1, len(matches)):
            nums = nums - matches[val]
        print("DOBBY:The answer is", nums)
        insertdata.insert_detail("DOBBY:", nums)
        return nums

    def mul(user_message):
        matches = [int(s) for s in re.findall(r'\d+', user_message)]
        nums = matches[0]
        for val in range(1, len(matches)):
            nums = nums * matches[val]
        print("DOBBY:The answer is", nums)
        insertdata.insert_detail("DOBBY:", nums)
        return nums

    def div(user_message):
        matches = [int(s) for s in re.findall(r'\d+', user_message)]
        try:
            nums = matches[0] / matches[1]
            print("DOBBY:The answer is", nums)
            insertdata.insert_detail("DOBBY:", nums)
            return nums
        except:
            print("Can not divide by zero")
    for val in msg:
        if val == "addition" or val == "+" or val == "add" or val == "sum":
            return ad(user_message)
        elif val == "subtraction" or val == "-" or val == "sub" or val == "subtract":
            return sb(user_message)
        elif val == "multiplication" or val == "*" or val == "multiply":
            return mul(user_message)
        elif val == "divide" or val == "division" or val == "/":
            return div(user_message)
