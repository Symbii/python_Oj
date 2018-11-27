#!/usr/bin/env python

def Unique_Email_Add(email_list):
    unique_email = []
    for str in email_list:
        domain_index = str.index('@')
        email_name = ''
        host_name  = ''
        for i in range(len(str)):
            if str[i] == '+':
                email_name = host_name + (str[domain_index:])
                break
            elif str[i] == '.':
                continue
            elif str[i] == '@':
                email_name = host_name + str[domain_index:]
                break
            host_name += str[i]
        if 0 == unique_email.count(email_name):
            unique_email.append(email_name)
    return len(unique_email)

if __name__ == "__main__":
    email = ["aaa@163.com","aaa.@163.com","aaa+@163.com","aaa+aa@126.com"]
    print(Unique_Email_Add(email))