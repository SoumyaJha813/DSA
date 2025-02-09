class Solution:
    def reverseWords(self, s: str) -> str:
        rev = s[::-1]+' '
        print(rev)
        str1 = ''
        wrd1 = ''
        sent = ''
        for i in rev:
            if i == ' ':
                wrd1 = str1[::-1]
                print("this is a word: ",wrd1)
                if wrd1.strip() != '':
                    sent+=wrd1+' '
                str1 = ''
                wrd1 = ''
            elif i != ' ':
                str1 += i
        print("rev word sent: ",sent.strip())
        return sent.strip()
