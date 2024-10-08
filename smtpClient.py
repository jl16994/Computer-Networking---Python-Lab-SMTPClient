from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"  # The body of the email
    endmsg = "\r\n.\r\n"  # The end of the email message

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)  # Create a socket
    clientSocket.connect((mailserver, port))  # Establish a TCP connection to the mail server
    # Fill in end

    recv = clientSocket.recv(1024).decode()  # Receive the initial response from the server
    # You can uncomment the following lines for debugging
    # print(recv)
    # if recv[:3] != '220':
    #     print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())  # Send HELO command
    recv1 = clientSocket.recv(1024).decode()  # Get server response
    # print(recv1)
    # if recv1[:3] != '250':
    #     print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFromCommand = 'MAIL FROM:<alice@example.com>\r\n'  # Replace with appropriate email address
    clientSocket.send(mailFromCommand.encode())  # Send MAIL FROM command
    recv2 = clientSocket.recv(1024).decode()  # Get server response
    # print(recv2)
    # if recv2[:3] != '250':
    #     print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptToCommand = 'RCPT TO:<bob@example.com>\r\n'  # Replace with recipient's email address
    clientSocket.send(rcptToCommand.encode())  # Send RCPT TO command
    recv3 = clientSocket.recv(1024).decode()  # Get server response
    # print(recv3)
    # if recv3[:3] != '250':
    #     print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())  # Send DATA command
    recv4 = clientSocket.recv(1024).decode()  # Get server response
    # print(recv4)
    # if recv4[:3] != '354':
    #     print('354 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())  # Send the body of the email
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())  # Send the end of the message indicator
    recv5 = clientSocket.recv(1024).decode()  # Get server response
    # print(recv5)
    # if recv5[:3] != '250':
    #     print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())  # Send QUIT command
    recv6 = clientSocket.recv(1024).decode()  # Get server response
    # print(recv6)
    # if recv6[:3] != '221':
    #     print('221 reply not received from server.')
    # Fill in end

    clientSocket.close()  # Close the connection

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
