from PIL import Image, ImageDraw, ImageFont #Import PIL functions
class myTemplate(): #Your template
    def __init__(self, name, description, image):
        self.name=name #Saves Name input as a self object
        self.description=description #Saves Description input as a self object
        self.image=image #Saves Image input as a self object
    def draw(self):
        """
        Draw Function
        ------------------ 
        Draws the template
        """
        img = Image.open(r'C:\Users\Dell\Pictures\AcaTemplate.png', 'r').convert('RGB') #Opens Template Image
        if self.image != '':
            pasted = Image.open(self.image).convert("RGBA") #Opens Selected Image
            pasted=pasted.resize((278, int(pasted.size[1]*(278/pasted.size[0])))) #Resize image to width fit black area's width
            pasted=pasted.crop((0, 0, 278, 322)) #Crop height
            img.paste(pasted, (31, 141)) #Pastes image into template
            imgdraw=ImageDraw.Draw(img) #Create a canvas
        font=ImageFont.truetype("C:/Windows/Fonts/Calibri.ttf", 48) #Loads font
        imgdraw.text((515,152), self.name, (0,0,0), font=font) #Draws name
        imgdraw.text((654,231), self.description, (0,0,0), font=font) #Draws description

        img.save(r'C:\Users\Dell\Pictures\AcaTemplate1.png') #Saves output

amaztemp=myTemplate('Hello, world!', 'Hi there, this is amit gupta', r'C:\Users\Dell\Pictures\AcaTemplate.png')
amaztemp.draw()