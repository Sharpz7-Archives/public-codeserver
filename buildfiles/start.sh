#!/bin/sh

# Replace commas with spaces
SHARPDOMAINS=$(echo $SHARPDOMAINS | sed 's/,/ /g')
sudo sed -i "s/XXXXX/$SHARPDOMAINS/g" /sharpnet/nginx.conf

code-server --auth password --host 0.0.0.0