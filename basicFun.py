# -*- coding: utf-8 -*-
"""
@author: Thompson Hu

This script aims to dealing with the format of input data to post data easily
"""
import re

def passwordFormat(password):
    passOut = password.title()
    
    return passOut

def emailFormat(email):
    text = re.findall(r'(.*?)at(.*?).com', email)[0]
    emailOut = text[0] + '@' + text[1] + '.com'
    
    return emailOut

def birthdayFormat(birthday):
    birthday = birthday[5:7] + "-" + birthday[-2:] + "-" + birthday[0:4]
    
    return birthday

def incomeJudge(income):
    if income < 50000:
        incomeOut = '$0-$50,000'
    elif income < 75000:
        incomeOut = '$50,001-$75,000'
    elif income < 100000:
        incomeOut = '$75,001-$100,000'
    elif income < 150000:
        incomeOut = '$100,001-$150,000'
    elif income < 250000:
        incomeOut = '$150,001-$250,000'
    else:
        incomeOut = '$250,001 +'
                    
    return incomeOut

def netJudge(networth):
    if networth < 25000:
        networthOut = '$0-$25,000'
    elif networth < 50000:
        networthOut = '$25,001-$50,000'
    elif networth < 100000:
        networthOut = '$50,001-$100,000'
    elif networth < 200000:
        networthOut = '$100,001-$200,000'
    elif networth < 350000:
        networthOut = '$200,001-$350,000'
    elif networth < 700000:
        networthOut = '$350,001-$700,000'
    elif networth < 1000000:
        networthOut = '$700,001-$1,000,000'
    else:
        networthOut = '$1,000,000 +'
                    
    return networthOut

def employFormat(employment):
    if employment.find('unemployed') != -1:
        employOut = 'Unemployed'
    elif employment.find('self-employed') != -1:
        employOut = 'Self-Employed'
    elif employment.find('retired') != -1:
        employOut = 'Retired'
    elif employment.find('employed') != -1:
        employOut = 'Employed'
    
    return employOut

def martialFormat(martial):
    if martial.find('single') != -1:
        martialOut = 'Single'
    elif martial.find('married') != -1:
        martialOut = 'Married'
    elif martial.find('divorced') != -1:
        martialOut = 'Divorced'
    elif martial.find('separated') != -1:
        martialOut = 'Separated'
    
    return martialOut

def phoneFormat(phone):
    text = re.findall(r'(\d+) (\d+) (\d+)', phone)[0]
    phoneOut = '(' + text[0] + ')' + ' ' + text[1] + '-' + text[2]
    
    return phoneOut

def Q1Format(Q1):
    if Q1.find('sell all') != -1:
        q1Out = '23'
    elif Q1.find('sell part') != -1 or Q1.find('sell some') != -1:
        q1Out = '24'
    elif Q1.find('buy') != -1 or Q1.find('invest') != -1:
        q1Out = '25'
    elif Q1.find('keep') != -1:
        q1Out = '26'
    
    return q1Out

def Q2Format(Q2):
    if Q2.find('5') != -1 or Q2.find('five') != -1:
        q2Out = '29'
    if Q2.find('10') != -1 or Q2.find('ten') != -1:
        q2Out = '28'
    if Q2.find('15') != -1 or Q2.find('fifteen') != -1:
        q2Out = '27'
    
    return q2Out
    
def Q3Format(Q3):
    if Q3.find('lower') != -1:
        q3Out = '30'
    elif Q3.find('higher') != -1:
        q3Out = '31'
    
    return q3Out

def Q4Format(Q4):
    if Q4.find('yes') != -1:
        q4Out = '32'
    elif Q4.find('no') != -1:
        q4Out = '33'
    
    return q4Out

def C1Format(C1):
    if C1.find('new') != -1:
        c1Out = 'deposit_money'
    elif C1.find('transfer') != -1:
        c1Out = 'financial_institution'
    elif C1.find('401') != -1:
        c1Out = 'old_employer_retirement'
    
    return c1Out

def C2Format(C2):
    if C2.find('personal') != -1:
        c2Out = '12'
    elif C2.find('joint') != -1:
        c2Out = '14'
    elif C2.find('roth') != -1:
        c2Out = '18'
    elif C2.find('traditional') != -1:
        c2Out = '25'
        
    return c2Out

def C3Format(C3):
    if C3.find('contribution') != -1:
        c3Out = 'contributions'
    elif C3.find('withdraw') != -1:
        c3Out = 'distribution'  
    elif C3.find('neither') != -1:
        c3Out = 'neither' 

    return c3Out

def portFormat(port):
    textOut = ''.join(port)
    
    return textOut