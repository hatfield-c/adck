import serial
import math
import time
import numpy as np

class ConversionManifold:
	def __init__(self, alpha_keys, beta_keys):
		self.alpha_keys = alpha_keys
		self.beta_keys = beta_keys

	def AlphaToBeta(self, alpha):
		return self.ManifoldConversion(alpha, self.alpha_keys, self.beta_keys)

	def BetaToAlpha(self, beta):
		return self.ManifoldConversion(beta, self.beta_keys, self.alpha_keys)

	def ManifoldConversion(self, x, start_keys, end_keys):
		y = np.zeros(end_keys[0].shape)
		mixer_scores = []

		for i in range(len(start_keys)):
			start_key = start_keys[i]

			distance = np.linalg.norm(x - start_key)
			mixer_score = math.exp(-5 * distance)

			mixer_scores.append(mixer_score)

		mixer_scores = np.array(mixer_scores)
		mixers = mixer_scores / np.sum(mixer_scores)

		for i in range(len(start_keys)):
			end_key = end_keys[i]
			mixer_val = mixers[i]

			y = y + (mixer_val * end_key)

		return y
