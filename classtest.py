
class uv_vis_calc:
	"""docstring for uv_vis_calc"""
	def __init__(self):
		super(uv_vis_calc, self).__init__()

	def moty_calc(self, UV, size):
	    constant = 1066
	    moty = UV/(1*constant)
	    
	    mw = 230.38
	    amount = .00205
	    weight = mw * moty * amount

	    dilution = weight * 200
	    # global bottom
	    # global answer

	    # answer.destroy()

	    concentration = dilution/size * 100
	    concentration = round(concentration,2)

	    return concentration

x = uv_vis_calc()

print(x.moty_calc(.783, .200))


	    

	    # answer= Label(bottom, text=str(concentration) + '%', pady = 40)
	    # answer.grid(row=3, column=1)



