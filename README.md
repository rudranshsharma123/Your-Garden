# Your Garden (Won Best use of Google Cloud)
 
## Inspiration
I wanted to create an exclusive platform for gardening. Where people can get their questions answered in real-time with a bot trained only to handle their woes. I also wanted people to be able to see what plants they can have in their garden and which plants would look best with what they already have hence I created the companion app. The YourGardenAR app. Using this, you can see your plants in real-time and decide which ones to buy. The main app alongside the companion was made by keeping in mind the real problem of apartment dwellers. The people who want to own plants but can only own potted ones. 
## What it does
It does a few different things. It has a bot integrated into the application which would handle specific questions aimed at gardening. I have also coded a screen from where you can buy plants. It also shows you all the search keywords which a particular user has asked the bot over a lifetime. The companion app uses the power of AR to project the models of potted plants into the real world allowing you to see exactly how they look like in your own backyard. 

## How I built it
I built the Chat Bot using Diagflow ES. The backend for the webhooks and all the API calls was handled by a flask server and the main application was developed using flutter. The companion app was made using Unity 3D's AR Foundation. For database I have used CockroachDB and I have used Repl.it as my server of choice for development and testing. The same server can be deployed anywhere using any cloud provider.

## Challenges we ran into
There were many challenges I faced along the way. I had never built a backend before so understanding how a server works and coding together a flask server was a very big challenge. Using Dialogflow ES for the first time wasn't easy. I stayed up all night reading through documentation. I also wasn't able to integrate NLP into the project because of the 5 sec limit of DiagFlow ES. So, I had to create my own response cleansing algorithm. I also faced some major issues with Cockroach DB and using it on replit. It did not support installation of Psycopg2 which is neccasory for any POSTGRE SQL to be able to run on a python based server. So, handling that was also a major challenge. Adding everything to flutter, calling and cleansing responses was also a big challenge. 

## Accomplishments that we're proud of
I am very proud of the fact that despite every challenge I faced I was able to complete the application and submit it. 

## What we learned
I learned a lot about servers, flask, DiagFlow, webhooks, flutter, API calls and creation, AR, Unity, Repl.it, Cockroach DB, PonyORM and a lot more. 

## What's next for Your Garden
Next and immediate steps would be to extend the functionality to add the whole e-commerce section. Also to extend DiagFlow ES to CX allowing me to have further control over the bot. Also, polishing UI and integrating the companion app into the main one.


By the time this project will be evaluated the server will be shut down. Replit creates issues with long running servers and I cannot afford to host it elsewhere. Also, I have included the link to diagflow chat bot. Without server it might not work much but it will still handle all the small talks
