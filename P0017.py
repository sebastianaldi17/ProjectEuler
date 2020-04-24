# Number letter counts
# https://projecteuler.net/problem=17
# Feelings of deja vu envelop me

num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: ''}
ans = 0
for i in range(1, 1001):
    if i == 1000: ans += len("onethousand")
    s = str(i)
    if len(s) == 1: ans += len(num2words[i])
    elif len(s) == 2:
        if s[0] == '1' or s[1] == '0': ans += len(num2words[i])
        else: ans += len(num2words[int(s[0])*10]) + len(num2words[int(s[1])])
    elif len(s) == 3:
        ans += len(num2words[int(s[0])]) + len("hundred") 
        if i%100: ans += len("and")
        if s[1] == '1' or s[2] == '0': ans += len(num2words[int(s[1:])])
        else: ans += len(num2words[int(s[1])*10]) + len(num2words[int(s[2])])
print(ans)