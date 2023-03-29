from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("story.png", x=1.2, h=0.8)
        self.ln(0.1)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 12)
        self.cell(w=0, h=0.5, txt='Dev Stories LTDA',
                  align='l', new_x='LMARGIN', new_y='NEXT')
        # Performing a line break:
        self.ln(0.1)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-1.5)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(
            w=0, h=1, txt=f"Página {self.page_no()}/{{nb}} - Dev Stories - Direitos Reservados", align="C")

pdf = PDF(orientation='p', unit='cm')
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(w=0, h=0.5, txt="Mexico is the DREAM!",
         align='c', new_x='LMARGIN', new_y='NEXT')
pdf.set_font("helvetica", style='', size=12)
pdf.ln(0.5)
pdf.multi_cell(
    w=0, h=0.5, txt='''Rumour has it targeted online advertising was developed because the internet was upset that you could read it but it couldn't read you. Trepidelicious. I'm in a band that does Metallica covers with our private parts - it's called Myphallica. Petrovache. A tagline for an airline: Take the High Road. You say potatoe, I say starchy carbs. Are there Out-of-Stock photos? Gafuffle.

If you wake up with a giant zit, you are really facing your fears when you look in the mirror. Smiling could easily be misinterpreted for showing your teeth to someone because they said something that made you happy. If you wake up with a giant zit, you are really facing your fears when you look in the mirror. Rumour has it targeted online advertising was developed because the internet was upset that you could read it but it couldn't read you. Trepidelicious. A tagline for a car company that prides itself on its morals and ethics: Take the High Road.

If the word kerning is kerned poorly, it kind of looks like learning - which is appropriate because both are important. If you wake up with a giant zit, you are really facing your fears when you look in the mirror. Do we make money or does money make us? Chezwich. I bet most serial killers play the drums. I think of a lot of good ideas when going to the bathroom - I guess I have a real stream of consciousness.

A tagline for an airline: Take the High Road. Tim Horton was a hockey player but is the name of a coffee chain, which means my dream of a goat sanctuary being my legacy is not unrealistic. If Fantasy Hockey actually lived up to its name, every team would have Henrik Lundqvist and Joffrey Lupul on it. INjuries always keep you OUT of things. Visticula. I think of a lot of good ideas when going to the bathroom - I guess I have a real stream of consciousness.

We need more werkin and less twerkin if you ask me. Balooby. A tagline for a special highway that is easy to navigate while under the influence of drugs: Take the High Road. I'm still upset that Tie Domi didn't name his child Tyson. This is a true fact: I never had a fear of heights until I fell off a roof. Why don't we call glasses duocles.

Why don't we call glasses duocles. Logan Ipsum will loop at some point. If you were a member of the Bloods and became paralyzed do you then become a member of the Crips?. We need more werkin and less twerkin if you ask me. Balooby. Pantone is a colour but also the singular version of pants.

This is a true fact: I never had a fear of heights until I fell off a roof. You know the Grammys are a joke when Future doesn't win Best Everything. I have never known a Jack that was in good enough shape to name bodybuilding after him. Twitter is the rice of social media. Twitter is the rice of social media.

North America should be called Russia since people are always moving so fast. Gralitica. For the name of an act as serious as killing someone, assassination literally translates to buttbuttination. Why don't we call glasses duocles. We say we are walking the dog, but the dog always leads. I'm the only person in the world with my name.

I'm still upset that Tie Domi didn't name his child Tyson. You know the Grammys are a joke when Future doesn't win Best Everything. Smiling could easily be misinterpreted for showing your teeth to someone because they said something that made you happy. A tagline for a car company that prides itself on its morals and ethics: Take the High Road. You should "listen to my mixtape" (check out the rest of my portfolio).

I don't need a big house, just a two-floor condo - you could say I have lofty expectations. If the word kerning is kerned poorly, it kind of looks like learning - which is appropriate because both are important. If you wake up with a giant zit, you are really facing your fears when you look in the mirror. Most streets are two-way streets...why does that make love so special?. We need more werkin and less twerkin if you ask me. Balooby.

I bet most serial killers play the drums. If the word kerning is kerned poorly, it kind of looks like learning - which is appropriate because both are important. Logan Ipsum will loop at some point. Why don't we call glasses duocles. I don't need a big house, just a two-floor condo - you could say I have lofty expectations.

Logan Ipsum will loop at some point. North America should be called Russia since people are always moving so fast. Gralitica. Tim Horton was a hockey player but is the name of a coffee chain, which means my dream of a goat sanctuary being my legacy is not unrealistic. Do we make money or does money make us? Chezwich. Twitter is the rice of social media.

I'm still upset that Tie Domi didn't name his child Tyson. Twitter is the rice of social media. Smiling could easily be misinterpreted for showing your teeth to someone because they said something that made you happy. You should "listen to my mixtape" (check out the rest of my portfolio). For the name of an act as serious as killing someone, assassination literally translates to buttbuttination.

Most streets are two-way streets...why does that make love so special?. I have never known a Jack that was in good enough shape to name bodybuilding after him. For the name of an act as serious as killing someone, assassination literally translates to buttbuttination. We need more werkin and less twerkin if you ask me. Balooby. I started a sensory deprivation chamber business - it involves really dark curtains, ear plugs, and a sleeping mask.

I started a sensory deprivation chamber business - it involves really dark curtains, ear plugs, and a sleeping mask. I bet most serial killers play the drums. I'm still upset that Tie Domi didn't name his child Tyson. I have never known a Jack that was in good enough shape to name bodybuilding after him. I think of a lot of good ideas when going to the bathroom - I guess I have a real stream of consciousness.

If you wake up with a giant zit, you are really facing your fears when you look in the mirror. We need more werkin and less twerkin if you ask me. Balooby. Rumour has it targeted online advertising was developed because the internet was upset that you could read it but it couldn't read you. Trepidelicious. A tagline for an airline: Take the High Road. Tim Horton was a hockey player but is the name of a coffee chain, which means my dream of a goat sanctuary being my legacy is not unrealistic.

You say potatoe, I say starchy carbs. Curling is the best sport named after something you do to your hair. I'm in a band that does Metallica covers with our private parts - it's called Myphallica. Petrovache. You should "listen to my mixtape" (check out the rest of my portfolio). For the name of an act as serious as killing someone, assassination literally translates to buttbuttination.

We say we are walking the dog, but the dog always leads. We say we are walking the dog, but the dog always leads. A tagline for a special highway that is easy to navigate while under the influence of drugs: Take the High Road. I have a moral code, but I haven't figured out how to read it yet. A tagline for a car company that prides itself on its morals and ethics: Take the High Road.

For the name of an act as serious as killing someone, assassination literally translates to buttbuttination. If a dog and cat had a baby together that grew up and worked a desk job he'd be a Cog in the machine. Logan Ipsum will loop at some point. To Catch A Predator would have been a great name for a Steve Irwin show. Mintslavicia. I'm the only person in the world with my name.

Most streets are two-way streets...why does that make love so special?. I'm still upset that Tie Domi didn't name his child Tyson. You say potatoe, I say starchy carbs. You know the Grammys are a joke when Future doesn't win Best Everything. I bet most serial killers play the drums.''', align='j', new_x='LMARGIN', new_y='NEXT')

pdf.output("demo.pdf")