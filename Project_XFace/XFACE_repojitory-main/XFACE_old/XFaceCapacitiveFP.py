# -*- coding:utf-8 -*-
import os
import serial
import time
import threading
import sys

TRUE         =  1
FALSE        =  0

# Basic response message definition
ACK_SUCCESS           = 0x00
ACK_FAIL              = 0x01
ACK_FULL              = 0x04
ACK_NO_USER           = 0x05
ACK_TIMEOUT           = 0x08
ACK_GO_OUT            = 0x0F     # The center of the fingerprint is out of alignment with sensor

# User information definition
ACK_ALL_USER          = 0x00
ACK_GUEST_USER        = 0x01
ACK_NORMAL_USER       = 0x02
ACK_MASTER_USER       = 0x03

USER_MAX_CNT          = 1000        # Maximum fingerprint number

# Command definition
CMD_ADD_1             = 0x01
CMD_ADD_2             = 0x02
CMD_ADD_3             = 0x03
CMD_DEL               = 0x04
CMD_DEL_ALL           = 0x05
CMD_USER_CNT          = 0x09
CMD_MATCH             = 0x0C
CMD_COMP_EG           = 0x23
CMD_COM_LEV           = 0x28
CMD_LP_MODE           = 0x2C
CMD_TIMEOUT           = 0x2E
CMD_DUP               = 0x2D
CMD_GET_EG            = 0x31
CMD_SET_EG            = 0x41
CMD_HEAD              = 0xF5
CMD_TAIL              = 0xF5

CMD_FINGER_DETECTED   = 0x14

g_rx_buf            = []
PC_Command_RxBuf    = []
user_id_buf         = []
Finger_SleepFlag    = 0

rLock = threading.RLock()
ser = serial.Serial("/dev/ttyTHS0", 19200, timeout=None) #yamaji

#***************************************************************************
# 0. @brief common function
#***************************************************************************/
def TxAndRxCmd(command_buf, rx_bytes_need, timeout):
    global g_rx_buf
    CheckSum = 0
    tx_buf = []

    tx_buf.append(CMD_HEAD)
    for byte in command_buf:
        tx_buf.append(byte)
        CheckSum ^= byte

    tx_buf.append(CheckSum)
    tx_buf.append(CMD_TAIL)

    ser.flushInput()
    ser.write(tx_buf)

    g_rx_buf = []
    time_before = time.time()
    time_after = time.time()
    time.sleep(2)#20
    while time_after - time_before < timeout and len(g_rx_buf) < rx_bytes_need:  # Waiting for response
        bytes_can_recv = ser.in_waiting   #2024/01/09 fujiwara inWaiting() -> in_waiting
        print(bytes_can_recv, "fujiwara_bytes_can_recv_check")   #2024/01/09 fujiwara
        if bytes_can_recv != 0:
            print(ser.read)
            g_rx_buf += ser.read(bytes_can_recv)
            #print(type(g_rx_buf))
            time_before = time.time()
        time_after = time.time()

    if len(g_rx_buf) != rx_bytes_need: 
        return ACK_TIMEOUT
    if g_rx_buf[0] != CMD_HEAD: return ACK_FAIL
    if g_rx_buf[rx_bytes_need - 1] != CMD_TAIL: return ACK_FAIL
    if g_rx_buf[1] != tx_buf[1]: return ACK_FAIL

    return  ACK_SUCCESS
def hl_to_index(array):
    return (array[0]<<8)+array[1]
def index_to_hl(index):
    return [index>>8, index&0x00FF]




#***************************************************************************
# 7. @brief   Delete Fingerprint
#***************************************************************************/
def DeleteFingerprint(index):
    global g_rx_buf
    high, low = index_to_hl(index)
    command_buf = [CMD_DEL, high, low, 0, 0]
    r = TxAndRxCmd(command_buf, 8, 2)
    if r == ACK_TIMEOUT:
        return ACK_TIMEOUT
    if r == ACK_SUCCESS and g_rx_buf[4] == ACK_SUCCESS:
        return ACK_SUCCESS
    else:
        return 0xFF

#***************************************************************************
# 9. @brief   Query the number of existing fingerprints // use to check if CFP is connected
#***************************************************************************/
try:
    def GetUserCount():
        global g_rx_buf
        command_buf = [CMD_USER_CNT, 0, 0, 0, 0]
        r = TxAndRxCmd(command_buf, 8, 0.5)
        if r == ACK_TIMEOUT:
            return ACK_TIMEOUT
        if r == ACK_SUCCESS and g_rx_buf[4] == ACK_SUCCESS:
            return g_rx_buf[3]
        else:
            return 0xFF
except Exception as e:
    print(e)

#***************************************************************************
# 11. @brief    Fingerprint matching
#***************************************************************************/
def VerifyUser():
    global g_rx_buf
    command_buf = [CMD_MATCH, 0, 0, 0, 0]
    r = TxAndRxCmd(command_buf, 8, 0.8)
    print(r,"fujiwara_r_check_XFaceCapaticiveFP")   #2024/01/09 fujiwara tuika
    #print(g_rx_buf) #[245, 12, 0, 1, 3, 0, 14, 245]
    if r == ACK_TIMEOUT:
        return (ACK_TIMEOUT, 0)
    if r == ACK_SUCCESS:
        index = hl_to_index([g_rx_buf[2],g_rx_buf[3]])
        print(ACK_SUCCESS, index)
        if index == 0:
            return (ACK_NO_USER, 0)
        return (ACK_SUCCESS, index)
    if g_rx_buf[4] == ACK_NO_USER:
        return (ACK_NO_USER, 0)
    if g_rx_buf[4] == ACK_TIMEOUT:
        return (ACK_TIMEOUT, 0)
    else:
        return (ACK_GO_OUT, 0)   # The center of the fingerprint is out of alignment with sensor

#***************************************************************************
# 15. @brief    Acquire image and upload eigenvalues
#***************************************************************************/
def ComputeEigenvalues():
    global g_rx_buf
    command_buf = [CMD_COMP_EG, 0, 0, 0, 0] 
    time.sleep(0.8)                                  #yamaji 11.21
    r = TxAndRxCmd(command_buf, 207, 0.8)
    if r == ACK_TIMEOUT:
        return (ACK_TIMEOUT, 0)
    if r == ACK_SUCCESS and g_rx_buf[4] == ACK_SUCCESS:
        return (ACK_SUCCESS, g_rx_buf[12:-2])
    else:
        return (0xFF, 0)

#***************************************************************************
# 19. @brief    Get Eigenvalues
#***************************************************************************/
def GetEigenvalues(index):
    global g_rx_buf
    high, low = index_to_hl(index)
    command_buf = [CMD_GET_EG, high, low, 0, 0]
    r = TxAndRxCmd(command_buf, 207, 2) #8+4+[193]+2 = 207
    if r == ACK_TIMEOUT:
        return ACK_TIMEOUT
    if r == ACK_SUCCESS and g_rx_buf[4] == ACK_SUCCESS:
        return g_rx_buf[12:-2]
    else:
        return 0xFF

#***************************************************************************
# 20. @brief    Register Eigenvalues
#***************************************************************************/
def SetEigenvalues(index, eigenvalues):
    print(index, eigenvalues)
    global g_rx_buf
    high, low = index_to_hl(index)

    cmb = [CMD_SET_EG, 0, 196, 0, 0]
    CheckSum = 0
    for byte in cmb:
        CheckSum ^= byte

    command_buf = [CMD_SET_EG, 0, 196, 0, 0, CheckSum, 245, 245, high, low, 3] + eigenvalues
    print(11111)
    DeleteFingerprint(index)
    print(command_buf, "fujiwara_command_buf")   #2024/01/09 fujiwara tuika
    r = TxAndRxCmd(command_buf, 8, 2)
    print(33333333)
    print(r)
    if r == ACK_TIMEOUT:
        return ACK_TIMEOUT
    if r == ACK_SUCCESS and g_rx_buf[5] == ACK_SUCCESS:   #2024/01/05 fujiwara g_rx_buf[4] -> g_rx_buf[5]
        return ACK_SUCCESS
    else:
        print("fujiwara_insert_error")   #2024/01/09 fujiwara tuika
        return 0xFF




# region develepment

def main():

    #***************************************************************************
    # 5. @brief    Register fingerprint
    #***************************************************************************/
    def AddUser():
        global g_rx_buf
        r = GetUserCount()
        if r >= USER_MAX_CNT:
            return ACK_FULL	

        command_buf = [CMD_ADD_1, 0, r+1, 3, 0]
        r = TxAndRxCmd(command_buf, 8, 6)

        if r == ACK_TIMEOUT:
            return ACK_TIMEOUT
        if r == ACK_SUCCESS and g_rx_buf[4] == ACK_SUCCESS:
            command_buf[0] = CMD_ADD_3
            r = TxAndRxCmd(command_buf, 8, 2)
            if r == ACK_TIMEOUT:
                return ACK_TIMEOUT
            if r == ACK_SUCCESS and g_rx_buf[4] == ACK_SUCCESS:
                return ACK_SUCCESS
            else:
                return ACK_FAIL
        else:
            return ACK_FAIL

    #***************************************************************************
    # 8. @brief    Clear fingerprints
    #***************************************************************************/
    def ClearAllUser():
        global g_rx_buf
        command_buf = [CMD_DEL_ALL, 0, 0, 0, 0]
        r = TxAndRxCmd(command_buf, 8, 5)
        if r == ACK_TIMEOUT:
            return ACK_TIMEOUT
        if r == ACK_SUCCESS and g_rx_buf[4] == ACK_SUCCESS:
            return ACK_SUCCESS
        else:
            return ACK_FAIL

    #***************************************************************************
    # 9. @brief   Query the number of existing fingerprints
    #***************************************************************************/
    def GetUserCount():
        global g_rx_buf
        command_buf = [CMD_USER_CNT, 0, 0, 0, 0]
        r = TxAndRxCmd(command_buf, 8, 0.1)
        if r == ACK_TIMEOUT:
            return ACK_TIMEOUT
        if r == ACK_SUCCESS and g_rx_buf[4] == ACK_SUCCESS:
            return g_rx_buf[3]
        else:
            return 0xFF

    #***************************************************************************
    # 13. @brief    Get / Set Compare Level
    #***************************************************************************/
    def GetCompareLevel():
        global g_rx_buf
        command_buf = [CMD_COM_LEV, 0, 0, 1, 0]
        r = TxAndRxCmd(command_buf, 8, 0.1)
        if r == ACK_TIMEOUT:
            return ACK_TIMEOUT
        if r == ACK_SUCCESS and g_rx_buf[4] == ACK_SUCCESS:
            return g_rx_buf[3]
        else:
            return 0xFF
    def SetCompareLevel(level):
        global g_rx_buf
        command_buf = [CMD_COM_LEV, 0, level, 0, 0]
        r = TxAndRxCmd(command_buf, 8, 0.1)
        if r == ACK_TIMEOUT:
            return ACK_TIMEOUT
        if r == ACK_SUCCESS and g_rx_buf[4] == ACK_SUCCESS:	
            return  g_rx_buf[3]
        else:
            return 0xFF

    def Analysis_PC_Command():
        global Finger_SleepFlag

        if  PC_Command_RxBuf[0] == "CMD1" and Finger_SleepFlag != 1:
            print ("Number of fingerprints already available:  %d"  % GetUserCount())
        elif PC_Command_RxBuf[0] == "CMD2" and Finger_SleepFlag != 1:
            print ("Add fingerprint  (Each entry needs to be read two times: \"beep\",put the finger on sensor, \"beep\", put up ,\"beep\", put on again) ")
            r = AddUser()
            if r == ACK_SUCCESS:
                print ("Fingerprint added successfully !")
            elif r == ACK_FAIL:
                print ("Failed: Please try to place the center of the fingerprint flat to sensor, or this fingerprint already exists !")
            elif r == ACK_FULL:
                print ("Failed: The fingerprint library is full !")

        elif PC_Command_RxBuf[0] == "CMD3" and Finger_SleepFlag != 1:
            print ("Waiting Finger......")
            r = VerifyUser()
            if r[0] == ACK_SUCCESS:            #2023/11/20 fujiwara r -> r[0]
                print ("Matching successful !")
            elif r[0] == ACK_NO_USER:            #2023/11/20 fujiwara r -> r[0]
                print ("Failed: This fingerprint was not found in the library !")
            elif r[0] == ACK_TIMEOUT:            #2023/11/20 fujiwara r -> r[0]
                print ("Failed: Time out !")
            elif r[0] == ACK_GO_OUT:            #2023/11/20 fujiwara r -> r[0]
                print ("Failed: Please try to place the center of the fingerprint flat to sensor !")
        elif PC_Command_RxBuf[0] == "CMD4" and Finger_SleepFlag != 1:
            ClearAllUser()
            print ("All fingerprints have been cleared !")
        elif PC_Command_RxBuf[0] == "CMD5" and Finger_SleepFlag != 1:
            GPIO.output(Finger_RST_Pin, GPIO.LOW)
            Finger_SleepFlag = 1
            print ("Module has entered sleep mode: you can use the finger Automatic wake-up function, in this mode, only CMD6 is valid, send CMD6 to pull up the RST pin of module, so that the module exits sleep !")
        elif PC_Command_RxBuf[0] == "CMD6":
            if rLock.acquire(blocking=True, timeout=0.6) == True:
                Finger_SleepFlag = 0
                GPIO.output(Finger_RST_Pin, GPIO.HIGH)
                time.sleep(0.25)    # Wait for module to start
                print ("The module is awake. All commands are valid !")
                rLock.release()
        elif PC_Command_RxBuf[0] == "G1":
            print ("Getting eigen values for user 3..")
            r = GetEigenvalues(1)
            if r == 8:
                print('time out')
                return
            print(r)
            print ("Setting eigen values for user 10..")
            print(SetEigenvalues(10, r))

        elif PC_Command_RxBuf[0] == "G2":
            print ("Getting eigen values for user 0-2..")
            r = GetEigenvalues(3)
            print(r)
        elif PC_Command_RxBuf[0] == "G3":
            print ("Getting eigen values for user 0-2..")
            r = GetEigenvalues(10)
            print(r)
        elif PC_Command_RxBuf[0] == "G4":
            SetEigenvalues(3, [13, 30, 151, 230, 97, 46, 157, 223, 65, 55, 143, 207, 161, 58, 151, 80, 1, 76, 35, 131, 193, 83, 16, 150, 129, 17, 161, 196, 162, 18, 26, 0, 66, 22, 142, 79, 98, 39, 30, 93, 34, 43, 165, 28, 34, 73, 17, 21, 2, 83, 25, 153, 66, 0, 254, 255, 255, 0, 0, 0, 96, 0, 128, 0, 2, 0, 50, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 178, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def Auto_Verify_Finger():
        while True:
            if rLock.acquire() == True:
                # If you enter the sleep mode, then open the Automatic wake-up function of the finger,
                # begin to check if the finger is pressed, and then start the module and match
                if Finger_SleepFlag == 1:
                    if GPIO.input(Finger_WAKE_Pin) == 1:   # If you press your finger
                        time.sleep(0.01)
                        if GPIO.input(Finger_WAKE_Pin) == 1:
                            GPIO.output(Finger_RST_Pin, GPIO.HIGH)   # Pull up the RST to start the module and start matching the fingers
                            time.sleep(0.25)	   # Wait for module to start
                            print ("Waiting Finger......Please try to place the center of the fingerprint flat to sensor !")
                            r = VerifyUser()
                            if r == ACK_SUCCESS:
                                print ("Matching successful !")
                            elif r == ACK_NO_USER:
                                print ("Failed: This fingerprint was not found in the library !")
                            elif r == ACK_TIMEOUT:
                                print ("Failed: Time out !")
                            elif r == ACK_GO_OUT:
                                print ("Failed: Please try to place the center of the fingerprint flat to sensor !")

                            #After the matching action is completed, drag RST down to sleep
                            #and continue to wait for your fingers to press
                            GPIO.output(Finger_RST_Pin, GPIO.LOW)
                rLock.release()

    GPIO.output(Finger_RST_Pin, GPIO.LOW)
    time.sleep(0.25)
    GPIO.output(Finger_RST_Pin, GPIO.HIGH)
    time.sleep(0.25)    # Wait for module to start
    print ("***************************** WaveShare Capacitive Fingerprint Reader Test *****************************")
    print ("Compare Level:  5    (can be set to 0-9, the bigger, the stricter)")
    print ("Number of fingerprints already available:  %d "  % GetUserCount())
    print (" send commands to operate the module: ")
    print ("  CMD1 : Query the number of existing fingerprints")
    print ("  CMD2 : Registered fingerprint  (Put your finger on the sensor until successfully/failed information returned) ")
    print ("  CMD3 : Fingerprint matching  (Send the command, put your finger on sensor) ")
    print ("  CMD4 : Clear fingerprints ")
    print ("  CMD5 : Switch to sleep mode, you can use the finger Automatic wake-up function (In this state, only CMD6 is valid. When a finger is placed on the sensor,the module is awakened and the finger is matched, without sending commands to match each time. The CMD6 can be used to wake up) ")
    print ("  CMD6 : Wake up and make all commands valid ")
    print ("***************************** WaveShare Capacitive Fingerprint Reader Test ***************************** ")

    # t = threading.Thread(target=Auto_Verify_Finger)
    # t.setDaemon(True)
    # t.start()

    while  True:
        print ("Please input command (CMD1-CMD6):", end=' ')
        PC_Command_RxBuf.append(input())
        Analysis_PC_Command()
        del PC_Command_RxBuf[:]    # Clear PC_Command_RxBuf and prepare for the next time
if __name__ == '__main__':
    try:
        import Jetson.GPIO as GPIO
        Finger_WAKE_Pin   = 29#23
        Finger_RST_Pin    = 33#24
        GPIO.setmode(GPIO.BOARD)#BCM
        GPIO.setup(Finger_WAKE_Pin, GPIO.IN)    # wake finger
        GPIO.setup(Finger_RST_Pin, GPIO.OUT, initial=GPIO.HIGH)  #rest finger
        main()
    except KeyboardInterrupt:
        if ser != None:
            ser.close()
        GPIO.cleanup()
        print("\n\n Test finished ! \n")
        sys.exit()
# endregion