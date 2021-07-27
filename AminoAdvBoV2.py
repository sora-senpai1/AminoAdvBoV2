import amino
import asyncio
import pyfiglet
from colored import fore, back, style, attr
attr(0)
print(fore.THISTLE_1 + style.BOLD)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminoadvbov2", font="slant"))

async def main():
	client = amino.Client()    
	email = input("Email >> ")
	password = input("Password >> ")
	msg = input("Message >> ")
	await client.login(email=email, password=password)
	clients = await client.sub_clients(start=0, size=1000)
	for x, name in enumerate(clients.name, 1):
		print(f"{x}.{name}")
	communityid = clients.comId[int(input("Select the community >> "))-1]
	sub_client = await amino.SubClient(comId=communityid, profile=client.profile)
	while True:
		try:
			users = await sub_client.get_online_users(start=0, size=1000)
			for userId, level, nickname in zip(users.profile.userId, users.profile.level, users.profile.nickname):
				starting = await sub_client.start_chat(userId=[sub_client.profile.userId, userId], message=msg)
				print(f"Sended Advertise {nickname}, level = {level}")
		except amino.lib.util.exceptions.VerificationRequired as e:
			print(f"VerificationRequired")
			link = e.args[0]['url']
			print(link)
			verify = input("Waiting for verification >> ")
		except Exception as e:
			print(e)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
