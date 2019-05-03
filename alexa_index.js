{
    "interactionModel": {
        "languageModel": {
            "invocationName": "robot advisor",
            "intents": [
                {
                    "name": "AMAZON.FallbackIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.CancelIntent",
                    "samples": [
                        "i don't want to continue"
                    ]
                },
                {
                    "name": "AMAZON.HelpIntent",
                    "samples": [
                        "how to use this application",
                        "can you show me how to use",
                        "please help me",
                        "I don't know how to use",
                        "I need help"
                    ]
                },
                {
                    "name": "AMAZON.StopIntent",
                    "samples": [
                        "good bye",
                        "see you later",
                        "bye bye",
                        "bye"
                    ]
                },
                {
                    "name": "AMAZON.NavigateHomeIntent",
                    "samples": []
                },
                {
                    "name": "LoginIntent",
                    "slots": [
                        {
                            "name": "email",
                            "type": "AMAZON.FictionalCharacter"
                        },
                        {
                            "name": "password",
                            "type": "AMAZON.FictionalCharacter"
                        }
                    ],
                    "samples": [
                        "please log in",
                        "my password is {password}",
                        "my email is {email}",
                        "log in"
                    ]
                },
                {
                    "name": "StepOneIntent",
                    "slots": [
                        {
                            "name": "birthday",
                            "type": "AMAZON.DATE"
                        },
                        {
                            "name": "address",
                            "type": "AMAZON.GB_REGION"
                        },
                        {
                            "name": "income",
                            "type": "AMAZON.NUMBER"
                        },
                        {
                            "name": "networth",
                            "type": "AMAZON.NUMBER"
                        },
                        {
                            "name": "employment",
                            "type": "employmentType"
                        },
                        {
                            "name": "phone",
                            "type": "AMAZON.FictionalCharacter"
                        },
                        {
                            "name": "martial",
                            "type": "martialType"
                        },
                        {
                            "name": "city",
                            "type": "AMAZON.GB_REGION"
                        },
                        {
                            "name": "tax",
                            "type": "AMAZON.NUMBER"
                        }
                    ],
                    "samples": [
                        "{martial}",
                        "i'm {employment} now",
                        "my net worth is {networth}",
                        "my annual income is {income}",
                        "my estimated income tax bracket is {tax} percent",
                        "my phone number is {phone}",
                        "i live in {address} in {city}",
                        "my birthday is {birthday}"
                    ]
                },
                {
                    "name": "StepTwoIntent",
                    "slots": [
                        {
                            "name": "returntype",
                            "type": "RetType"
                        },
                        {
                            "name": "volatilitytype",
                            "type": "AMAZON.FictionalCharacter"
                        },
                        {
                            "name": "investchoice",
                            "type": "InvestmentChoice"
                        },
                        {
                            "name": "yesno",
                            "type": "YESorNO"
                        }
                    ],
                    "samples": [
                        "i'm interested in {returntype} return",
                        "{yesno} i will not",
                        "{yesno} i will",
                        "i would {investchoice}",
                        "i prefer {volatilitytype} percentage",
                        "i prefer {returntype} return"
                    ]
                },
                {
                    "name": "StepThreeIntent",
                    "slots": [
                        {
                            "name": "estimatedvalue",
                            "type": "AMAZON.NUMBER"
                        },
                        {
                            "name": "monthcontrivalue",
                            "type": "AMAZON.NUMBER"
                        },
                        {
                            "name": "stepthree",
                            "type": "AMAZON.FictionalCharacter"
                        }
                    ],
                    "samples": [
                        "my contributions value is {monthcontrivalue}",
                        "{stepthree}",
                        "monthly contributions value is {monthcontrivalue}",
                        "the monthly contributions value is {monthcontrivalue}",
                        "estimated value is {estimatedvalue}",
                        "my estimated value is {estimatedvalue}"
                    ]
                },
                {
                    "name": "RegisterIntent",
                    "slots": [
                        {
                            "name": "email",
                            "type": "AMAZON.FictionalCharacter"
                        },
                        {
                            "name": "firstname",
                            "type": "AMAZON.GB_FIRST_NAME"
                        },
                        {
                            "name": "nickname",
                            "type": "AMAZON.GB_FIRST_NAME"
                        },
                        {
                            "name": "lastname",
                            "type": "AMAZON.GB_FIRST_NAME"
                        },
                        {
                            "name": "password",
                            "type": "AMAZON.FictionalCharacter"
                        }
                    ],
                    "samples": [
                        "register",
                        "set {password} as my password",
                        "my nick name is {nickname}",
                        "my full name is {lastname} {firstname}",
                        "set {email} as account number",
                        "register as client"
                    ]
                }
            ],
            "types": [
                {
                    "name": "YESorNO",
                    "values": [
                        {
                            "name": {
                                "value": "no"
                            }
                        },
                        {
                            "name": {
                                "value": "yes"
                            }
                        }
                    ]
                },
                {
                    "name": "RetType",
                    "values": [
                        {
                            "name": {
                                "value": "higher"
                            }
                        },
                        {
                            "name": {
                                "value": "lower"
                            }
                        }
                    ]
                },
                {
                    "name": "InvestmentChoice",
                    "values": [
                        {
                            "name": {
                                "value": "keep portfolio unchanged"
                            }
                        },
                        {
                            "name": {
                                "value": "keep it unchanged"
                            }
                        },
                        {
                            "name": {
                                "value": "invest more"
                            }
                        },
                        {
                            "name": {
                                "value": "buy some of them"
                            }
                        },
                        {
                            "name": {
                                "value": "buy some"
                            }
                        },
                        {
                            "name": {
                                "value": "sell all of them"
                            }
                        },
                        {
                            "name": {
                                "value": "sell part of them"
                            }
                        },
                        {
                            "name": {
                                "value": "sell all of your investments"
                            }
                        }
                    ]
                },
                {
                    "name": "martialType",
                    "values": [
                        {
                            "name": {
                                "value": "i got married"
                            }
                        },
                        {
                            "name": {
                                "value": "separated"
                            }
                        },
                        {
                            "name": {
                                "value": "divorced"
                            }
                        },
                        {
                            "name": {
                                "value": "married"
                            }
                        },
                        {
                            "name": {
                                "value": "single"
                            }
                        }
                    ]
                },
                {
                    "name": "employmentType",
                    "values": [
                        {
                            "name": {
                                "value": "unemployed"
                            }
                        },
                        {
                            "name": {
                                "value": "retired"
                            }
                        },
                        {
                            "name": {
                                "value": "self-employed"
                            }
                        },
                        {
                            "name": {
                                "value": "employed"
                            }
                        }
                    ]
                }
            ]
        }
    }
}