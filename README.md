# Centos Web Panel (CWP) - Otomatik mod_cloudflare modül kurulumu / Automatic mod_cloudflare module installing


Centos Web Panel üzerinde cloudflare kurulumuna karşın kullanıcıların gerçek IP adreslerini almak isteyen sistem yöneticileri paket kurulumunda ana dizinine kurulmayan sistem tarafından tanımlanmayan dizine kurulmasına karşın bu yazılımı kullanabilirler.


### Kurulum / Installing
```
yum install -y python34
wget https://raw.githubusercontent.com/furkansandal/cwp-mod_clouflare-auto-installer/master/kurulum.py
python3 kurulum.py
```
