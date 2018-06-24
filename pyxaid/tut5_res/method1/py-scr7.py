from PYXAID import pdos

#Example of usage:
PT = ["C","H"]
E_f = -2.5938 # Fermi energy


C6H6 = range(1,13) # = [1,2,3,4,5,6,7...]

C = [1,2,3,4,5,6]
H = range(6,13)
nat = 12
pdos.sum_pdos('pdos/x.pdos_atm#',C6H6,nat,["s","p"],"C6H6", E_f,2,1,0.1,0.02,0.1,PT) 

