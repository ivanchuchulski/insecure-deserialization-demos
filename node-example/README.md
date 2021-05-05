# Node.js app

Install Node.js and npm
```
apt-get install -yq nodejs npm
```

Initialize the app
```
npm init --yes
```
Install Express framework and required libraries
```
npm install express cookie-parser pug --save
```

Run the application
```
node app.js
```

How to exploit
```
echo <cookie_value> | base64 -d | sed 's/guest/admin/g' | base64
```