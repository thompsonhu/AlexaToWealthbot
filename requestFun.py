# -*- coding: utf-8 -*-
"""
@author: Thompson Hu & Wesley Wang
"""
from __future__ import print_function
import requests
import re

sess = requests.Session()

"""
    Functions
"""
# Get token before input data
def get_token(html):
    token = re.findall(r'\[_token\]"\ value=\"(.*?)\"', html, re.S)[0]
    return token

def input_value(value):
    if value == "logout":
        url = 'http://ec2-54-173-235-225.compute-1.amazonaws.com'
        url_logout = build_url(url, "/logout")
        response = sess.get(url_logout)
        return response
    else:
        return value

def build_url(url, endpoint):
    return ''.join([url, endpoint])     
        
"""
    Register Function
"""
def register(session_attributes, headers):
    # Get Register page
    url_register = session_attributes['url_step']
    response = sess.get(url_register, headers = headers)
    
    token = get_token(response.text)
    
    # Input value
    first_name = input_value(session_attributes['first name'])
    last_name = input_value(session_attributes['last name'])
    nick_name = input_value(session_attributes['nick name'])
    email = input_value(session_attributes['email'])
    password_first = input_value(session_attributes['password'])
    password_second = input_value(session_attributes['password'])
    
    payload = ({'fos_user_registration_form[profile][first_name]': first_name,
            'fos_user_registration_form[profile][last_name]': last_name,
            'fos_user_registration_form[profile][nick_name]': nick_name,
            'fos_user_registration_form[email]': email,
            'fos_user_registration_form[plainPassword][first]': password_first,
            'fos_user_registration_form[plainPassword][second]': password_second,
            'fos_user_registration_form[is_accepted]': '1',
            'fos_user_registration_form[_token]': token})

    response = sess.post(url_register, data=payload, headers=headers)
    
    Name = [first_name, last_name, nick_name]

    return [response.url, Name]
    
"""
    Login Function
"""
def login(session_attributes, headers):
    # Get dynamic csrf token
    url_login = session_attributes['url_step']
    url = session_attributes['url']
    
    response = sess.get(url_login)
    csrf_token = re.findall(r'name="_csrf_token" value="(.*?)" />', response.text, re.S)[0]

    url_logincheck = build_url(url, "/login_check")
    
    # Input value
    user_name = input_value(session_attributes['email'])
    password = input_value(session_attributes['password'])

    payload = ({'_submit': 'Login',
                '_username': user_name,
                '_remember_me': '',
                '_csrf_token': csrf_token,
                '_password': password})
    
    response = sess.post(url_logincheck, data=payload, headers=headers)
    
    Name = re.findall(r'class=\"input-medium\ \ form-control"\ value=\"(.*?)\"', response.text, re.S)

    return [response.url, Name, response.text]
    
"""
    Step 1 Process
"""
def step_one(session_attributes, headers):
    url_step1 = session_attributes['url_step']
    response = sess.get(url_step1)
    token_step1 = get_token(response.text)
    
    # input value
    first_name = input_value(session_attributes['first name'])
    last_name = input_value(session_attributes['last name'])
    nick_name = input_value(session_attributes['nick name'])
    annual_income = input_value(session_attributes['annual income'])
    birth_date = input_value(session_attributes['birthday'])
    city = input_value(session_attributes['city'])  
    street = input_value(session_attributes['address'])
    employment_type = input_value(session_attributes['employment type'])
    estimated_income_tax = input_value(session_attributes['tax'])
    liquid_net_worth = input_value(session_attributes['net worth'])
    marital_status = input_value(session_attributes['martial status'])
    phone_number = input_value(session_attributes['phone number'])

    payload_step1 = ({'Continue': 'Continue',
                      'wealthbot_client_bundle_profile_type[_token]': token_step1,
                      'wealthbot_client_bundle_profile_type[annual_income]': annual_income,
                      'wealthbot_client_bundle_profile_type[birth_date]': birth_date,
                      'wealthbot_client_bundle_profile_type[city]': city,
                      'wealthbot_client_bundle_profile_type[employment_type]': employment_type,
                      'wealthbot_client_bundle_profile_type[estimated_income_tax]': estimated_income_tax,
                      'wealthbot_client_bundle_profile_type[first_name]': first_name,
                      'wealthbot_client_bundle_profile_type[last_name]': last_name,
                      'wealthbot_client_bundle_profile_type[liquid_net_worth]': liquid_net_worth,
                      'wealthbot_client_bundle_profile_type[mailing_city]': '',
                      'wealthbot_client_bundle_profile_type[mailing_street]': '',
                      'wealthbot_client_bundle_profile_type[marital_status]': marital_status,
                      'wealthbot_client_bundle_profile_type[nick_name]': nick_name,
                      'wealthbot_client_bundle_profile_type[phone_number]': phone_number,
                      'wealthbot_client_bundle_profile_type[spouse][birth_date]': '',
                      'wealthbot_client_bundle_profile_type[spouse][first_name]': '',
                      'wealthbot_client_bundle_profile_type[spouse][last_name]': '',
                      'wealthbot_client_bundle_profile_type[street]': street})

    response = sess.post(url_step1, data=payload_step1, headers=headers)

    return response.url

"""
    Step 2 Process
"""
def step_two(session_attributes, headers):
    url_step2 = session_attributes['url_step']
    response = sess.get(url_step2)
    token_step2 = get_token(response.text)
    
    # Input value
    answer_9 = input_value(session_attributes['Q1'])
    answer_10 = input_value(session_attributes['Q2'])
    answer_11 = input_value(session_attributes['Q3'])
    answer_12 = input_value(session_attributes['Q4'])
    payload_step2 = ({'Continue': 'Continue',
                      'wealthbot_userbundle_client_questions_type[_token]': token_step2,
                      'wealthbot_userbundle_client_questions_type[answer_9]': answer_9,
                      'wealthbot_userbundle_client_questions_type[answer_10]': answer_10,
                      'wealthbot_userbundle_client_questions_type[answer_11]': answer_11,
                      'wealthbot_userbundle_client_questions_type[answer_12]': answer_12})

    response = sess.post(url_step2, data=payload_step2, headers=headers)
    
    return response.url
    
"""
    Step 3 Process
"""    
def step_three(session_attributes, headers):
    url_step3 = session_attributes['url_step']
    url = session_attributes['url']
    response = sess.get(url_step3)
    token_step3 = get_token(response.text)

    # Input value
    groups = input_value(session_attributes['Choice1'])
    group_type = input_value(session_attributes['Choice2'])
    estimated_value = input_value(session_attributes['estimated value'])
    contributions_type = input_value(session_attributes['Choice3'])
    monthly_contributions = input_value(session_attributes['monthcontrivalue'])
    
    payload_step31 = ({'client_account_types[groups]': groups,
                      'client_account_types[_token]': token_step3})
        
    payload_step32 = ({'client_account_types[groups]': groups,
                       'client_account_types[group_type]': group_type,
                       'client_account_types[_token]': token_step3})
        
    payload_step33 = ({'wealthbot_userbundle_client_account_type[value]': estimated_value,
                       'wealthbot_userbundle_client_account_type[groupType]': group_type,
                       'wealthbot_userbundle_client_account_type[contribution_type]': contributions_type,
                       'wealthbot_userbundle_client_account_type[_token]': ''})

    payload_step34 = ({'wealthbot_userbundle_client_account_type[value]': estimated_value,
                       'wealthbot_userbundle_client_account_type[monthly_contributions]': monthly_contributions,
                       'wealthbot_userbundle_client_account_type[groupType]': group_type,
                       'wealthbot_userbundle_client_account_type[_token]': ''})
    
    url_new = build_url(url, "/client/profile")
    
    url_step31 = build_url(url_new,"/show-deposit-account-form")
    url_step32 = build_url(url_new,"/update-account-form/deposit_money")
    url_step33 = build_url(url_new,"/create-account/deposit_money")
    url_step34 = build_url(url_new,"/show-accounts-table")
    url_final = build_url(url_new,"/step-three-complete")

    response = sess.post(url_step3, data=payload_step31, headers=headers)
    response = sess.post(url_step31, data=payload_step32, headers=headers)
    response = sess.post(url_step32, data=payload_step33, headers=headers)
    response = sess.post(url_step33, data=payload_step34, headers=headers)
    response = sess.get(url_step34, headers=headers)
    response = sess.get(url_final, headers=headers)
    
    # Get portfolio information
    port_infor = get_portfolio(response.text)
    return port_infor
    
"""
    Log out
"""
def logout(session_attributes):
    url = session_attributes['url']
    headers1 = session_attributes['headers1']
    url_logout = build_url(url, "/logout")
    response = sess.get(url_logout, headers=headers1)
    
    return response

"""
    Get final portfolio
"""
def get_portfolio(html):
    # Performance of portfolio
    # Get highest return of performance
    HR = re.findall(r'<td id="highReturn">(.*?)</td>', html, re.S)[0]
    # Get lowest return of performance
    LR = re.findall(r'<td id="lowReturn">(.*?)</td>', html, re.S)[0]
    # Get specific information of portfolio
    return [HR, LR]