import subprocess #สำหรับ terminal command

if __name__ == "__main__" :
    # basic terminal command
    subprocess.run(["ls" , "-ltr"])
    subprocess.run(["rm","-r","/home/thanapat_window/testfolder1"])