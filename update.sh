#!/bin/sh
wget -N http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
wget -N http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
gunzip GeoIP.dat.gz GeoLiteCity.dat.gz
mv GeoLiteCity.dat /home/pfe2/Desktop/django_geo/geo
mv GeoIP.dat /home/pfe2/Desktop/django_geo/geo