# A Simple Public IP Address API

![](https://raw.githubusercontent.com/groovy-sky/azure/master/images/logos/function.png)

## Introduction

This repository contains the Python script which you can use to run on Azure Functions to obtain your public IPv4 address. The code is stored in [one file](/http/__init__.py), which looks following:

![](/function.png)

For IP identifying it uses HTTP `X-Forwarded-For` header and can return the result in text/json/jsonp format.

## Demo
You can use https://showip.azurewebsites.net/api/http address to test the running solution. All currently available formats are stored in the table below:

| API URL |	Response Type | Sample Output (IPv4) |
|---|---|---|
| https://showip.azurewebsites.net/api/http | text | 1.2.3.4 |
| https://showip.azurewebsites.net/api/http?format=json | json | {"ip":"1.2.3.46"} |
| https://showip.azurewebsites.net/api/http?format=jsonp | jsonp | callback({"ip":"1.2.3.4"}); |

## Code examples

This section contains some common usage patterns from a variety of programming languages.

### Bash
```
#!/bin/bash

ip=$(curl -s https://showip.azurewebsites.net/api/http)
echo "My public IP address is: $ip"
```

### NGS (Next Generation Shell)
```
ip=`curl -s https://showip.azurewebsites.net/api/http`
echo("My public IP address is: $ip")
```

### Python
```
# This example requires the requests library be installed.  You can learn more
# about the Requests library here: http://docs.python-requests.org/en/latest/
from requests import get

ip = get('https://showip.azurewebsites.net/api/http').text
print('My public IP address is: {}'.format(ip))
```

### Ruby
```
require "net/http"

ip = Net::HTTP.get(URI("https://showip.azurewebsites.net/api/http"))
puts "My public IP Address is: " + ip
```

### PHP
```
<?php
    $ip = file_get_contents('https://showip.azurewebsites.net/api/http');
    echo "My public IP address is: " . $ip;
?>
```

### Java
```
try (java.util.Scanner s = new java.util.Scanner(new java.net.URL("https://showip.azurewebsites.net/api/http").openStream(), "UTF-8").useDelimiter("\\A")) {
    System.out.println("My current IP address is " + s.next());
} catch (java.io.IOException e) {
    e.printStackTrace();
}
```

### Perl
```
use strict;
use warnings;
use LWP::UserAgent;

my $ua = new LWP::UserAgent();
my $ip = $ua->get('https://showip.azurewebsites.net/api/http')->content;
print 'My public IP address is: '. $ip;
```

### C#
```
var httpClient = new HttpClient();
var ip = await httpClient.GetStringAsync("https://showip.azurewebsites.net/api/http");
Console.WriteLine($"My public IP address is: {ip}");
```

### VB.NET
```
Dim httpClient As New System.Net.Http.HttpClient
Dim ip As String = Await httpClient.GetStringAsync("https://showip.azurewebsites.net/api/http")
Console.WriteLine($"My public IP address is: {ip}")
```

### Go
```
package main

import (
        "io/ioutil"
        "net/http"
        "os"
)

func main() {
        res, _ := http.Get("https://showip.azurewebsites.net/api/http")
        ip, _ := ioutil.ReadAll(res.Body)
        os.Stdout.Write(ip)
}
```

### Racket
```
(require net/url)

(define ip (port->string (get-pure-port (string->url "https://showip.azurewebsites.net/api/http"))))
(printf "My public IP address is: ~a" ip)
```

### Lisp
```
;This example requires the drakma http package installed.
;It can be found here: http://www.weitz.de/drakma

(let ((stream
    (drakma:http-request "https://showip.azurewebsites.net/api/http" :want-stream t)))
  (let ((public-ip (read-line stream)))
    (format t "My public IP address is: ~A" public-ip)))
```

### Xojo
```
Dim s As New HTTPSecureSocket
Dim t As String = s.Get("https://showip.azurewebsites.net/api/http",10)
MsgBox "My public IP Address is: " + t
```

### Scala
```
val addr = scala.io.Source.fromURL("https://showip.azurewebsites.net/api/http").mkString
println(s"My public IP address is: $addr")
```

### Javascript
```
<script type="application/javascript">
  function getIP(json) {
    document.write("My public IP address is: ", json.ip);
  }
</script>

<script type="application/javascript" src="https://showip.azurewebsites.net/api/http?format=jsonp&callback=getIP"></script>
```

### jQuery
```
<script type="application/javascript">
  $(function() {
    $.getJSON("https://showip.azurewebsites.net/api/http?format=jsonp&callback=?",
      function(json) {
        document.write("My public IP address is: ", json.ip);
      }
    );
  });
</script>
```

### C#
```
using System;
using System.Net;

namespace PublicIP.Examples {
    class Program {
        public static void Main (string[] args) {
            WebClient webClient = new WebClient();
            string publicIp = webClient.DownloadString("https://showip.azurewebsites.net/api/http");
            Console.WriteLine("My public IP Address is: {0}", publicIp);
        }
    }
}
```

### Elixir
```
:inets.start
{:ok, {_, _, inet_addr}} = :httpc.request('http://showip.azurewebsites.net/api/http')
:inets.stop
```

### nim
```
import HttpClient
var ip = newHttpClient().getContent("https://showip.azurewebsites.net/api/http")
echo("My public IP address is: ", ip)
```

### PowerShell
```
$ip = Invoke-RestMethod -Uri 'https://showip.azurewebsites.net/api/http?format=json'
"My public IP address is: $($ip.ip)"
```

### Lua
```
http.Fetch("https://showip.azurewebsites.net/api/http", function(body) print("My ip is: " .. body ) end

PureBasic

InitNetwork()
*Buffer = ReceiveHTTPMemory("https://showip.azurewebsites.net/api/http?format=json")
If *Buffer
  ParseJSON(0, PeekS(*Buffer, MemorySize(*Buffer), #PB_UTF8))
  FreeMemory(*Buffer)
  Debug GetJSONString(GetJSONMember(JSONValue(0), "ip"))
EndIf
```

### LiveCode
```
put "My public IP address is" && url "https://showip.azurewebsites.net/api/http"
```

### Objective-C
```
NSURL *url = [NSURL URLWithString:@"https://showip.azurewebsites.net/api/http/"];
NSString *ipAddress = [NSString stringWithContentsOfURL:url encoding:NSUTF8StringEncoding error:nil];
NSLog(@"My public IP address is: %@", ipAddress);
```

### Swift
```
import Foundation

let url = URL(string: "https://showip.azurewebsites.net/api/http")

do {
    if let url = url {
        let ipAddress = try String(contentsOf: url)
        print("My public IP address is: " + ipAddress)
    }
} catch let error {
    print(error)
}
```
