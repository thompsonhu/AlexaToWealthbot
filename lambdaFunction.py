# -*- coding: utf-8 -*-
"""
@author: Thompson Hu & Wesley Wang
"""
from __future__ import print_function
import requestFun
import basicFun

# --------------- Questions in different stages ----------------------

register_questions = { 0:'Would you please tell me your full name?',
                       1:'Would you please tell me your nick name?',
                       2:'Please set your email address as account number.',
                       3:'Please set your password. The requirement is following: ' \
                       'At least 6 characters; At least 1 uppercase; At least 1 number; ' \
                       'No parts of first or last name'}

login_questions = { 0:'Would you please tell me your email address?',
                    1:'would you please tell me your password?'}
                   
step1_questions = { 0:'When is your birthday?',
                    1:'Would you tell me your home address? You can tell me like this: ' \
                    'I live in Clear Water Bay in Hong Kong',
                    2:'Would you tell me roughly your annual income?',
                    3:'Would you tell me rougly your net worth?',
                    4:'What is your estimated income tax bracket? You can tell me like this: ' \
                    'my estimated income tax bracket is 10 percent.',
                    5:'What is your employment status now?' \
                    'Employed, Self-Employed, Retired or Unemployed?',
                    6:'Could you please tell me about your martial status? ' \
                    'Single, Married, Divorced or Separated?',
                    7:'Would you tell me your phone number? ' \
                    'You can tell like this: my phone number is 852 2201 2937.'}
                   
step2_questions = { 0:'We\'d like to ask you a few questions. ' \
                    'Firstly, Let\'s say if your portfolio value declines by ten ' \
                    'percent in a mouth due to some market shock event, ' \
                    'then what would you do. Would you sell all of your investments, ' \
                    'or sell part of them, or keep the portfolio unchanged, ' \
                    'or even invest more to capture the potential gain from rebounding?',
                    1:'Suppose we have the following portfolios with different volatility of the return, ' \
                    'which one will your prefer, plus to minus five percentage, ' \
                    'plus to minus ten percentage, or plus to minus fifteen percentage?',
                    2:'Do you prefer an investment with steady but lower return, ' \
                    'or risky but higher return in the long run?',
                    3:'Will you need to withdraw a quarter of your portfolio within ' \
                    'the next ten years for a large expenses, like house or collage?'}      
                    
step3_questions = { 0:'Which type of process do you want to choose? ' \
                    '1: Open a new account; 2: Transfer an account; 3: Rollover a 401 plan.',
                    1:'What kind of account do you want to choose? ' \
                    '1: Personal Account; 2: Joint Account; 3: Roth IRA; 4: Traditional IRA.',
                    2:'Would you tell me your estimated value of portfolio? You must invest at least $50,000 with us.',
                    3:'Will you be making contributions or withdrawing money from the account? ' \
                    '1. making contributions; 2. withdrawing money; 3. neither',
                    4:'Would you tell me the monthly value?'}       

# --------------- Helpers that build all of the responses ----------------------
def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

# --------------- Functions that control the skill's behavior ------------------
def get_welcome_response():
    """ Initialize application """
    session_attributes = { 'register index':0, 'login index':0, 'step1 index':0,
                           'step2 index':0, 'step3 index':0,
                           'first name':'', 'last name':'', 'nick name':'', 
                           'email':'', 'password':'', 'annual income':'',
                           'birthday':'', 'address':'', 'city':'',
                           'employment type':'', 'net worth':'', 'tax':0,
                           'martial status':'', 'phone number':'',
                           'Q1':'', 'Q2':'', 'Q3':'', 'Q4':'',
                           'Choice1':'', 'Choice2':'', 'Choice3':'',
                           'estimated value':0, 'monthcontrivalue':0, 'port':'',
                           'url_step':'',
                           'url':'http://ec2-54-173-235-225.compute-1.amazonaws.com',
                           'headers1':{'origin':'http://ec2-54-173-235-225.compute-1.amazonaws.com',
                                       'upgrade-insecure-requests':'1',
                                       'content-type':'application/x-www-form-urlencoded',
                                       'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                                       'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                       'cache-control':'no-cache'},
                           'headers2':{'accept':'*/*',
                                       'origin':'http://ec2-54-173-235-225.compute-1.amazonaws.com',
                                       'x-requested-with':'XMLHttpRequest',
                                       'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                                       'content-type':'application/x-www-form-urlencoded',
                                       'cache-control':'no-cache'}
    }


    card_title = "Welcome"
    speech_output = "Welcome to Robot Advisor! It's my pleasure to meet you! " + \
    "Would you want to register or log in?"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I don't know if you heard me, " \
                    "welcome to your Robot Advisor! What can I help you?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def register_response(intent, session_attributes, register_questions):
    """ register """
    card_title = "Register"
    ind = session_attributes['register index']
    if ind == 0:
        speech_output = register_questions[ind]
    elif ind == 1:
        session_attributes['first name'] = intent['slots']['firstname']['value']
        session_attributes['last name'] = intent['slots']['lastname']['value']
        speech_output = "Hi, " + session_attributes['first name'] + "! " + register_questions[ind]
    elif ind == 2:
        if session_attributes['nick name'] != '':
            speech_output = "The account has been registered and please try again! " + \
            register_questions[ind]
        else:
            session_attributes['nick name'] = intent['slots']['nickname']['value']
            speech_output = register_questions[ind]
    else:
        email = intent['slots']['email']['value']
        session_attributes['email'] = basicFun.emailFormat(email)
        speech_output = register_questions[ind]
        
    reprompt_text = "I don't understand what you mean. " + register_questions[ind]
    session_attributes['register index'] = ind + 1
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def login_response(intent, session_attributes, login_questions):
    """ log in """ 
    card_title = "Log in"
    ind = session_attributes['login index']
    if ind == 0:
        if session_attributes['email'] != '':
            speech_output = "The email and password is invalid and please try again! " + \
            login_questions[ind]
        else:
            speech_output = login_questions[ind]
    elif ind == 1:
        email = intent['slots']['email']['value']
        session_attributes['email'] = basicFun.emailFormat(email)
        speech_output = login_questions[ind]
    
    reprompt_text = "I don't understand what you mean. " + speech_output
    session_attributes['login index'] = ind + 1
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def step1_response(intent, session_attributes, step1_questions):
    """ step one """
    card_title = "Step One"
    ind = session_attributes['step1 index'] 
    if ind == 1:
        birthday = intent['slots']['birthday']['value']
        session_attributes['birthday'] = basicFun.birthdayFormat(birthday)
    elif ind == 2:
        session_attributes['address'] = intent['slots']['address']['value']
        session_attributes['city'] = intent['slots']['city']['value']
    elif ind == 3:
        income = intent['slots']['income']['value']
        session_attributes['annual income'] = basicFun.incomeJudge(int(income))
    elif ind == 4:
        net = intent['slots']['networth']['value']
        session_attributes['net worth'] = basicFun.netJudge(int(net))
    elif ind == 5:
        session_attributes['tax'] = intent['slots']['tax']['value']
    elif ind == 6:
        employString = intent['slots']['employment']['value']
        session_attributes['employment type'] = basicFun.employFormat(employString)
    elif ind == 7:
        martialString = intent['slots']['martial']['value']
        session_attributes['martial status'] = basicFun.martialFormat(martialString)
    
    speech_output = step1_questions[ind]
    if ind == 0 and session_attributes['register index'] == 4:
        speech_output = 'Congratulation, you have successufully register a new account, ' \
        'now let\'s improve your relevant information. ' + speech_output
    elif ind == 0 and session_attributes['register index'] == 0:
        first_name = session_attributes['first name']
        speech_output = "Welcome back! " + first_name + \
        ", Now let's improve your relevant information. " + speech_output
    
    reprompt_text = "I don't understand what you mean. " + speech_output
    session_attributes['step1 index'] = ind + 1
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def step2_response(intent, session_attributes, step2_questions):
    """ step two """
    card_title = "Step Two"
    ind = session_attributes['step2 index']
    if ind == 1:
        Q1 = intent['slots']['investchoice']['value']
        session_attributes['Q1'] = basicFun.Q1Format(Q1)
    elif ind == 2:
        Q2 = intent['slots']['volatilitytype']['value']
        session_attributes['Q2'] = basicFun.Q2Format(Q2)
    elif ind == 3:
        Q3 = intent['slots']['returntype']['value']
        session_attributes['Q3'] = basicFun.Q3Format(Q3)
        
    speech_output = step2_questions[ind]
    if ind == 0 and session_attributes['step1 index'] == 8:
        speech_output = speech_output
    elif ind == 0 and session_attributes['step1 index'] == 0:
        speech_output = "Welcome back! " + speech_output
        
    reprompt_text = "I don't understand what you mean. " + speech_output
    session_attributes['step2 index'] = ind + 1
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def step3_response(intent, session_attributes, step3_questions):
    """ step three """
    card_title = "Step Three"
    ind = session_attributes['step3 index']
    if ind == 1:
        C1 = intent['slots']['stepthree']['value']
        session_attributes['Choice1'] = basicFun.C1Format(C1)
    elif ind == 2:
        C2 = intent['slots']['stepthree']['value']
        session_attributes['Choice2'] = basicFun.C2Format(C2)
    elif ind == 3:
        session_attributes['estimated value'] = intent['slots']['estimatedvalue']['value']
    elif ind == 4:
        C3 = intent['slots']['stepthree']['value']
        session_attributes['Choice3'] = basicFun.C3Format(C3)
        
    speech_output = step3_questions[ind]
    if ind == 0 and session_attributes['step2 index'] == 4:
        speech_output = speech_output
    elif ind == 0 and session_attributes['step2 index'] == 0:
        speech_output = "Welcome back! " + speech_output
        
    reprompt_text = "I don't understand what you mean. " + speech_output
    session_attributes['step3 index'] = ind + 1
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def get_portfolio_response(session_attributes):
    """ Get Portfolio """
    card_title = "Get Portfolio"
    port_infor = session_attributes['port']
    speech_output = "After 30 years, the generous expected annual return of your portfolio is " + \
    port_infor[0] + "; And the lowest expected annual return is " + port_infor[1] + \
    "; If you want to know more details, please check information in wealthbot. " + \
    "Would you want to say goodbye to me?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, None, should_end_session))
        
def handle_session_end_request(session_attributes):
    card_title = "Session Ended"
    speech_output = "Thank you for using Robot Advisor. I will miss you!"
    requestFun.logout(session_attributes)
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))
        
# ------------------------------ Request function ------------------------------
# ----------------------------------- Events -----------------------------------
def on_launch(launch_request, session):
    """ Launch the application """
    return get_welcome_response()

def on_intent(register_questions, login_questions, step1_questions,
              step2_questions, step3_questions, intent_request, session):
    """ Called when the user specifies an intent for this skill """
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    session_attributes = session.get('attributes', {})
    url = session_attributes['url']
    headers1 = session_attributes['headers1']
    headers2 = session_attributes['headers2']
    
    # Dispatch to your skill's intent handlers
    if intent_name == "RegisterIntent": 
        if session_attributes['register index'] == 4:  # Post register information to url_register
            password = intent['slots']['password']['value']
            session_attributes['password'] = basicFun.passwordFormat(password)
            session_attributes['url_step'] = requestFun.build_url(url, "/client/registration/5")
            Register = requestFun.register(session_attributes, headers1)
            if Register[0] == session_attributes['url_step']:
                session_attributes['register index'] = 2
                return register_response(intent, session_attributes, register_questions)
            else:
                # Renew url after post request
                session_attributes['url_step'] = Register[0]
                return step1_response(intent, session_attributes, step1_questions)
        else: # Keep ask questions
            return register_response(intent, session_attributes, register_questions)
            
    elif intent_name == "LoginIntent":
        if session_attributes['login index'] == 2: # Post login information to url_login
            password = intent['slots']['password']['value']
            session_attributes['password'] = basicFun.passwordFormat(password)
            session_attributes['url_step'] = requestFun.build_url(url, "/login")
            Login = requestFun.login(session_attributes, headers1)
            if Login[0] == session_attributes['url_step']:
                session_attributes['login index'] = 0
                return login_response(intent, session_attributes, register_questions)
            else:
                # Renew url after post request
                session_attributes['url_step'] = Login[0]
                # Determine which step
                url_step = Login[0]
                step = url_step.replace(requestFun.build_url(url, '/client/profile/'),'')
                if step == "step-one":
                    name = Login[1]
                    session_attributes['first name'] = name[0]
                    session_attributes['last name'] = name[1]
                    session_attributes['nick name'] = name[2]
                    return step1_response(intent, session_attributes, step1_questions)
                elif step == "step-two":
                    return step2_response(intent, session_attributes, step2_questions)
                elif step == "step-three":
                    return step3_response(intent, session_attributes, step3_questions)
                else:
                    port_infor = requestFun.get_portfolio(Login[2])
                    session_attributes['port'] = port_infor
                    return get_portfolio_response(session_attributes)
        else: # keep ask questions
            return login_response(intent, session_attributes, login_questions)
            
    elif intent_name == "StepOneIntent": 
        if session_attributes['step1 index'] == 8: # Post step one information to url_step1
            phone_number = intent['slots']['phone']['value']
            session_attributes['phone number'] = basicFun.phoneFormat(phone_number)
            # Renew url after post request
            session_attributes['url_step'] = requestFun.step_one(session_attributes, headers1)
            return step2_response(intent, session_attributes, step2_questions)
        else:
            return step1_response(intent, session_attributes, step1_questions)
            
    elif intent_name == "StepTwoIntent":
        if session_attributes['step2 index'] == 4:
            Q4 = intent['slots']['yesno']['value']
            session_attributes['Q4'] = basicFun.Q4Format(Q4)
            session_attributes['url_step'] =  requestFun.step_two(session_attributes, headers1)
            return step3_response(intent, session_attributes, step3_questions)
        else:
            return step2_response(intent, session_attributes, step2_questions)
            
    elif intent_name == "StepThreeIntent":
        if session_attributes['step3 index'] == 5:
            session_attributes['monthcontrivalue'] = intent['slots']['monthcontrivalue']['value']
            port_infor =  requestFun.step_three(session_attributes, headers2)
            session_attributes['port'] = port_infor
            return get_portfolio_response(session_attributes)
        elif session_attributes['step3 index'] == 4 and intent['slots']['stepthree']['value'] == "neither":
            port_infor =  requestFun.step_three(session_attributes, headers2)
            session_attributes['port'] = port_infor
            return get_portfolio_response(session_attributes)
        else:
            return step3_response(intent, session_attributes, step3_questions)
            
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request(session_attributes)
    else:
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    session_attributes = session.get('attributes', {})
    requestFun.logout(session_attributes)
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])

# ------------------------------- Main handler ---------------------------------
def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(register_questions, login_questions, step1_questions,
                          step2_questions, step3_questions, event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])