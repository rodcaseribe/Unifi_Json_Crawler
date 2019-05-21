#!/bin/bash
#pwd=/usr/lib/cgi-bin/

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<title>UNICEP- CAMPUS 2</title>'
echo '<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet"><style>h2,p,font{font-family: 'Raleway', sans-serif;}</style>'
echo '</head>'
echo '<body style="background-color:white">'
echo "<h2 style=color:blue;>Wi-FI Campus 2</h2>"
cat /var/www/html/aps
exit 0
