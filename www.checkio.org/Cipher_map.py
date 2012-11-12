# Help Sofia to make a decipher for the passwords that Nikola will encrypt in the map.

# A cipher grille is a 4 ¡Á 4 paper square in which four windows are cut out. Putting the grille on a paper sheet of the same size, the chairman writes down the first four symbols of his password in the windows (see fig. below). After that the chairman turns the grille clockwise by 90 degrees. The symbols written earlier become hidden under the grille and clean paper appears in the windows. He writes down the next four symbols of the password in the windows and again turns the grille by 90 degrees. Then he writes down the following four symbols and turns the grille once more. After that he writes down the last four symbols of the password. Now, without the same cipher grille, it is very difficult to restore the password from the resulting square with 16 symbols. Thus, the chairman is sure that no contestant will get access to the problems too early.



# Write a module for the robots to remember their passwords with the codes easily when they come back.

# Input The first four lines contain the Robot's cipher grille. The next four lines contain the square with the ciphered password. All the symbols in the square are lowercase Latin letters.

# Output: Password
def matrix_transpose(matrix_src):

    matrix_des = []
    myrow = ""
    for col in range(4):
        for row in range(3, -1, -1):
            myrow += matrix_src[row][col]
        matrix_des.append(myrow)
        myrow = ""

    return matrix_des

def checkio(input_data):
    'Return password of given cipher map'

    cipher_grille, ciphered_password = input_data

    mypassword = ""
    new_cipher_grille = cipher_grille
    
    for p in range(4):
        for i in range(4):
            for j in range(4):
                # print "&&&&&&&"
                # print "i=", i
                # print "j=", j
                if new_cipher_grille[i][j] == "X":
                    mypassword += ciphered_password[i][j]
                    
        new_cipher_grille = matrix_transpose(new_cipher_grille)

    return mypassword

if __name__ == '__main__':
    assert checkio([[
    'X...',
    '..X.',
    'X..X',
    '....'],[
    'itdf',
    'gdce',
    'aton',
    'qrdi']]) == 'icantforgetiddqd', 'First'

    assert checkio( [[
    '....',
    'X..X',
    '.X..',
    '...X'],[
    'xhwc',
    'rsqx',
    'xqzz',
    'fyzr']]) == 'rxqrwsfzxqxzhczy', 'Second'
    print('All ok')