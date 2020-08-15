#Nama : Efraim
#NRP: 1572048
#_TB_C_1572048_Efraim
#from __future__ import print_function <-- untuk mendapatkan variabel dari python 3 karena interpreter ini python 2
from __future__ import print_function

#####Fungsi print matriks######
#Kamus lokal
#i,j  : var.counter(int)
#Baris: wadah banyak baris(int)
#Kolom: wadah banyak kolom(int)
#Bil  : wadah banyak angka di belakang koma(int)
def Cetak_Hasil(Baris,Kolom,Arr,Bil):
    for i in range(0,Baris):
        for j in range(0,Kolom):
            print(round(Arr[i][j],Bil),end=' | ')
        print()
    print()
    return

#####Fungsi utama program#####
##Kamus lokal##
#i,j,k,h  : var.counter(int)
#Baris    : wadah banyak baris(int)
#Kolom    : wadah banyak kolom(int)
#Kolom_temp: wadah untuk identitas matriks(int)
#Bil      : wadah banyak angka di belakang koma(int)
#Arr      : var.matriks(float)
#Stop_1    : var.cek baris(boolean)
#Stop_2    : var.cek pivot(boolean)
#Indeks   : wadah sementara var.counter(int)
#Temp_1,Bilangan,Temp_2: wadah sementara variabel(float)
def main():
    Mulai=raw_input("Mulai program[ya/tidak] : ")
    while (Mulai=="ya"):
        Baris=int(input("Baris : "))
        Kolom=int(input("Kolom : "))
        Kolom_temp=Kolom*2
        Kolom=Kolom_temp
        Arr=[None]*Baris
        for i in range(0,Baris):
            Arr[i]=[None]*Kolom
        print("Masukan nilai")
        for i in range(0,Baris):
            print("Persamaan linier ke-"+str(i+1))
            for j in range(0,Kolom):
                if(j<(Kolom/2)):
                    Arr[i][j]=float(input("A["+str(i+1)+"]["+str(j+1)+"] : "))
                else:
                    if(i%2==0 and j==(Kolom/2)+i):
                        Arr[i][j]=1
                    elif(i%2==1 and j==(Kolom/2)+i):
                        Arr[i][j]=1
                    else:
                        Arr[i][j]=0
        Bil=int(input("Angka di belakang koma:"))
        print("")
        print("Matriks awal")
        Cetak_Hasil(Baris,Kolom,Arr,Bil)

        #Proses Eliminasi Gauss-Jordan Row echelon
        i=0
        h=0
        Stop_1=False
        while (i!=Baris and not Stop_1):
            while Arr[i][h]!=1 and not Stop_1:
                Stop_2=False
                while Arr[i][h]==0 and not Stop_2:#Jika pivot ==0 do looping
                    Indeks=99
                    k=i
                    while k!=Baris and Arr[k][h]==0:#Mencari pivot bukan nol
                        k+=1
                    if k!=Baris and Arr[k][h]!=0:#Jika ketemu pivot bukan nol
                        Indeks=k
                        Stop_2=True
                    else:
                        if h+1!=Kolom:#Pindah kolom
                            h+=1
                        else:#Hentikan looping
                            Stop_1=True
                            Stop_2=True
                if (not Stop_1 and Arr[i][h]==0):#Menukar bilangan
                    print("tukar R["+str(i+1)+"] <-> R["+str(Indeks+1)+"]")
                    for k in range(0,Kolom,1):
                        Temp_1=Arr[i][k]
                        Arr[i][k]=Arr[Indeks][k]
                        Arr[Indeks][k]=Temp_1
                    Cetak_Hasil(Baris, Kolom, Arr, Bil)
                elif (not Stop_1 and Arr[i][h]!=1):#Membagi bilangan pivot
                    Temp_1=Arr[i][h]
                    print("R["+str(i+1)+"] -> R["+str(i+1)+"]*1/("+str(Temp_1)+")")
                    for k in range(i,Kolom,1):
                        Bilangan=Arr[i][k]*(1/Temp_1)
                        Arr[i][k]=Bilangan
                    Cetak_Hasil(Baris, Kolom, Arr, Bil)

            for j in range(i+1,Baris,1):#Nolkan bilangan bawah pivot
                Temp_1=Arr[j][h]
                for k in range(0,Kolom,1):
                    Temp_2=Temp_1*Arr[i][k]*(-1)
                    Arr[j][k]=Arr[j][k]+Temp_2
                print("R["+str(i+2)+"] -> R["+str(i+2)+"]+("+str(Temp_1*-1)+")R["+str(i+1)+"]")
                Cetak_Hasil(Baris, Kolom, Arr, Bil)

            for j in range(i-1,-1,-1):#Nolkan bilangan atas pivot
                Temp_1=Arr[j][h]
                for k in range(i,Kolom,1):
                    Temp_2=Temp_1*Arr[i][k]*(-1)
                    Arr[j][k]=Arr[j][k]+Temp_2
                print("R["+str(i)+"] -> R["+str(i)+"]+("+str(Temp_1*-1)+")R["+str(i+1)+"]")
                Cetak_Hasil(Baris, Kolom, Arr, Bil)
            i+=1
            h+=1
        print("Hasil akhir")
        Cetak_Hasil(Baris, Kolom, Arr, Bil)
        Mulai=raw_input("Mulai program[ya/tidak] : ")
    print("Program Selesai, Terima kasih!")
if __name__=='__main__':
    main()
