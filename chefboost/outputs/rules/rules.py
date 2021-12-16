def findDecision(obj): #obj[0]: Alt, obj[1]: Bar, obj[2]: Fri, obj[3]: Hun, obj[4]: Pat, obj[5]: Price, obj[6]: Rain, obj[7]: Res, obj[8]: Type, obj[9]: Est
	# {"feature": "Pat", "instances": 12, "metric_value": 1.0, "depth": 1}
	if obj[4] == 'Full':
		# {"feature": "Type", "instances": 6, "metric_value": 0.9183, "depth": 2}
		if obj[8] == 'T':
			# {"feature": "Fri", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2] == 'F':
				return 'F'
			elif obj[2] == 'T':
				return 'T'
			else: return 'T'
		elif obj[8] == 'B':
			# {"feature": "Alt", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0] == 'F':
				return 'F'
			elif obj[0] == 'T':
				return 'T'
			else: return 'T'
		elif obj[8] == 'F':
			return 'F'
		elif obj[8] == 'I':
			return 'F'
		else: return 'F'
	elif obj[4] == 'Some':
		return 'T'
	elif obj[4] == 'None':
		return 'F'
	else: return 'F'
