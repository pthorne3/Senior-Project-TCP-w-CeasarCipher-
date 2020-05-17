import socket
import time

'''
******************************************************************************
* A copy of the sample file is stored on the server, by default, to be used  *
* to compare with file being read as the client continues to send the same   *
* file up to 100 times.                                                      *
******************************************************************************
'''

server_side_file = f = open('testfile.txt','rb')
server_side_sample_data = f.read()
f.close()

# Add an incrementing number to the file name as each file is received
file_number = 0

time_to_send_list = []
total_incorrect_times_received = 0
total_correct_times_received = 0

s = socket.socket()
host_name = socket.gethostname()
ip_addr = socket.gethostbyname(host_name)
port = 12345
s.bind((ip_addr, port))

s.listen(5)
print("I am ready for any client side request")
print("--------------------------------------")
while True:
    c, addr = s.accept()
    
    begin_millisecond_time = int(round(time.time() * 1000))
    file_number = file_number +1
    
    print("I am starting receiving file 'testfile.txt' for the ", file_number, 'th time')
    print('Got connection from', addr)
    
    new_server_file_name = 'sentfile_' +str(file_number) +".txt"
    
    l = c.recv(4096)
    print("I am finishing receiving file 'testfile.txt' for the ", file_number, 'th time')
    
    new_server_file = open(new_server_file_name, 'wb')
    new_server_file.write(l)
    new_server_file.close()
    
    if server_side_sample_data == l:
        print(".. the file just uploaded is the same as the sample file")
        total_correct_times_received += 1
    else:
        print(".. the file uploaded is different from the sample file")
        total_incorrect_times_received += 1
    
    ending_millisecond_time = int(round(time.time() * 1000))
    time_it_took_to_send_in_milliseconds = ending_millisecond_time - begin_millisecond_time
    print("The time used in millisecond to receive file 'testfile.txt' for " ,file_number, "th time is: ", time_it_took_to_send_in_milliseconds)
    print()
    
    time_to_send_list.append(time_it_took_to_send_in_milliseconds)

    c.close()
    
    if file_number == 26:
        break
    
    print()

s.close()

print("the average time to send file 'testfile.txt' in milliseconds is: ", sum(time_to_send_list) / len(time_to_send_list))
print("The number of times file received correctly   is: ", total_correct_times_received)
print("The number of times file received incorrectly is: ", total_incorrect_times_received)

print("I am done")

