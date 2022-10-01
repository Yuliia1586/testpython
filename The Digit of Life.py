def split(word):
    return [char for char in word]

date = input("Enter your date of birth in YYYYMMDD format: > ")
sum_list = []


def digitOfLife(date):
    sum = 0
    if(len(date) > 8):
        print("Input data too long")
        return
    else:
        date_list = []
        for char in date:
            date_list.append(int(char))
            
        while len(date_list) >= 1:
            print(len(date_list))
            for num in date_list:
                if sum > 9:
                    sum = 0
                sum+=num
                date_list.pop()
    return sum
    
print(digitOfLife(date))
