import random
import array


def randompwd_gen():
    length = 12
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                 'v', 'w', 'x', 'y', 'z']

    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U',
                 'V', 'W', 'X', 'Y', 'Z']

    specialcharacters = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

    combination = number + lowercase + uppercase + specialcharacters

    rand_num = random.choice(number)
    rand_upper = random.choice(uppercase)
    rand_lower = random.choice(lowercase)
    rand_spl = random.choice(specialcharacters)

    password = rand_num + rand_upper + rand_lower + rand_spl
    for x in range(length - 4):
        password = password + random.choice(combination)
        passwordlist = array.array('u', password)
        random.shuffle(passwordlist)
    password = ""
    for x in passwordlist:
        password = password + x
    return (password)