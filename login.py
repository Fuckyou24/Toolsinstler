import os, sys

print ("\033[1;34mSilahkan Masukkan ID & Password My-Tools")

print ("\033[1;35matau silahkan Hubungi 085240457692 ")
print ("\033[1;32mJgn Ngasal Cok ntr salah :V mampus")
ID = 'Maul'      

password = 'Palingganteng'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("ID : ")

	if uname == ID:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\034[1;32mSuksess Login To My-Tools..", 

			sys.exit()
			
sh installer.sh


		else:

			print "\033[1;32mMaaf Password Kamu Salah Silakan Coba Lagi... [?]\033[00m"

			print "Silahkan log-in kembali untuk Masuk ke My-Tools...!!\n"

			restart()



	else:

		print "\033[1;32mMaaf  ID Kamu salah Silahkan Check Kembali Untuk Masuk... [?]\033[00m"

		print "Silahkan log-in kembali untuk Login ke My-Tools...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
