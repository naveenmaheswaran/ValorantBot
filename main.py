import discord
commandPrefix = '/'

hi=commandPrefix+"hi"
play=commandPrefix+"play"
yeslist=[[],[],[],[],[]]

class MyClient(discord.Client):
    count=[0,0,0,0,0]
    pollmaster = ["","","","",""]
    top=0

    async def on_ready(self):
        pass
        #print('Logged on as {0}!'.format(self.user))



    async def on_message(self, message):
        #print('Message from {0.author}: {0.content}'.format(message))
        await message.delete()
        if(message.author.bot):
            return
        if(message.content[0]!=commandPrefix):
            return

        if (message.content == play):
            if(self.top==6):
                await message.channel.send("No more Room max_parties=5")
                return
            author="{0.author}".format(message)
            if author in self.pollmaster:
                await message.channel.send("already poll has been started stop that to create new one")
                return

            self.pollmaster[self.top] = author
            self.top+=1
            ## chaech duplicate pa
            await message.channel.send(self.pollmaster[self.top-1]+ " wants to play Valorant now! who wanna join?")

        if (message.content == "/stop"):
            self.top -= 1
            author="{0.author}".format(message)
            if author not in self.pollmaster:
                await message.channel.send("No poll to stop")

            c=0
            for i in self.pollmaster:
                if i==author:
                    self.pollmaster[c]=""
                c=c+1

            await message.channel.send(author + " terminated joining poll")

        if (message.content == "/yy" or message.content == "/join"):
            if(self.top==0):
                await message.channel.send("No party is open you can create one")
                return
            if self.top==1:
                name = "{0.author}".format(message)
                if (self.count[0] >= 5):
                    await message.channel.send("sorry! party full max_ppl=5")
                    return
                await message.channel.send(
                    " ***** {0.author}".format(message) + " can join Valorant now with " + self.pollmaster[
                        self.top - 1] + " *****")
                if name not in yeslist[0]:
                    yeslist[0].append(name)
                    self.count[0] = self.count[0]+ 1
                await message.channel.send("-------------------------")
                await message.channel.send("***** ppl can play now*****")
                await message.channel.send("***** Total = " + str(self.count[0]) + "*****")
                for i in yeslist[0]:
                    await message.channel.send("***** " + i + " *****")
                return
            c=0
            for i in self.pollmaster:
                if(i==""):
                    continue
                await message.channel.send("/"+str(c+1)+" -- "+i)
                c=c+1
        if(message.content=="/1"):
            if(self.pollmaster[0]==""):
                await message.channel.send("room is empty")
                return
            if (self.count[0] >= 5):
                await message.channel.send("sorry! party full max_ppl=5")
                return
            name = "{0.author}".format(message)
            await message.channel.send(
                " ***** {0.author}".format(message) + " can join Valorant now with " + self.pollmaster[0] + " *****")
            if name not in yeslist[0]:
                yeslist[0].append(name)
                self.count[0] = self.count[0] + 1
            await message.channel.send("-------------------------")
            await message.channel.send("***** ppl can play now*****")
            await message.channel.send("***** Total = " + str(self.count[0]) + "*****")
            for i in yeslist[0]:
                await message.channel.send("***** " + i + " *****")
            return
        if (message.content == "/2"):
            if (self.pollmaster[1] == ""):
                await message.channel.send("room is empty")
                return
            if (self.count[1] >= 5):
                await message.channel.send("sorry! party full max_ppl=5")
                return
            name = "{0.author}".format(message)
            await message.channel.send(
                " ***** {0.author}".format(message) + " can join Valorant now with " + self.pollmaster[1] + " *****")
            if name not in yeslist[1]:
                yeslist[1].append(name)
                self.count[1] = self.count[1] + 1
            await message.channel.send("-------------------------")
            await message.channel.send("***** ppl can play now*****")
            await message.channel.send("***** Total = " + str(self.count[1]) + "*****")
            for i in yeslist[1]:
                await message.channel.send("***** " + i + " *****")
            return
        if (message.content == "/3"):
            if (self.pollmaster[2] == ""):
                await message.channel.send("room is empty")
                return
            if (self.count[2] >= 5):
                await message.channel.send("sorry! party full max_ppl=5")
                return
            name = "{0.author}".format(message)
            await message.channel.send(
                " ***** {0.author}".format(message) + " can join Valorant now with " + self.pollmaster[2] + " *****")
            if name not in yeslist[2]:
                yeslist[2].append(name)
                self.count[2] = self.count[2] + 1
            await message.channel.send("-------------------------")
            await message.channel.send("***** ppl can play now*****")
            await message.channel.send("***** Total = " + str(self.count[2]) + "*****")
            for i in yeslist[2]:
                await message.channel.send("***** " + i + " *****")
            return
        if (message.content == "/4"):
            if (self.pollmaster[3] == ""):
                await message.channel.send("room is empty")
                return
            if (self.count[3] >= 5):
                await message.channel.send("sorry! party full max_ppl=5")
                return
            name = "{0.author}".format(message)
            await message.channel.send(
                " ***** {0.author}".format(message) + " can join Valorant now with " + self.pollmaster[3] + " *****")
            if name not in yeslist[3]:
                yeslist[3].append(name)
                self.count[3] = self.count[3] + 1
            await message.channel.send("-------------------------")
            await message.channel.send("***** ppl can play now*****")
            await message.channel.send("***** Total = " + str(self.count[3]) + "*****")
            for i in yeslist[3]:
                await message.channel.send("***** " + i + " *****")
            return
        if (message.content == "/5"):
            if (self.pollmaster[4] == ""):
                await message.channel.send("room is empty")
                return
            if (self.count[4] >= 5):
                await message.channel.send("sorry! party full max_ppl=5")
                return
            name = "{0.author}".format(message)
            await message.channel.send(
                " ***** {0.author}".format(message) + " can join Valorant now with " + self.pollmaster[4] + " *****")
            if name not in yeslist[4]:
                yeslist[4].append(name)
                self.count[4] = self.count[4] + 1
            await message.channel.send("-------------------------")
            await message.channel.send("***** ppl can play now*****")
            await message.channel.send("***** Total = " + str(self.count[4]) + "*****")
            for i in yeslist[4]:
                await message.channel.send("***** " + i + " *****")
            return




        if (message.content == "/nn"):
            if (self.top==0):
                await message.channel.send("No party is open you can create one")
                return
            await message.channel.send("***** {0.author}".format(message) + " is unable to join now *****")
            name = "{0.author}".format(message)
            c=0
            for sublist in yeslist:
                if name in sublist:
                    yeslist[c].remove(name)
                    self.count[c]=self.count[c]-1
                c+=1

        if(message.content=="/yeslist"):
            await message.channel.send("-------------------------")
            listnumber=0
            for sublist in yeslist:
                await message.channel.send("***** Displaying yes list "+str(listnumber+1)+"*****")
                if self.count[listnumber]==0:
                    await message.channel.send("***** No one willing to play now *****")
                    listnumber+=1
                    continue

                await message.channel.send("***** Total = " + str(self.count[listnumber]) + "*****")
                for i in yeslist[listnumber]:
                    await message.channel.send("***** " + i + " *****")
                listnumber += 1


        if message.content==hi:
            await message.channel.send("hi! "+"{0.author}".format(message) + " have a nice day")
        if message.content=="/help":
            await message.channel.send("/hi - to great the bot ")
            await message.channel.send("/play - to ask the ppl can join the game")
            await message.channel.send("/yy or /join - to join in the party")
            await message.channel.send("/nn - to decline the RSVP")
            await message.channel.send("/stop - stop the poll only my its maker")
            await message.channel.send("/yeslist - to see all the members able to play")



client = MyClient()
client.run('NzMyNjYyOTEyNzgyNTY1NDE4.XxFvIA.dbB-0ZHFdcBLFaRB4PwwjXAEL9I')