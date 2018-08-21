p=raw_input('')
o=['a','e','i','o','u','A','E','I','O','U']
if(p>='a' and p<='z' or p>='A' and p<='Z'):
    if(p in o):
          print('vowel')
    else:
          print('consonant')
else:
    print('invalid')
