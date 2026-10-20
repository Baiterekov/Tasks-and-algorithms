class Solution:
    def convertDateToBinary(date):
        
        def decimal_to_binary(decimal):
            str_binary = ""
            while True:
                str_binary = str(decimal%2) + str_binary
                if(decimal==1 or decimal==0):
                    return str_binary
                decimal //=2 

        date_arr = date.split("-")
        binary_date = ""
        binary_date = decimal_to_binary(int(date_arr[0]))+"-"+decimal_to_binary(int(date_arr[1]))+"-"+decimal_to_binary(int(date_arr[2]))
        return binary_date


print(Solution.convertDateToBinary("1900-01-01"))
