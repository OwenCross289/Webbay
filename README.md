# Webbay
Webbay is a moc webserver designed to serve data for the assignemnt ECM2429. It creates a local host server and sends random data with an indexed id on a get request.
Note: the order_id field does not persist across multiple runs. This means once the webserver has closed the index for the ID will start back at 0 If you wanted to have this persist I would store the OrderToSend.last_id in a file and read it in at every boot.
# API.py
The API file contains the webserver run this file to start the webserver on localhost.
# Consumer.py
The consumer file contsains an example of how to call a GET request from the web server it then prints the returned value. Make sure the webserver is running before running this.
