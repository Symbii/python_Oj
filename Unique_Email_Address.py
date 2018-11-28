#!/usr/bin/env python

def Unique_Email_Add(email_list):
    unique_email = set()
    for str in email_list:
        host, _, domain = str.partition('@')
        if '+' in host:
            host = host[:host.index('+')]
        unique_email.add(host.replace(".","") + '@' + domain)
    return (unique_email)

if __name__ == "__main__":
    email = ["aaa@163.com","aaa.@163.com","aaa+@163.com","aaa+aa@126.com"]
    print(Unique_Email_Add(email))