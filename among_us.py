from PIL import Image, ImageDraw, ImageFont

bg = Image.open("amongusbackground.jpg")
crewmate = Image.open("crewmate-1.png").resize((119, 149))
pfp = Image.open("Cat.png").resize((50, 50))

width, height = bg.width, bg.height
username = "Loud_Cat"
frames = []

class Box():
    def __init__(self):
        self.x = -60
        self.y = (height // 2) - (pfp.height // 2)
        self.angle = 0
box = Box()

myFont = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 25)
coverBox = bg.resize((bg.width, 45))
crewguy = None
for i in range(125):
    frame = Image.new("RGB", (width, height))
    frame2 = ImageDraw.Draw(frame)
    frame.paste(bg, (0,0))
    
    frame2.text((width//2 - 150, height//2 - 25), f"{username} was the imposter", fill=(255,255,255), font=myFont)
    frame.paste(coverBox, (box.x+119, height//2 - 25 ))

    if crewguy == None:
        frame.paste(pfp, (box.x+55, box.y-50))
        frame.paste(crewmate, (box.x, box.y - 82), mask=crewmate)
        if box.x == 0:
            frame.crop((box.x, box.y - 75, box.x + 119, box.y + 149 - 75)).save("Crewguy.png")
            crewguy = Image.open("Crewguy.png")
    else:
        crewguy2 = crewguy.rotate(box.angle)
        frame.paste(crewguy2, (box.x, box.y - 75))
        box.angle += 10
        if box.angle >= 360:
            box.angle = 0
    frames.append(frame)
    box.x += 10

frames[0].save('among_us.gif', save_all=True, append_images=frames[1:], optimize=True, duration=60, loop=0) 
