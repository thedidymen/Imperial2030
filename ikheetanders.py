import logging



# log.debug("hello world")
# log.info("All is well")
# log.warn("Fire fire")
# log.error("Houston...... waaa")


class A:
	def __init__(self):
		log = logging.getLogger("ClassA")
		log.setLevel(logging.DEBUG)
		ch = logging.StreamHandler()
		ch.setLevel(logging.DEBUG)
		log.addHandler(ch)
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		ch.setFormatter(formatter)
		log.debug("hello world")

class B:
	def __init__(self):
		log = logging.getLogger("ClassB")
		log.setLevel(logging.DEBUG)
		ch = logging.StreamHandler()
		ch.setLevel(logging.DEBUG)
		log.addHandler(ch)
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		ch.setFormatter(formatter)
		log.debug("hello world")


a = A()

b = B ()

c = A()
d = B()

c = A()
d = B()