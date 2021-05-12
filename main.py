import discord
from discord.ext import commands
bot = commands.Bot(command_prefix=':', description="Ten bot to jest moderator")
token = 'ODQxMjI5ODgxOTkxODg4OTI3.YJjuYQ.oBzdfa78vgi0LsChb1fvUJ3Dvdk'
embed = discord.Embed(title="KOMENDY", description="tutaj znajdziesz komendy tego bota", color=0x00ff91)
embed.add_field(name="1.:pomoc", value="pokazuje ta komende", inline=False)
embed.add_field(name="2.:administracja", value="pokazuje liste adminow", inline=False)
embed.add_field(name="3.:ping", value="odpowiada", inline=False)
embed.add_field(name="4.:regulamin", value="wyswietla regulamin", inline=False)

klakson = discord.Embed(title="Administracja Serwera:", description="czyli ja i moje ziomki")
klakson.add_field(name="1.@nazwa#5172", value="to wlasciciel serwera itd.", inline=False)
klakson.add_field(name="2.@radosgra#4164", value="to jest technik serwera", inline=False)
klakson.add_field(name="3.@X_PH4THOM_X#6413", value="to jest headadmin serwera", inline=False)
klakson.add_field(name="4.@Moderator Serwera#6413", value="to jestem ja i jestem modem", inline=False)
nick = 388032108104384513


@bot.command()
async def pomoc(ctx):
    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    await ctx.send('pong!')


@bot.command()
async def administracja(ctx):
    await ctx.send(embed=klakson)

@bot.command()
async def regulamin(ctx):
    await ctx.author.send('REGULAMIN:')
    await ctx.author.send('1.nie prosimy o rangi')
    await ctx.author.send('2.nie wyzywamy innych')
    await ctx.author.send('3. nie przeklinamy')
    await ctx.author.send('4. nie reklamujemy swojego kanału na yt bez odpowiedniej rangi')
    await ctx.author.send('5. nie piszemy słów typu "JD"')
    await ctx.author.send('6. piszemy na przeznaczonych do tego kanałach')
    await ctx.author.send('7. nie pingujemy nikogo z administracji bez powodu')
    await ctx.author.send('8. administracja może PINGOWAĆ jeśli ma potrzebe')
    await ctx.author.send('9. reklamujemy swoj serwer discord na przeznaczonym do tego kanale')
    await ctx.author.send('10. nie oznaczamy everyone  (administracja jesli ma potrzebe to może)')
    await ctx.author.send('11. nie udostępniamy treści erotycznych')
    await ctx.author.send('12. jesli mamy range przeznaczoną do reklamowania się to reklamujemy się MAX 2 razy na dzień (administrację nie obowiązuje)')
    await ctx.author.send('13. zakaz ustawiania nicków z przkleństwami i dziwnymi znaczkami')
    await ctx.author.send('14. nie robimy nic co moglo by zniszczyc serwer')
    await ctx.author.send('15. nieznanie regulaminu nie upoważnia do jego łamania')
    await ctx.author.send('16. nie wysyłamy dziwnych zdj')
    await ctx.author.send('17. NIE ZNAJOMOŚĆ REGULAMINU NIE ZWALNIA Z JEGO PRZESTRZEGANIA')
    await ctx.author.send('18. na kanale "MEMY piszemy jak NAJMNIEJ!')
    await ctx.author.send('Administracja może ukarać za coś nawet jesli nie ma tego w regulaminie')


@bot.command()
async def jakastamtestowa(ctx):
    await ctx.send('dziala')
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Podales zla komende")

@bot.event
async def on_ready():
    print(f'{bot.user} Polaczyl sie z discordem!')
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name="cie | Jesli cos chcesz, idz do admina"))


bot.run(token)
