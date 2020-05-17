import socket
import time


'''
*************************************************************
* Connect to server (on this same machine) using IP address *
*************************************************************
'''
def CaesarCipher(string, shift):
 
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  
  return cipher


def main():
    time_to_send_list = []
    index = 0
    for n_times in range(26):
    
        s = socket.socket()
        host_name = socket.gethostname()
        ip_addr = socket.gethostbyname(host_name)
        port = 12345
    
        print("I am connecting to server side: " +ip_addr)
        s.connect((ip_addr, port))
    
        print("I am sending file 'testfile.txt' for the " +str(n_times +1) +"th time" )            # Note: n_times, using range, goes from 0 thru 2
        begin_millisecond_time = int(round(time.time() * 1000))
    
        f = open('testfile.txt','r')
        file_data = f.read()
        f.close()

        data = str(file_data)
        
        secretTxt = CaesarCipher(data, index)

        secretTxt = secretTxt.encode('utf-8')
        index += 1
        s.send(secretTxt)
        ending_millisecond_time = int(round(time.time() * 1000))
        print("I am finishing sending file 'testfile.txt' for the " +str(n_times +1) +"th time" )            # Note: n_times, using range, goes from 0 thru 2
        time_it_took_to_send_in_milliseconds = ending_millisecond_time - begin_millisecond_time
        print("The time used in millisecond to send file 'testfile.txt' for " +str(n_times+1) +"th time is: ", time_it_took_to_send_in_milliseconds)
        print()
    
        time_to_send_list.append(time_it_took_to_send_in_milliseconds)
    

    s.shutdown(socket.SHUT_WR)
    s.close()
    

    print("the average time to send file 'testfile.txt' in milliseconds is: ", sum(time_to_send_list) / len(time_to_send_list))

    print("I am done")

main()
    
    

