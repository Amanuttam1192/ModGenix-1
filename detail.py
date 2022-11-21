class Det_Report(tk.Frame):
    
		#new.geometry("100x50+665+410")
	def __init__(self):
		new =tk.Frame.__init__(self)
		new = Toplevel(self)
		#new.pack()
		new.geometry("700x650+361+100")
		new.title("Evaluation Full Report")
		global ans
		ans = (str)(ans)
		global x
		
		tk.Message(new, text=" Your Total Marks is = " + ans, font='Arial 10 underline',justify='left',aspect=1500).grid(row= 1, column=2, padx=2, pady=2,sticky=W)
		
		tk.Message(new, text=" The Similarity factor of the sentence is :            {:.2%}".format(fr/100), font='Arial 10 underline',justify='left',aspect=1500).grid(row= 2, column=2, padx=2, pady=2,sticky=W)
		tk.Message(new, text=" The Grammar accuracy of the sentence is :              {:.2%}".format(gm), font='Arial 10 underline',justify='left',aspect=1500).grid(row= 3, column=2, padx=2, pady=2,sticky=W)
		tk.Message(new, text=" The Total Keywords found in the sentence is :          {:.2%}".format(kt), font='Arial 10 underline',justify='left',aspect=10000).grid(row= 4, column=2, padx=2, pady=2,sticky=W)
		
		
		tk.Message(new, text=" The Keyword order accuracy of the sentence is :        {:.2%}".format(cm), font='Arial 10 underline',justify='left',aspect=10000).grid(row= 5, column=2, padx=2, pady=2,sticky=W)
		
		key="> "
		for k in keyword:
			if k==keyword[len(keyword)-1]:
				key= key+ " , " + k + " . "
			elif k==keyword[0]:
				key= key + k
			else:
				key= key+ " , " + k
		
		tk.Message(new, text=" Some of the Sample Answers are: "+strans, font='System 14',justify='left',aspect=200).grid(row= 6, column=2, padx=2, pady=2,sticky=W)
		tk.Message(new, text=" The Keywords Extracted are :- \n"+key, font='System 12',justify='left',aspect=900).grid(row= 7, column=2, padx=2, pady=2,sticky=W)