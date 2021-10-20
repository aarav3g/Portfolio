// *****************************************************************************
// Copyright 2019 Amazon.com, Inc. or its affiliates.  All Rights Reserved. 

// You may not use this file except in compliance with the terms and conditions 
// set forth in the accompanying LICENSE.TXT file.

// THESE MATERIALS ARE PROVIDED ON AN "AS IS" BASIS. AMAZON SPECIFICALLY 
// DISCLAIMS, WITH RESPECT TO THESE MATERIALS, ALL WARRANTIES, EXPRESS, IMPLIED, 
// OR STATUTORY, INCLUDING THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS 
// OR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT.
// *****************************************************************************

        
        
const Alexa = require('ask-sdk-core');
const util = require('./util');
const weatherClient = require('./weather-client');

const GetWeatherApiHandler = {
    canHandle(handlerInput) {
        return util.isApiRequest(handlerInput, 'GetWeatherApi');
    },
    handle(handlerInput) {
        const typeNameWithId = util.getTypeNameWithIdFromApiRequestSlots(handlerInput);

        if (!typeNameWithId) {
            // We couldn't match this city value to our slot, we'll return empty and let the response template handle it.
            return {apiResponse:{}};
        }

        // "Call a service" to get the weather for this location and date.
        const weather = weatherClient.getWeather(typeNameWithId.id);

        const response = {
            apiResponse: {
                typeName: typeNameWithId.name,
                fact: weather.fact,
                fact2: weather.fact2,
                fact3: weather.fact3,
                fact4: weather.fact4,
                fact5: weather.fact5,
                fact6: weather.fact6,
                fact7: weather.fact7,
                fact8: weather.fact8,
                fact9: weather.fact9,
                fact10: weather.fact10,
                fact11: weather.fact11,
                fact12: weather.fact12,
                fact13: weather.fact13,
                fact14: weather.fact14,
                fact15: weather.fact15,
                fact16: weather.fact16,
                fact17: weather.fact17,
                fact18: weather.fact18,
                fact19: weather.fact19,
                fact20: weather.fact20,
                fact21: weather.fact21,
                fact22: weather.fact22,
                fact23: weather.fact23,
                fact24: weather.fact24,
                fact25: weather.fact25,
                fact26: weather.fact26,
                fact27: weather.fact27,
                fact28: weather.fact28,
                fact29: weather.fact29,
                fact30: weather.fact30,
                fact31: weather.fact31,
                fact32: weather.fact32,
                fact33: weather.fact33,
                fact34: weather.fact34,
                fact35: weather.fact35,
                fact36: weather.fact36,
                fact37: weather.fact37,
                fact38: weather.fact38,
                fact39: weather.fact39,
                fact40: weather.fact40,
                fact41: weather.fact41,
                fact42: weather.fact42,
                fact43: weather.fact43,
                fact44: weather.fact44,
                fact45: weather.fact45,
                fact46: weather.fact46,
                fact47: weather.fact47,
                fact48: weather.fact48,
                fact49: weather.fact49,
                
            }
        }


        return response;
        }
}
const SessionEndedRequestHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'SessionEndedRequest';
    },
    handle(handlerInput) {
        // Any cleanup logic goes here.
        return handlerInput.responseBuilder.getResponse();
    }
};

// The intent reflector is used for interaction model testing and debugging.
// It will simply repeat the intent the user said. You can create custom handlers
// for your intents by defining them above, then also adding them to the request
// handler chain below.
const IntentReflectorHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest';
    },
    handle(handlerInput) {
        const intentName = Alexa.getIntentName(handlerInput.requestEnvelope);
        const speakOutput = `You just triggered ${intentName}`;

        return handlerInput.responseBuilder
            .speak(speakOutput)
            .getResponse();
    }
};

// Generic error handling to capture any syntax or routing errors. If you receive an error
// stating the request handler chain is not found, you have not implemented a handler for
// the intent being invoked or included it in the skill builder below.
const ErrorHandler = {
    canHandle() {
        return true;
    },
    handle(handlerInput, error) {
        console.error(`Error handled: ${error.message}`);
        console.error(`Error stack`, JSON.stringify(error.stack));
        console.error(`Error`, JSON.stringify(error));

        const speakOutput = `Sorry, I had trouble doing what you asked. Please try again.`;

        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};

// *****************************************************************************
// These simple interceptors just log the incoming and outgoing request bodies to assist in debugging.

const LogRequestInterceptor = {
    process(handlerInput) {
        console.log(`REQUEST ENVELOPE = ${JSON.stringify(handlerInput.requestEnvelope)}`);
    },
};

const LogResponseInterceptor = {
    process(handlerInput, response) {
        console.log(`RESPONSE = ${JSON.stringify(response)}`);
    },
};

// The SkillBuilder acts as the entry point for your skill, routing all request and response
// payloads to the handlers above. Make sure any new handlers or interceptors you've
// defined are included below. The order matters - they're processed top to bottom.
exports.handler = Alexa.SkillBuilders.custom()
    .addRequestHandlers(
        GetWeatherApiHandler,
        SessionEndedRequestHandler,
        IntentReflectorHandler, // make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers
    )
    .addErrorHandlers(ErrorHandler)
    .addRequestInterceptors(LogRequestInterceptor)
    .addResponseInterceptors(LogResponseInterceptor)
    .lambda();
