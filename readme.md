
This is a sample of how one might call and consume ASDM from an ASA in python.  

Packages required:  
          - bs4  
          - beautifulsoup4  
          - colorama  
          
1. pip install bs4 beautifulsoup4 colorama
2. edit test-ptracer.py with your ASA IP, credentials, and IPs/Ports
3. python test-ptracer.py


```
POST /admin/config HTTP/1.1
Accept-Encoding: identity
Content-Length: 196
Host: 172.16.127.127:8443
User-Agent: Python-urllib/2.7
Connection: close
Content-Type: text/xml
Authorization: Basic Y2lzY286c2FuZnJhbg==
   
<?xml version="1.0" encoding="ISO-8859-1"?>
<config-data config-action="merge" errors="continue">
  <cli id="0">packet-tracer input outside tcp 8.8.8.8 35290 192.168.248.248 21 xml</cli>
</config-data>
```

HTTP Server Response
```
Date: Fri, 25 May 2018 01:27:33 UTC
Connection: close
Content-Type: text/xml  

<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE ErrorList SYSTEM "urn:com-cisco-nm-callhome:ErrorList">
<ErrorList>
  <config-failure>
    <error-info id="0" type="info">
      &lt;Phase&gt;
      &lt;id&gt;1&lt;/id&gt;
      &lt;type&gt;ROUTE-LOOKUP&lt;/type&gt;
      &lt;subtype&gt;Resolve Egress Interface&lt;/subtype&gt;
      &lt;result&gt;ALLOW&lt;/result&gt;
      &lt;config&gt;
      &lt;/config&gt;
      &lt;extra&gt;
      found next-hop 192.168.248.248 using egress ifc  inside
      &lt;/extra&gt;
      &lt;/Phase&gt;
      
      &lt;Phase&gt;
      &lt;id&gt;2&lt;/id&gt;
      &lt;type&gt;ACCESS-LIST&lt;/type&gt;
      &lt;subtype&gt;&lt;/subtype&gt;
      &lt;result&gt;DROP&lt;/result&gt;
      &lt;config&gt;
      Implicit Rule
      &lt;/config&gt;
      &lt;extra&gt;
      &lt;/extra&gt;
      &lt;/Phase&gt;
         
      &lt;result&gt;
      &lt;input-interface&gt;outside&lt;/input-interface&gt;
      &lt;input-status&gt;up&lt;/input-status&gt;
      &lt;input-line-status&gt;up&lt;/input-line-status&gt;
      &lt;output-interface&gt;inside&lt;/output-interface&gt;
      &lt;output-status&gt;up&lt;/output-status&gt;
      &lt;output-line-status&gt;up&lt;/output-line-status&gt;
      &lt;action&gt;drop&lt;/action&gt;
      &lt;drop-reason&gt;(acl-drop) Flow is denied by configured rule&lt;/drop-reason&gt;
      &lt;/result&gt;
    </error-info>
  </config-failure>
</ErrorList>
```