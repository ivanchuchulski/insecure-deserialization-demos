var express = require('express');
var cookieParser = require('cookie-parser');
var crypto = require('crypto');
var app = express();

app.use(cookieParser());
app.set('view engine', 'pug');

app.get('/', function (req, res) {
  res.render('index');
});

app.get('/insecure', function (req, res) {
  greeting(getUser(req, res), res);
});

app.get('/secure', function (req, res) {
   greeting(getUserSecure(req, res), res);
});

app.listen(3000, function () {
  console.log('listening on port 3000');
});

function greeting(user, res) {
  let content = {}

  if (user == null) {
    // user provided invalid cookie
    res.status(403);
    content = 'Unauthorized';
  } else {
    content = 'Hello ' + user['name'] + '!!'
    
    // let's figure out the role
    if (user['role'] === 'admin') {
      content += ' You are an administrator!'
    } else {
      content += ' You are guest!'
    }
  }

  res.render('user', {'content': content});
}

// guest user object
var guestUser = {
  name: 'ivan',
  role: 'guest'
}

// parse the user cookie insecurely (simply trust whatever the user says)
function getUser(req, res) {
  if ('user' in req.cookies) {
    return JSON.parse(Buffer.from(req.cookies['user'], 'base64').toString());
  } else {
    // user's first visit, give them a guest cookie
    let guestAsJson = JSON.stringify(guestUser)
    let user64 = Buffer.from(guestAsJson).toString('base64')
    res.cookie('user', 
               user64, 
                { path: '/insecure', 
                  expires: new Date(Date.now() + 8 * 3600000) // cookie will be removed after 8 hours
                });

    return guestUser;
  }
}

// parse the user cookie securely
function getUserSecure(req, res) {
  let key = 'my $up3r $3cr37 k3y' // HMAC key
  
  if ('user' in req.cookies) {
    let cookie = req.cookies['user'].split('.');
    let user64 = cookie[0]
    let providedHmacBase64 = cookie[1]

    let payloadComputedHmacBase64 = crypto.createHmac('sha256', key).update(user64).digest('base64')

    if (providedHmacBase64 != payloadComputedHmacBase64) {
      return null;   // HMAC doesn't match, we can't accept this
    } else {
      return JSON.parse(Buffer.from(user64, 'base64').toString()); // HMAC matches, we can trust the data
    }
  } else {
    // user's first visit, give them a guest cookie
    let userAsJson = JSON.stringify(guestUser)
    let user64 = Buffer.from(userAsJson).toString('base64');
    let hmac64 = crypto.createHmac('sha256', key).update(user64).digest('base64');

    let cookieValue = user64 + '.' + hmac64

    res.cookie('user', 
                cookieValue, 
                { path: '/secure',
                  expires: new Date(Date.now() + 8 * 3600000) // cookie will be removed after 8 hours
                });

    return guestUser
  }
}
