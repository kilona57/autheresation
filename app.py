from auth_system.authentication_service import AuthSystem
from registration_system.regisration_service import RegistrationSystem


class App:
    MENU = {
        "login": AuthSystem.auth,
        "registr": RegistrationSystem.sign_up,
    }

    def run(self):
        command = input("Your choice please (login | registr)")
        do = self.MENU[command]
        do()


app = App()
app.run()
