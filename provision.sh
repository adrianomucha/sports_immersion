#!/usr/bin/env bash
# simple provision for Python3 ready Vagrant box with Ubuntu 14

hostname vagrant-python-env

echo ""
echo "apt-get update"
echo ""
apt-get update

echo ""
echo "Linux utils (some for Pandas and Numpy if must build from source)"
echo ""
apt-get install -y linux-headers-$(uname -r) build-essential git-core
apt-get install -y libreadline-dev
apt-get install -y libxml2-dev libxslt-dev curl libcurl4-openssl-dev \
  libatlas-base-dev libatlas3gf-base libjpeg-dev libfreetype6-dev libpng-dev
apt-get install -y gfortran

echo ""
echo "Python utils"
echo ""
apt-get install -y python3 python3-setuptools python3-dev python3-pip \
  libpq-dev pep8

echo ""
echo "apt-get cleanup"
echo ""
apt-get clean

echo ""
echo "virtualenv"
echo ""
pip3 install virtualenv

echo ""
echo "Disabling firewall"
echo ""
sudo ufw disable

reboot
