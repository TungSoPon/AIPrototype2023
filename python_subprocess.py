import subprocess #สำหรับ terminal command

if __name__ == "__main__" :
    # basic terminal command
    subprocess.run(["ls" , "-ltr"])
    subprocess.run(["rm","-r","/home/thanapat_window/testfolder1"])
    subprocess.run(["python", "/home/thanapat_window/codes/AIPrototype2023/firstpy1.py", "--num", "48", "--XX", "58"])
    subprocess.run(["python", "/home/thanapat_window/codes/AIPrototype2023/firstpy1.py", "--num", "60", "--XX", "74"])
    subprocess.run(["python", "/home/thanapat_window/codes/AIPrototype2023/firstpy1.py", "--num", "88"])