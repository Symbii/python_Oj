def RobotToOrigin(str):
    if str.count('U') == str.count('D') and str.count('L') == str.count('R'):
        return True
    return False
