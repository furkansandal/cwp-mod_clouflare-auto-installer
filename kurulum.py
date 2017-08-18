import os, subprocess

def kurulum():
    subprocess.call("cd", "/tmp")
    subprocess.call("yum", "install", "libtool", "git", "-y")
    subprocess.call("git", "clone", "https://github.com/cloudflare/mod_cloudflare.git")
    subprocess.call("cd", "mod_cloudflare")
    subprocess.call("/usr/local/apache/bin/apxs", "-a", "-i", "-c", "mod_cloudflare.c")
    subprocess.call("systemctl", "restart", "httpd")
    subprocess.call("clear")
    

print("""##### CENTOS WEB PANEL MOD_CLOUDFLARE OTO KURULUM/INSTALL #####
@furkansandal

1->Kurulum/Install
2->Çıkış/Exit\n""")
while True:
    secim = int(input("Seçiminiz / Your choice [1-2]: "))
    if secim==1:
        subprocess.call("clear")
        print("Kuruluma Başlanıyor / Starting Installation")
        kurulum()
        print("Başarıyla kuruldu / Successfully installed")
    elif secim==2:
        break
    else:
        print("Hatalı seçim yaptınız. / You made an incorrect choice. Bye Bye")
        break
        
