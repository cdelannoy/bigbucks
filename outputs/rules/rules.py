def findDecision(obj): #obj[0]: Title, obj[1]: Price, obj[2]: Qty, obj[3]: Owned, obj[4]: DeltaOwn, obj[5]: Value
	# {"feature": "Title", "instances": 256, "metric_value": 0.1779, "depth": 1}
	if obj[0] == 'Dir':
		# {"feature": "Owned", "instances": 124, "metric_value": 0.129, "depth": 2}
		if obj[3]<=548454.3177435239:
			# {"feature": "Qty", "instances": 122, "metric_value": 0.0672, "depth": 3}
			if obj[2]<=200446.07209588191:
				# {"feature": "DeltaOwn", "instances": 120, "metric_value": 0.0193, "depth": 4}
				if obj[4]<=8364.633333333333:
					# {"feature": "Price", "instances": 110, "metric_value": 0.0041, "depth": 5}
					if obj[1]<=603.8299634592651:
						# {"feature": "Value", "instances": 100, "metric_value": 0.0024, "depth": 6}
						if obj[5]<=167355.32:
							return 0.0
						elif obj[5]>167355.32:
							return 0.0115894324674633
						else: return 0.11594884224325407
					elif obj[1]>603.8299634592651:
						return 0.0975329300996999
					else: return 0.09753293009969989
				elif obj[4]>8364.633333333333:
					# {"feature": "Price", "instances": 10, "metric_value": 0.0659, "depth": 5}
					if obj[1]>12.91:
						# {"feature": "Value", "instances": 7, "metric_value": 0.0274, "depth": 6}
						if obj[5]<=100105.0:
							return 0.1595554270464093
						elif obj[5]>100105.0:
							return 0.1595554270464093
						else: return 0.25809054538795667
					elif obj[1]<=12.91:
						return 0.503745299145809
					else: return 0.503745299145809
				else: return 0.27404409105192523
			elif obj[2]>200446.07209588191:
				return -1.0
			else: return -1.0
		elif obj[3]>548454.3177435239:
			return 1.6180723002313753
		else: return 1.6180723002313753
	elif obj[0] == 'CEO':
		# {"feature": "DeltaOwn", "instances": 24, "metric_value": 0.2494, "depth": 2}
		if obj[4]>0.0:
			# {"feature": "Price", "instances": 19, "metric_value": 0.042, "depth": 3}
			if obj[1]>5.0:
				# {"feature": "Owned", "instances": 10, "metric_value": 0.0207, "depth": 4}
				if obj[3]>196282.0:
					# {"feature": "Value", "instances": 5, "metric_value": 0.0246, "depth": 5}
					if obj[5]<=999620.0:
						return 0.09549502727609623
					elif obj[5]>999620.0:
						return 0.194761326383289
					else: return 0.194761326383289
				elif obj[3]<=196282.0:
					# {"feature": "Qty", "instances": 5, "metric_value": 0.0207, "depth": 5}
					if obj[2]>200.0:
						return 0.0
					elif obj[2]<=200.0:
						return 0.0527611458734591
					else: return 0.0527611458734591
				else: return 0.02110445834938364
			elif obj[1]<=5.0:
				# {"feature": "Value", "instances": 9, "metric_value": 0.0715, "depth": 4}
				if obj[5]<=50000.0:
					# {"feature": "Qty", "instances": 6, "metric_value": 0.0372, "depth": 5}
					if obj[2]>1250.0:
						return 0.09704315239145726
					elif obj[2]<=1250.0:
						return 0.19450638963127856
					else: return 0.19450638963127856
				elif obj[5]>50000.0:
					return 0.45737286517571923
				else: return 0.45737286517571923
			else: return 0.24964080239948505
		elif obj[4]<=0.0:
			# {"feature": "Price", "instances": 5, "metric_value": 0.9906, "depth": 3}
			if obj[1]>2.46:
				return 0.21469043958517406
			elif obj[1]<=2.46:
				return 3.2
			else: return 3.2
		else: return 0.8117523516681393
	elif obj[0] == '10%':
		# {"feature": "Owned", "instances": 16, "metric_value": 0.1212, "depth": 2}
		if obj[3]<=8866709.0:
			# {"feature": "DeltaOwn", "instances": 9, "metric_value": 0.1866, "depth": 3}
			if obj[4]<=20.0:
				# {"feature": "Price", "instances": 7, "metric_value": 0.1484, "depth": 4}
				if obj[1]<=17.0:
					# {"feature": "Qty", "instances": 5, "metric_value": 0.1691, "depth": 5}
					if obj[2]>31529.0:
						return -0.75
					elif obj[2]<=31529.0:
						return 0.1006060513583096
					else: return 0.1006060513583096
				elif obj[1]>17.0:
					return 0.0347746323074449
				else: return 0.0347746323074449
			elif obj[4]>20.0:
				return 0.7038990685569848
			else: return 0.7038990685569848
		elif obj[3]>8866709.0:
			# {"feature": "Qty", "instances": 7, "metric_value": 0.076, "depth": 3}
			if obj[2]>13000.0:
				# {"feature": "DeltaOwn", "instances": 6, "metric_value": 0.053, "depth": 4}
				if obj[4]<=28.0:
					return 0.2939751028361757
				elif obj[4]>28.0:
					return 0.4349441683969001
				else: return 0.4349441683969001
			elif obj[2]<=13000.0:
				return 0.0
			else: return 0.0
		else: return 0.2922555354483576
	elif obj[0] == 'CFO':
		# {"feature": "Qty", "instances": 15, "metric_value": 0.7956, "depth": 2}
		if obj[2]<=16000.0:
			# {"feature": "Owned", "instances": 11, "metric_value": 0.0714, "depth": 3}
			if obj[3]>22460.0:
				# {"feature": "DeltaOwn", "instances": 7, "metric_value": 0.0269, "depth": 4}
				if obj[4]<=12.0:
					return 0.12641477282526226
				elif obj[4]>12.0:
					return 0.03652126868316527
				else: return 0.03652126868316527
			elif obj[3]<=22460.0:
				return 0.3234717343780925
			else: return 0.3234717343780925
		elif obj[2]>16000.0:
			return 2.5622359357718256
		else: return 2.5622359357718256
	elif obj[0] == 'Pres, CEO':
		# {"feature": "Qty", "instances": 10, "metric_value": 0.0422, "depth": 2}
		if obj[2]>1500.0:
			# {"feature": "Price", "instances": 6, "metric_value": 0.0335, "depth": 3}
			if obj[1]>7.05:
				return 0.1184838920853668
			elif obj[1]<=7.05:
				return 0.023352990601800235
			else: return 0.023352990601800235
		elif obj[2]<=1500.0:
			return 0.24095700001322956
		else: return 0.24095700001322956
	elif obj[0] == 'Dir, 10%':
		# {"feature": "Price", "instances": 8, "metric_value": 0.4228, "depth": 2}
		if obj[1]<=11.14:
			# {"feature": "Owned", "instances": 6, "metric_value": 0.1152, "depth": 3}
			if obj[3]>548884.0:
				# {"feature": "Qty", "instances": 5, "metric_value": 0.0241, "depth": 4}
				if obj[2]>522.0:
					return 0.12368032688970011
				elif obj[2]<=522.0:
					return 0.2310605571426545
				else: return 0.2310605571426545
			elif obj[3]<=548884.0:
				return 0.5560916378637465
			else: return 0.5560916378637465
		elif obj[1]>11.14:
			return -1.0
		else: return -1.0
	elif obj[0] == 'EVP':
		return 0.021071880491591033
	elif obj[0] == 'COO':
		return 0.09207284389733512
	elif obj[0] == 'COB, Pres, CEO':
		return 0.07161991935567623
	elif obj[0] == 'CEO, Pres':
		return 0.031515807154188134
	elif obj[0] == 'EVP, CFO':
		return 0.0603255222609386
	elif obj[0] == 'Pres':
		return 0.0029133560027413997
	elif obj[0] == 'SVP':
		return 0.1125806993053805
	elif obj[0] == 'CEO, 10%':
		return 0.5780824480775343
	elif obj[0] == 'CFO, 10%':
		return -1.0
	elif obj[0] == 'V.P. Ind. Relations & Safety':
		return 0.0590989011038068
	elif obj[0] == 'SR EVP OF SPECIAL PROJECTS':
		return 0.0038485866167501
	elif obj[0] == 'EVP, CHIEF RISK OFFICER':
		return 0.0
	elif obj[0] == 'CHIEF INNOVATION OFFICER':
		return 0.0526316141707977
	elif obj[0] == 'VP, Interim CFO, Sec., Treas.':
		return 0.1262472860620887
	elif obj[0] == 'Chief Accounting Officer':
		return 0.4073106981344337
	elif obj[0] == 'Chief Scientific Officer':
		return 0.0474074328387225
	elif obj[0] == 'Chief Commercial Officer':
		return 0.5650172459074279
	elif obj[0] == 'Pres, CEO, 10%':
		return 0.3953487753158935
	elif obj[0] == 'COB, Pres, 10%':
		return 0.0347746323074449
	elif obj[0] == 'VP, Controller':
		return 0.0037438796663435
	elif obj[0] == 'COB, CEO, 10%':
		return 0.1417313006427912
	elif obj[0] == 'Acting CFO, 10%':
		return -1.0
	elif obj[0] == 'CEO, COB, 10%':
		return 0.0857142680208842
	elif obj[0] == 'Pres of Millis Transfer':
		return 0.0
	elif obj[0] == 'Exec COB':
		return 0.3975114284779258
	elif obj[0] == 'EVP, Dir OF REG RISK MNGT':
		return 0.0038485866167501
	elif obj[0] == 'Controller':
		return 0.002132163557946
	elif obj[0] == 'Possible Member of 10% Group, 10%':
		return 0.1105263395652884
	elif obj[0] == 'GC, Secretary':
		return 0.5650172459074279
	elif obj[0] == 'Chief Administration Officer':
		return 0.0253886890070896
	elif obj[0] == 'Chief Medical Officer':
		return 0.0506328617298278
	elif obj[0] == 'EVP, Dir. Corp. Development':
		return 0.0595026698645528
	elif obj[0] == 'SVP Operations':
		return 0.2310605571426545
	elif obj[0] == 'Pres, CEO ASRV, Bank':
		return 0.0
	elif obj[0] == 'EVP & CFO':
		return 0.0172413793103448
	elif obj[0] == 'Executive Vice President':
		return 0.0172413793103448
	elif obj[0] == 'President & CEO':
		return 0.0172413793103448
	elif obj[0] == 'CEO, TSC Bank, Dir TSC':
		return 0.0168612758818684
	elif obj[0] == 'SVP, CFO':
		return 0.0416666252745538
	elif obj[0] == 'Chief Strategy Officer':
		return 0.265568532440407
	elif obj[0] == 'SVP, CFO, Treasurer':
		return 0.1044644869722023
	elif obj[0] == 'EVP, COO':
		return 0.0
	elif obj[0] == 'GC':
		return 0.1105263358668277
	elif obj[0] == 'Pres, COO':
		return 0.0
	elif obj[0] == 'CHRO':
		return 0.1105263358668277
	elif obj[0] == 'VP, CTO':
		return 0.002132163557946
	elif obj[0] == 'EVP, HR':
		return 0.2844444557472511
	else: return 0.2844444557472511
