import os
#al_icine =os.system("lspci | grep VGA")

cikti = os.popen("lspci").read()

print("içi",cikti)

print(type(cikti))
print(os.getpid())