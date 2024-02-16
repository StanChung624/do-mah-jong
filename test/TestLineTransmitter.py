def TestDitchCardMode(line_transmitter):
    test = "筒12345678條22北1"
    result = line_transmitter(test)
    result = result.replace(" ", "")
    result = result.replace("\n", "")
    return result == "丟<北>等：3筒有3張6筒有3張9筒有4張"
    
def TestListenCardMode(line_transmitter):
    test = "筒12345678條22北"
    result = line_transmitter(test)
    result = result.replace(" ", "")
    result = result.replace("\n", "")
    return result == "等：3筒,6筒,9筒,"