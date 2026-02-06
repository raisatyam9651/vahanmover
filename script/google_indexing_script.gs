/**
 * Google Indexing API Automation Script
 * 
 * Instructions:
 * 1. Paste your JSON key content into the 'CREDENTIALS' variable below.
 * 2. Set the 'SPREADSHEET_ID' to your Google Sheet ID.
 * 3. Run 'testIndexing' to verify.
 * 4. Run 'indexUrls' to process the list.
 */

// PASTE YOUR FULL JSON KEY CONTENT HERE
var CREDENTIALS = {
  // ... paste json here ...
};

// PASTE YOUR SPREADSHEET ID HERE
var SPREADSHEET_ID = 'YOUR_SPREADSHEET_ID_HERE'; 
var SHEET_NAME = 'Sheet1';

/**
 * Main function to index URLs from the Sheet.
 */
function indexUrls() {
  var service = getService();
  if (!service.hasAccess()) {
    Logger.log('Authentication failed: ' + service.getLastError());
    return;
  }

  var sheet = SpreadsheetApp.openById(SPREADSHEET_ID).getSheetByName(SHEET_NAME);
  var data = sheet.getDataRange().getValues();
  
  // Assume Row 1 is header, data starts from Row 2
  var urls = [];
  // Column A is index 0
  for (var i = 1; i < data.length; i++) {
    var url = data[i][0];
    var status = data[i][1]; // Column B for status check if needed
    if (url && status !== 'INDEXED') {
      urls.push({row: i + 1, url: url});
    }
  }
  
  // Google Quota: 200 per day usually, but let's stick to batch of 100 safe
  var batchSize = 100;
  var toProcess = urls.slice(0, batchSize);
  
  if (toProcess.length === 0) {
    Logger.log('No URLs to process.');
    return;
  }

  Logger.log('Processing ' + toProcess.length + ' URLs...');

  for (var j = 0; j < toProcess.length; j++) {
    var item = toProcess[j];
    var response = publishUrl(service, item.url);
    Logger.log('Row ' + item.row + ': ' + item.url + ' -> ' + response.status);
    
    // Optional: Update sheet with status
    if (response.status === 200) {
      sheet.getRange(item.row, 2).setValue('INDEXED'); // Column B
      sheet.getRange(item.row, 3).setValue(new Date()); // Column C timestamp
    } else {
      sheet.getRange(item.row, 2).setValue('ERROR: ' + response.status);
    }
    
    // Sleep to avoid rate limits (though simple batch is usually fine)
    Utilities.sleep(500);
  }
}

/**
 * Test function to verify single URL
 */
function testIndexing() {
  var service = getService();
  if (!service.hasAccess()) {
    Logger.log('Authentication failed: ' + service.getLastError());
    return;
  }
  
  // Replace with a real URL to test
  var urlToTest = 'https://vahanmover.com/'; 
  
  Logger.log('Testing URL: ' + urlToTest);
  var response = publishUrl(service, urlToTest);
  Logger.log('Response Status: ' + response.status);
  Logger.log('Response Body: ' + response.body);
}

/**
 * Sends a request to the Google Indexing API.
 */
function publishUrl(service, url) {
  var endpoint = 'https://indexing.googleapis.com/v3/urlNotifications:publish';
  var payload = {
    'url': url,
    'type': 'URL_UPDATED'
  };
  
  var options = {
    'method': 'post',
    'contentType': 'application/json',
    'payload': JSON.stringify(payload),
    'headers': {
      'Authorization': 'Bearer ' + service.getAccessToken()
    },
    'muteHttpExceptions': true
  };
  
  var response = UrlFetchApp.fetch(endpoint, options);
  return {
    status: response.getResponseCode(),
    body: response.getContentText()
  };
}

/**
 * Service Account Authentication using OAuth2 library pattern or direct JWT
 * For simplicity without external libraries, we implement a basic JWT signer.
 * 
 * If you have the standard OAuth2 library added to Apps Script (ID: 1B7FSrk5Zi6L1rSxxTDgDEUsPzlukDsi4KGuTMorsTQHhGBzBkMun4iDF),
 * you can use that. Below is a self-contained version using standard Utilities.
 */
function getService() {
  return {
    hasAccess: function() {
      // Basic check if we can generate a token
      try {
        var token = getJwtToken();
        return !!token;
      } catch (e) {
        this.lastError = e.toString();
        return false;
      }
    },
    getAccessToken: function() {
      return getJwtToken();
    },
    getLastError: function() {
      return this.lastError;
    },
    lastError: ''
  };
}

/**
 * Generates a signed JWT for the Service Account.
 */
function getJwtToken() {
  var privateKey = CREDENTIALS.private_key;
  var clientEmail = CREDENTIALS.client_email;
  var scopes = ['https://www.googleapis.com/auth/indexing'];
  
  if (!privateKey || !clientEmail) {
    throw new Error('Credentials not set. Please paste JSON content into CREDENTIALS variable.');
  }

  var header = {
    alg: 'RS256',
    typ: 'JWT'
  };
  
  var now = Math.floor(Date.now() / 1000);
  var claim = {
    iss: clientEmail,
    scope: scopes.join(' '),
    aud: 'https://oauth2.googleapis.com/token',
    exp: now + 3600,
    iat: now
  };
  
  var toSign = Utilities.base64EncodeWebSafe(JSON.stringify(header)) + '.' + 
               Utilities.base64EncodeWebSafe(JSON.stringify(claim));
               
  var signatureBytes = Utilities.computeRsaSha256Signature(toSign, privateKey);
  var signature = Utilities.base64EncodeWebSafe(signatureBytes);
  
  var jwt = toSign + '.' + signature;
  
  // Exchange JWT for Access Token
  var options = {
    method: 'post',
    payload: {
      grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer',
      assertion: jwt
    },
    muteHttpExceptions: true
  };
  
  var response = UrlFetchApp.fetch('https://oauth2.googleapis.com/token', options);
  var json = JSON.parse(response.getContentText());
  
  if (json.error) {
    throw new Error('Token exchange failed: ' + json.error_description);
  }
  
  return json.access_token;
}
