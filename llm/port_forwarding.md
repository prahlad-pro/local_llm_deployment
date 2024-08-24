ngrok http --domain=sure-tightly-asp.ngrok-free.app 5002

visit - https://dashboard.ngrok.com/cloud-edge/domains

you need to learn how to do port forwarding using ng-rock.
available for both mac and windows
for mac homebrew will be helpfull to istall it.


# Latest method that is being used
___________________________________________________
direcly portforwarding the llm
https://sure-tightly-asp.ngrok-free.app -> http://localhost:1234 


### here is how it works
front end will query the llm-server deployed on render at https://local-llm-deployment.onrender.com/ask
the server will then query the port forwarded llm at https://sure-tightly-asp.ngrok-free.app -> http://localhost:1234

this method is employed in a hope that one day we will autoscale the llm-server so that each user can have its own server so that,
they can independently use llm-server, even though the LLM hosted will be same, but the history for each LLM-Server will be different 
effectively making each llm-server as an independent instance.
