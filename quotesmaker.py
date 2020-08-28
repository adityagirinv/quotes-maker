#!/usr/bin/env python3
try:
    from PIL import Image, ImageDraw, ImageFont
    import argparse,os
    import uuid
    import textwrap
    import random
    import time
except ImportError:
    print("[-] Please install requirements.txt by running \n pip install -r requirements.txt")

try:
    def get_arguments():
        ret_data1={
            "quote" : "",
            "author": " ",
            "template": None,
            "logo" : "template/0.png",
            "type" : 1
            }
        ret_data2={
            "file":"",
            "separator":"```",
            "template": None,
            "logo":"template/0.png",
            "type" : 2
            }
        parser = argparse.ArgumentParser(description="Quote maker by Aditya Giri\n either provide quote manually")
        parser.add_argument("-q", "--quote", type=str, help="To manually provide quote")
        parser.add_argument("-a", "--author", type=str, help="To manually provide Author name.\n It will remain empty if not provided")
        parser.add_argument("-t", "--template", type=int, help="To select template between 1 and 4.\n Random will be selected for each quote if not provided.\n works for both mannual quote and quotes imported from file.")
        parser.add_argument("-f", "--file", type=str, help="To manually provide file name to convert to quote.\n -s or --separator can be provided if -f used default separator is (```)")
        parser.add_argument("-s", "--separator", type=str, help="default separator is (```) \nprovide separator exists between quote and author\n check readme.md for more info on using file as input")
        parser.add_argument("-l", "--logo", type=str, help="[!] Only .png file supported\nTo add logo watermark supports transparency(optional)")
        data = parser.parse_args()
        if not data.quote and not data.file:
            print("[!]Qoutemaker Error:001\n(code to check in readme.md)\n[-] Please Provide either file name or quote \n see [-h] for more info")
            exit()
        elif data.quote and data.file:
            print("[!]Qoutemaker Error:002\n(code to check in readme.md)\n[-] [-f] and [-q] are not allowed at a time \n see [-h] for more info")
            exit()
        elif data.quote and not data.file:
            ret_data1["quote"] = data.quote
            if data.author:
                ret_data1["author"] = data.author
            if data.template:
                ret_data1["template"] = data.template
            if data.logo:
                if data.logo[-3:] != "png":
                    print("[!] Quotemaker Error:003\n(code to check in readme.md)\n[-] Currently This program only supports .png as logo watermark")
                    exit()
                if os.path.exists(data.logo) == True:
                    ret_data1["logo"] = data.logo
                if os.path.exists(data.logo) == False:
                    print("[!] Quotemaker Error:004\n(code to check in readme.md)\n[-] Specified {} doesn't exists Please Check and try again".format(data.logo))
                    exit() 
            return ret_data1
        elif data.file and not data.quote:
            if os.path.exists(data.file) == True:
                ret_data2["file"] = data.file
            if os.path.exists(data.file) == False:
                print("[!] Quotemaker Error:005\n(code to check in readme.md)\n[-] Specified File {} doesn't exists Please Check and try again".format(data.file))
                exit()
            if data.separator:
                ret_data2["separator"] = data.separator
            if data.logo:
                if data.logo[-3:] != "png":
                    print("[!] Quotemaker Error:003\n(code to check in readme.md)\n[-] Currently This program only supports .png as logo watermark")
                    exit()
                if os.path.exists(data.logo) == True:
                    ret_data2["logo"] = data.logo
                if os.path.exists(data.logo) == False:
                    print("[!] Quotemaker Error:004\n(code to check in readme.md)\n[-] Specified {} doesn't exists Please Check and try again".format(data.logo))
                    exit() 
            if data.template:
                ret_data2["template"] = data.template
            return ret_data2
            
    def random_dat(typed):
        if typed == 0:
            return random.randint(1,4)
        elif typed == 1:
            return str(uuid.uuid4().hex)

    def wrap(text,wd):
        wrapper = textwrap.TextWrapper(width=wd)
        data = wrapper.wrap(text)
        data1 = '\n'.join(data)
        return data1

    def temp1(quote,author,sz,wd,n,logo):
        back_img = Image.open("template/1.png")
        logo = Image.open(logo)
        new_width = int(.1 * back_img.width)
        logo.thumbnail((new_width,new_width))
        x = int(back_img.width*.8)
        y = int(back_img.height*.1) - int(logo.height/2)
        back_img.paste(logo,(x,y),logo)
        canvas = Image.new("RGBA",back_img.size)
        draw = ImageDraw.Draw(canvas)
        font = ImageFont.truetype("font/font1.otf", size=sz)
        format_quote = wrap(quote,wd)
        text_width, text_height = draw.textsize(format_quote,font)
        location = (back_img.width/2-text_width/2,back_img.height/2-text_height/2-18)
        draw.text(location, format_quote, font=font, fill=(255,255,255,255))
        crd_location = (.05*back_img.width,back_img.height - .1*back_img.height)
        font1 = ImageFont.truetype("font/font1.otf", size=35)
        draw.text(crd_location, author, font=font1, fill=(255,255,255,255))
        back_img.paste(canvas,canvas)
        NEW = back_img.convert("RGB")
        NEW.save("Quotes/"+str(n)+".jpg", quality=100)

    def temp2(quote,author,sz,wd,n,logo):
        back_img = Image.open("template/2.png")
        logo = Image.open(logo)
        new_width = int(.1 * back_img.width)
        logo.thumbnail((new_width,new_width))
        x = int(back_img.width*.8)
        y = int(back_img.height*.1) - int(logo.height/2)
        back_img.paste(logo,(x,y),logo)
        canvas = Image.new("RGBA",back_img.size)
        draw = ImageDraw.Draw(canvas)
        font = ImageFont.truetype("font/font3.otf", size=sz)
        format_quote = wrap(quote,wd)
        text_width, text_height = draw.textsize(format_quote,font)
        location = (back_img.width/2-text_width/2,back_img.height/2-text_height/2-18)
        draw.text(location, format_quote, font=font, fill=(255,255,255,255))
        text_width1, text_height1 = draw.textsize(author,font)
        crd_location = (int(back_img.width*.7)-text_width1/2,back_img.height - int(back_img.height*.1)-text_height1/2-18)
        font1 = ImageFont.truetype("font/font3.otf", size=35)
        draw.text(crd_location, author, font=font1, fill=(255,255,255,255))
        back_img.paste(canvas,canvas)
        NEW = back_img.convert("RGB")
        NEW.save("Quotes/"+str(n)+".jpg", quality=100)

    def temp3(quote,author,sz,wd,n,logo):
        back_img = Image.open("template/3.png")
        logo = Image.open(logo)
        new_width = int(.1 * back_img.width)
        logo.thumbnail((new_width,new_width))
        x = int(back_img.width*.8)
        y = int(back_img.height*.1) - int(logo.height/2)
        back_img.paste(logo,(x,y),logo)
        canvas = Image.new("RGBA",back_img.size)
        draw = ImageDraw.Draw(canvas)
        font = ImageFont.truetype("font/font2.ttf", size=sz)
        format_quote = wrap(quote,wd)
        text_width, text_height = draw.textsize(format_quote,font)
        location = (back_img.width/2-text_width/2,int(back_img.height*.6)-text_height/2-18)
        draw.text(location, format_quote, font=font, fill=(255,255,255,255))
        text_width1, text_height1 = draw.textsize(author,font)
        crd_location = (int(back_img.width*.52)-text_width1/2,back_img.height - int(back_img.height*.05)-text_height1/2-18)
        font1 = ImageFont.truetype("font/font2.ttf", size=35)
        draw.text(crd_location, author.upper(), font=font1, fill=(0,0,0,255))
        back_img.paste(canvas,canvas)
        NEW = back_img.convert("RGB")
        NEW.save("Quotes/"+str(n)+".jpg", quality=100)

    def temp4(quote,author,sz,wd,n,logo):
        back_img = Image.open("template/4.png")
        logo = Image.open(logo)
        new_width = int(.1 * back_img.width)
        logo.thumbnail((new_width,new_width))
        x = int(back_img.width*.8)
        y = int(back_img.height*.1) - int(logo.height/2)
        back_img.paste(logo,(x,y),logo)
        canvas = Image.new("RGBA",back_img.size)
        draw = ImageDraw.Draw(canvas)
        font = ImageFont.truetype("font/font3.otf", size=sz)
        format_quote = wrap(quote,wd)
        text_width, text_height = draw.textsize(format_quote,font)
        location = (back_img.width/2-text_width/2,int(back_img.height*.55)-text_height/2-18)
        draw.text(location, format_quote, font=font, fill=(255,255,255,255))
        text_width1, text_height1 = draw.textsize(author,font)
        crd_location = (int(back_img.width*.37)-text_width1/2,back_img.height - int(back_img.height*.1)-text_height1/2-18)
        font1 = ImageFont.truetype("font/font3.otf", size=35)
        draw.text(crd_location, author, font=font1, fill=(255,255,255,255))
        back_img.paste(canvas,canvas)
        NEW = back_img.convert("RGB")
        NEW.save("Quotes/"+str(n)+".jpg", quality=100)

    def quotesmaker(quote, author,n,t_num,logo):
        if t_num == 1 or t_num == 2 or t_num == 4:
            if len(quote)<100:
                sz=50
                wd = 27
            if len(quote)>=100 and len(quote)<=250:
                sz=40
                wd = 30
            if len(quote)>250 and len(quote)>=300:
                sz=30
                wd = 34
            if len(quote)>300:
                sz=25
                wd = 50
        if t_num == 3:
            if len(quote)<100:
                sz=50
                wd = 24
            if len(quote)>=100 and len(quote)<=250:
                sz=40
                wd = 30
            if len(quote)>250 and len(quote)>=300:
                sz=28
                wd = 37
            if len(quote)>300:
                sz=25
                wd = 50

        if t_num ==1:
            temp1(quote,author,sz,wd,n,logo)
        if t_num ==2:
            temp2(quote,author,sz,wd,n,logo)
        if t_num ==3:
            temp3(quote,author,sz,wd,n,logo)
        if t_num ==4:
            temp4(quote,author,sz,wd,n,logo)

    def condition_analysis(quote_data):
        if quote_data:
            if quote_data["type"] == 1:
                if quote_data["template"] == None:
                    file_name = random_dat(1)
                    quotesmaker(quote_data["quote"], quote_data["author"],file_name, random_dat(0), quote_data["logo"])
                    print("[+] Image has been successfully saved in Quotes/{}.jpg\n [#] You can request more template in our github page".format(file_name))
                else:
                    file_name = random_dat(1)
                    quotesmaker(quote_data["quote"], quote_data["author"],file_name, quote_data["template"], quote_data["logo"])
                    print("[+] Image has been successfully saved in Quotes/{}.jpg\n [#] You can request more template in our github page".format(file_name))
            elif quote_data["type"] == 2:
                quotes_file = open(quote_data["file"], "r").read().splitlines()
                if quote_data["template"] == None:
                    for n in range(len(quotes_file)):
                        t_num = random_dat(0)
                        t=n+1
                        quotesmaker(quotes_file[n].split(quote_data["separator"])[0],quotes_file[n].split(quote_data["separator"])[1],t,t_num,quote_data["logo"])
                    print("[+] Image has been successfully saved in Quotes/1-{}.jpg\n [#] You can request more template in our github page".format(t)) 
                else:
                    for n in range(len(quotes_file)):
                        t=n+1
                        quotesmaker(quotes_file[n].split(quote_data["separator"])[0],quotes_file[n].split(quote_data["separator"])[1],t,quote_data["template"],quote_data["logo"])
                    print("[+] Image has been successfully saved in Quotes/1-{}.jpg\n [#] You can request more template in our github page".format(t))


    try:
        os.mkdir('Quotes')
    except FileExistsError:
        pass
    quote_data = get_arguments()
    condition_analysis(quote_data)
except Exception:
    if Exception == ValueError:
        print("[-] Error encountered\n Your logo file is either corrupt or not supported")
    elif Exception == KeyboardInterrupt:
        print("[-] ctrl+c detected exiting")
        exit()
    else:
        print(Exception)
        print("[-]Error encountered Try waiting some time\n If the error repeats report us at github")
