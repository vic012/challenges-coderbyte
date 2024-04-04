

class GeneratePermutation:

	def __init__(
		self,
		x: int,
		y: int,
		z: int,
		n: int
	) -> None:

		self._x = x
		self._y = y
		self._z = z
		self._n = n

	def without_list_comprehension(self) -> list:
		# -------------------------------------------------------------
		# -------Code without list comprehensions----------------------
		# -------------------------------------------------------------

		permutation = []

		for n_x in range(0, self._x+1, 1):

			for n_y in range(0, self._y+1, 1):

				for n_z in range(0, self._z+1, 1):

					if sum([n_x, n_y, n_z]) != self._n:
						permutation.append([n_x, n_y, n_z])

		return permutation

	def with_list_comprehension(self) -> list:
		# -------------------------------------------------------------
		# -------Code without list comprehensions----------------------
		# -------------------------------------------------------------

		permutation = [
			[n_x, n_y, n_z]
			for n_x in range(0, self._x+1, 1)
			for n_y in range(0, self._y+1, 1)
			for n_z in range(0, self._z+1, 1)
			if sum([n_x, n_y, n_z]) != self._n
		]

		return permutation

    
if __name__ == '__main__':
	x = int(input())
	y = int(input())
	z = int(input())
	n = int(input())

	lexicographic = GeneratePermutation(x, y, z, n)
	print(lexicographic.with_list_comprehension())
