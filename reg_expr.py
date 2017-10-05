
import re 

pattern = re.compile('AV')
res1 = pattern.findall('AV analytics AVer')
res2 = pattern.findall('AV is smth')
#print(res1)
#print(res2)


mails = ['abc@gmail.com', 'sdfs@', '78*sd@co.co', '789@go?com','../sds@ro.com', 'mr.shrrgn@gmail.com']

def checking_mails(mails):
	return [mail for mail in mails if re.match(r'^[a-z0-9_\.]{3,20}@\w{2,6}\.\w{2,4}$', mail)]


passwords = ['adasfasfsd', 'JHASBsjfnsdfn324j', 'sdaW4', 'ksjdfnWW234', 'dsfd asf WerERT 132','799wEdvs']

def checking_passwords(passwords):
	return [i for i in passwords if not re.match(r'^([^0-9]*|[^A-Z]*|[^a-z]*)$', i) and len(i) >= 8]


#right = r'^(?=.*[0-9]+.*)(?=.*[A-Z]+.*)(?=.*[a-z]+.*)[0-9a-zA-Z]*$'

print(checking_mails(mails))
print(checking_passwords(passwords))