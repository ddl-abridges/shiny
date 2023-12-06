# Python Shiny Apps

There are two example apps, both taken from https://github.com/posit-dev/py-shiny/tree/7ba8f90a44ee25f41aa8c258eceeba6807e0017a/examples

app.py is a basic example 

There are a couple caveats to shiny apps mentioned here: https://shiny.posit.co/py/docs/deploy-on-prem.html
1. Shiny uses WebSockets for most browser/server communication. Even as this is written in 2023, we have enterprise customers whose networks interfere with WebSocket traffic.
2. Shiny sessions hold state in memory. Therefore, from the moment a browser tab connects to a Shiny app to the moment it disconnects, all of its server communications must go to the same server and the same Python process on that server (“sticky” load balancing).

loadbalance.py is a test application to make sure that the deployment has sticky sessions configured; the application does nothing but send repeated requests to the server, which will only succeed if they connect to the same Python process that the page was loaded on.

Can switch between running these two apps by commenting/uncommenting in app.sh
