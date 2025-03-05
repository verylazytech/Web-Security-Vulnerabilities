# Open Redirect Vulnerability Demonstration

This folder demonstrates the Open Redirect vulnerability using a Flask-based application.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/dCfpY64WX9I/0.jpg)](https://www.youtube.com/watch?v=dCfpY64WX9I)

## Vulnerability
The application allows a user to specify a `next` URL, and it redirects the user to that URL after a successful login. If the URL is not validated properly, attackers can redirect users to malicious sites.

## Files:
- `open_redirect_vulnerable_code.py`: The code demonstrating the vulnerable behavior.


## Exploit process:
1) Run the server:
   ```
   python3 open_redirect_vulnerable_code.py
   ```
2) Enter this url:
   ```
   http://localhost:5000/login
   ```
3) Modife "Next" parameter:
   ```
   http://localhost:5000/login?next=https://www.verylazytech.com
   ```
