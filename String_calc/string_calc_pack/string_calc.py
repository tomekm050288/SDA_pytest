import re


class StringCalculator:

    def add(self, numbers):
        if numbers == "":
            return 0
        else:
            if numbers.startswith("//"):
                delimiter = re.search(r"//(.*?)-?[\n|\d|,]", numbers).group(1)
                pattern = re.compile(r"\n|,|{}".format(delimiter))
                result = re.split(pattern, numbers[2+len(delimiter):])
                if result[0] == '':
                    result = result[1:]
                sum = 0
                for number in result:
                    try:
                        int(number)
                        if int(number) > 1000:
                            continue
                        elif int(number) < 0:
                            return f'negatives not allowed: {", ".join([x for x in result if int(x) < 0])}'
                            break
                        sum += int(number)
                    except ValueError:
                        return "Wrong input"
                        break
                return sum
            else:
                pattern = re.compile(r"\n|,")
                result = re.split(pattern, numbers)
                if result[0] == '':
                    result = result[1:]
                sum = 0
                for number in result:
                    try:
                        int(number)
                        if int(number) > 1000:
                            continue
                        elif int(number) < 0:
                            return f'negatives not allowed: {", ".join([x for x in result if int(x) < 0])}'
                            break
                        sum += int(number)
                    except ValueError:
                        return "Wrong input"
                        break
                return sum


# calc = StringCalculator()
#
# print(calc.add("//abc\n5,3\n0abc5,5,0,1"))

