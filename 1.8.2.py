import urllib
import subprocess

print ("SimpleServer by Xaeliuz")
print ("https://github.com/xaeliuz/simpleserver")
print ("")
print ("Downloading Minecraft server...")
server = urllib.URLopener()
server.retrieve("https://s3.amazonaws.com/Minecraft.Download/versions/1.8.2/minecraft_server.1.8.2.jar", "minecraft_server.jar")
print ("Minecraft server downloaded!")
print ("")
print ("How much memory in MB do you want to allocate the Minecraft server?")
print ("Default: 1024")
print ("Answer MUST be a number without any spaces, letters or extra characters!")
xmx = raw_input ("> ")
startbat = ["java -Xmx" + xmx + "m" + " -Xms" + xmx + "m" + " -jar minecraft_server.jar nogui"]
f = open("start.bat", "w")
for item in startbat:
    f.write(str(item) + "\n")
f.close()
startsh = ["java -Xmx" + xmx + "m" + " -Xms" + xmx + "m" + " -jar minecraft_server.jar nogui"]
f = open("start.sh", "w")
for item in startsh:
    f.write(str(item) + "\n")
f.close()
p = subprocess.Popen('chmod +x start.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print line,
retval = p.wait()
print ("")
print ("Setup completed!")
print ("Run either start.bat or start.sh depending on your operating system.")
print ("If you are running Windows, use start.bat.")
print ("If you are running Linux, use start.sh.")