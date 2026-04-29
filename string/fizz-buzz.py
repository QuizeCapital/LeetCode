class Solution(object):
    def fizzBuzz(self, n):

        fizz_dict = {
            3: 'Fizz',
            5: 'Buzz'
        }
        res_list = []

        for i in range(1, n + 1):
            result = ""
            for key in fizz_dict.keys():
                if i % key == 0:
                    result += fizz_dict[key]

            if result == "":
                result = str(i)

            res_list.append(result)

        return res_list
