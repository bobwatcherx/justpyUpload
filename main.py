from justpy import *
import os
import base64

def myapp():


	app = QuasarPage()
	layout = Div(classes="column q-pa-md",a=app)


	def mysubmit(self,msg):
		# AND NOW YOU CREATE FOLDER UPLOAD FOR YOU IMAGE UPLOAD 
		for x in msg.form_data:
			if x.type == "file":
				break
		# AND NOW DUPLICATE YOU FILE AND COPY TO UPLOAD FOLDER
		for i,v in enumerate(x.files):
			with open(f"upload/{v.name}","wb") as f:
				f.write(base64.b64decode(v.file_content))
				

				# AND SET IMAGE SRC TO YOU LOCATION IMAGE UPLOAD
				myimage.src = f"static/upload/{v.name}"



	# NOW I CREATE FORM LIKE HTML AND INPUT FILE AND BUTTON 
	f = Form(enctype="multipart/form-data",
		a=layout,
		submit=mysubmit
		)
	myfile = QInput(
		type="file",
		multiple=True,
		# ONLY IMAGE
		accept="image/*",
		a=f
		)
	btn = QBtn(type="submit",text="you upload",a=f)
	# AND SHOW IMAGE YOU UPLOAD HERE
	myimage = QImg(a=layout,
		style="width:300px;height:200px;margin-top:30px"
		)
	return app


justpy(myapp)