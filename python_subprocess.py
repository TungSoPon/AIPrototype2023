from multiprocessing import process
import subprocess #สำหรับ terminal command

if __name__ == "__main__" :
    # basic terminal command
    subprocess.run(["ls" , "-ltr"])
    subprocess.run(["rm","-r","/home/thanapat_window/testfolder1"])
    print ("frist run num=48 XX=58")
    subprocess.run(["python", "/home/thanapat_window/codes/AIPrototype2023/firstpy1.py", "--num", "48", "--XX", "58"])
    print ("-----------------------------------")
    print ("second run num=60 XX=74")
    subprocess.run(["python", "/home/thanapat_window/codes/AIPrototype2023/firstpy1.py", "--num", "60", "--XX", "74"])
    print ("-----------------------------------")
    print ("third run num=88")
    subprocess.run(["python", "/home/thanapat_window/codes/AIPrototype2023/firstpy1.py", "--num", "88"])
    print ("-----------------------------------")


    #use output from other program
    process_output = subprocess.Popen(["python", "/home/thanapat_window/codes/AIPrototype2023/firstpy1.py", "--num", "88"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out, err = process_output.communicate()
    print(out.decode('utf-8'))
    print(len(out.decode('utf-8')))

    #HW เขียน subprocess sum output ทั้งหมด command 3 อันข้างบน (ตัวเลขก่อน Hello world!)


    from multiprocessing import Process
import subprocess

def run_command(command):
    process_output = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process_output.communicate()
    return out.decode('utf-8')

if __name__ == "__main__":
    # basic terminal command
    subprocess.run(["ls", "-ltr"])
    subprocess.run(["rm", "-r", "/home/thanapat_window/testfolder1"])
    
    print("frist run num=48 XX=58")
    output1 = run_command(["python", "/home/thanapat_window/codes/AIPrototype2023/firstpy1.py", "--num", "48", "--XX", "58"])
    print("-----------------------------------")

    print("second run num=60 XX=74")
    output2 = run_command(["python", "/home/thanapat_window/codes/AIPrototype2023/firstpy1.py", "--num", "60", "--XX", "74"])
    print("-----------------------------------")

    print("third run num=88")
    output3 = run_command(["python", "/home/thanapat_window/codes/AIPrototype2023/firstpy1.py", "--num", "88"])
    print("-----------------------------------")

    # Combine the lengths of the outputs
    total_length = len(output1) + len(output2) + len(output3)
    print("Total length of outputs:", total_length)
