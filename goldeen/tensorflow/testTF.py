import tensorflow as tf

# http://adventuresinmachinelearning.com/python-tensorflow-tutorial/

# First, create a tf constant
const = tf.constant(2.0, name="const")

# create tf variables
b = tf.placeholder(2.0, name='b')
c = tf.Variable(1.0, name='c')

# tf operations created here
d = tf.add(b, c, name='d')
e = tf.add(c, const, name='e')
a = tf.multiply(d, e, name='a')

# setup the variable initialisation
init_op = tf.global_variables_initializer()

# start the session
with tf.Session() as sess:
	#  initialise the variables
	sess.run(init_op)
	#  compute the output of the graph
	a_out = sess.run(a)
	d_out = sess.run(d)
	e_out = sess.run(e)
	print("Variable a is {}".format(a_out))
	print("Variable d is {}".format(d_out))
	print("Variable e is {}".format(e_out))