import numpy as np

def format(value):
    return "%.5f" %value

def main():
	
	init_cond_float = 0.1
	N_steps_int = 1000
	L_tail_int = 500

	dados_file = open("feigenbaum_diagram.txt","w")

	r_value_float = np.arange(0,10,0.001)

	for i_int in np.arange( len( r_value_float) ):

		orbit_ary = map( r_value_float[ i_int ], init_cond_float, N_steps_int, L_tail_int )

		for value_dbl in orbit_ary:

			dados_file.write( format( r_value_float[ i_int ] ) )
			dados_file.write( "\t\t" )
			dados_file.write( format( value_dbl ) )
			dados_file.write( "\n" )

	dados_file.close()

def map(
	r_value_float_,
	init_cond_float_,
	N_steps_int_,
	L_tail_int_ ):
	
	x_ary = N_steps_int_*[0]

	x_ary[0] = init_cond_float_

	for i_int in np.arange(1,N_steps_int_):

		x_ary[ i_int ] = x_ary[ i_int-1 ]  * np.exp( r_value_float_  * ( 1-x_ary[ i_int-1 ] ) )
		# x_ary[ i_int ] = x_ary[ i_int-1 ]  * r_value_float_  * ( 1-x_ary[ i_int-1 ] ) 

	return( x_ary[-L_tail_int_:-1] )

if __name__ == '__main__':
	main()

